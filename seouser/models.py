from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models import Sum


class PostManager(models.Manager):

	def count_like(self,user,soc_bound):
		pass

class UserManager(models.Manager):

	def likes_user(self):
		likes=[]
		for user in self.get_queryset().order_by('id'):
			likes.append('{0}:{1}'.format(self.get_queryset().get(id=user.id).nickname,
				self.get_queryset().filter(id=user.id).filter(post__social_bound='vk').aggregate(likes = Sum('post__likes'))))
		return likes


class Social_VK_Manager(models.Manager):

	def info_social(self, user):
		pass


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