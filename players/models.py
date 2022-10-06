from datetime import date
from email.mime import image
from random import choice
from django.db import models
from django.dispatch import receiver
from django.forms import CharField
from django.utils.text import slugify
from django.db.models.signals import post_delete,pre_save
from django.conf import settings
from traitlets import default
from accounts.models import Account

class Player(models.Model):
    def upload_location(instance,filename):
        file_path = 'players-images/{name}/{name}-{filename}'.format(
            name = str(instance.name),filename=filename
        )
        return file_path
    
    foot= (('Left','Left'),
             ('Right','Right'),
             ('Both',('Both')),
             )
    name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length = 50,blank = True,null = True)
    strong_foot = models.CharField(max_length=11,choices=foot)
    image = models.ImageField(upload_to=upload_location, blank=True,null=True)
    image2 = models.ImageField(blank=True,null=True)
    image3= models.ImageField(blank=True,null=True)
    position = models.CharField(max_length=100)
    kit_number = models.IntegerField(unique=True)
    slug = models.SlugField(blank=True, unique=True)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    contract = models.CharField(max_length=10)
    year_joined = models.CharField(blank=True,null=True,max_length=4)
    age = models.PositiveIntegerField(blank=True,null=True)
    DOB = models.DateField(blank= True,null=True)
    PAC = models.PositiveIntegerField(default=0)
    SHO = models.PositiveIntegerField(default=0)
    PAS = models.PositiveIntegerField(default=0)
    DRI = models.PositiveIntegerField(default=0)
    DEF = models.PositiveIntegerField(default=0)
    PHY = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    
class match(models.Model):
    match_type = models.CharField(max_length = 100,default='Friendly')
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    time  = models.TimeField()
    date = models.DateField()
    kit = models.CharField(max_length=100)
    goal_scorers = models.CharField(max_length=200, blank=True,null=True)
    played = models.BooleanField(default=False)
    meteors_logo = models.ImageField(blank=True)
    oponent_logo = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title

    
class Team(models.Model):
    def upload_location(instance,filename):
        file_path = 'Team-images/{name}-{filename}'.format(
            name = str(instance.name),filename=filename
        )
        return file_path
    image = models.ImageField(upload_to=upload_location)
    
class Officials(models.Model):
    def upload_location(instance,filename):
        file_path = 'officials-images/{name}/{name}-{filename}'.format(
            name = str(instance.name),filename=filename
        )
        return file_path
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_location,null=True,blank=True)
    bio = models.TextField(null = True,blank=True)
    
    
    
# to delete image after post has been deleted
@receiver(post_delete, sender=Player)
def submission_delete(sender, instance,**kwargs):
    instance.image.delete(False)
    
@receiver (post_delete,sender=Team)
def submission_delete(sender, instance,**kwargs):
    instance.image.delete(False)
    
@receiver (post_delete,sender=Officials)
def submission_delete(sender, instance,**kwargs):
    instance.image.delete(False)
        
# to save slug   
def pre_save_blog_post_reciever(sender, instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.kit_number) +'-'+ instance.name
pre_save.connect(pre_save_blog_post_reciever,sender=Player)