from django.db import models
from django.contrib.auth.models import User # User 모델의 사속
from django.db.models.signals import post_save
from django.dispatch import receiver

# user db는 있는 상태 -> sqllite db에서 확인해보면 auth_user로 들어가 있음
# 구축하고자 하는 바에서는 현재 Profile 모델은 필요 없는 상태 
# -> 이 모델의 구조 user의 요소가 들어 있는 부분을 일대일 관계가 아니라 일대다 관계로 하여 필드로 넣어 기존의 userdata, crawldata의 모델을 세워 사용할 것


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True) #User라는 모델이 지금 django.contrib.auth.models로부터 import
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Userdata(models.Model):
    user = models.ForeignKey(User, null=False)
    key = models.CharField(max_length=200)
    url = models.TextField()



class Crawldata(models.Model): # 무엇을 더 추가 할지.
    user = models.ForeignKey(User, null=False)
    title = models.CharField(max_length=200)
    url = models.TextField()
    reg_date = models.TextField(default='-')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
