from django import template
from seouser.models import SeoUser, Post, Social_VK
from django.db.models import Sum

register=template.Library()

@register.filter(name='likes')
def likes(value,arg):
	return SeoUser.objects.filter(id=value.id).filter(post__social_bound=arg).aggregate(likes = Sum('post__likes'))['likes']

@register.simple_tag
def colorist(value,arg):
	like = likes(value,arg)
	if like < 250:
		return "red"
	if like < 1000:
		return "yellow"
	if like > 1000:
		return "green"