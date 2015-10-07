from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models import Sum


class PostManager(models.Manager):

	def count_like(self,user):
		count = 0
		list_of_likes = self.get_queryset().filter(user_id=user).filter(likes__gt=0)
		for like in list_of_likes:
			count = count + like.likes
		return count

	def count_reposts(self,user):
		count = 0
		list_of_repost = self.get_queryset().filter(user_id=user).filter(reposts__gt=0)
		for repost in list_of_repost:
			count = count + repost.reposts
		return count

	def count_posts(self,user):
		count = 0
		list_of_post = self.get_queryset().filter(user_id=user)
		for post in list_of_post:
			count +=1
		return count


class UserManager(models.Manager):

	def info_user(self, user):
		return self.get_queryset().filter(nickname=user).values()[0]


class Social_VK_Manager(models.Manager):

		def info_social(self, user):
		    return self.get_queryset().filter(user_id=user).values()[0]


class SeoUser(models.Model):
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    email = models.EmailField(max_length=200)
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default="Male")
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    avatar = models.FileField(upload_to=None,max_length=100)
    objects = models.Manager()
    user_objects = UserManager()

    def __str__(self):
        return self.nickname

class Social_VK(models.Model):
    user = models.OneToOneField(SeoUser, primary_key=True)
    login = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    objects = models.Manager()
    social_objects = Social_VK_Manager()

    def __str__(self):
        return self.user.nickname

class Group(models.Model):
	name_group = models.CharField(max_length=100)
	url_group = models.CharField(max_length=100)
	user = models.ManyToManyField(SeoUser)

	def __str__(self):
		return self.user.nickname

class Post(models.Model):
	SOCIAL = (('vk','vkontakte'),('fb','facebook'),('tw','twitter'))
	post_text = models.TextField()
	date_text = models.DateTimeField('date published')
	likes = models.IntegerField(default=0)
	reposts = models.IntegerField(default=0)
	social_bound = models.CharField(max_length=10, choices=SOCIAL, default='vkontakte')
	user = models.ForeignKey(SeoUser)
	objects = models.Manager()
	post_objects = PostManager()

	def __str__(self):
		return self.user.nickname



@receiver(post_save, sender=SeoUser)
def create_user(sender, **kwards):
	s = Social_VK.objects.create(user=SeoUser.objects.last(), 
		login=SeoUser.objects.last().email,
		passwd=User.objects.make_random_password(), api_key='')