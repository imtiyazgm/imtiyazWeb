from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import UUIDField
import uuid

from django.db.models.fields.files import ImageField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE, null = True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='profile_images/', default ='profile_images/imtiyaz.jpeg')
    intro = models.TextField(null=True, blank=True)
    Bio = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=15)
    twitter_ac = models.CharField(max_length=100, null=True, blank=True)
    facebook_ac = models.CharField(max_length=100, null=True, blank=True)
    gitHub_ac = models.CharField(max_length=100, null=True, blank=True)
    linkedin_ac = models.CharField(max_length=100, null=True, blank=True)
    cv_doc =models.FileField(null=True, blank=True, upload_to='CV/', default ='CV/ImtiyazCV.pdf')
    createdDate = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)



class WorkExpirnce(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    orgName = models.CharField(max_length=50)
    orgLocation = models.CharField(max_length=50)
    startDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    EndDate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    position = models.CharField(max_length=50)
    orgIntro = models.TextField()
    responsibility = models.ManyToManyField('Responsibility', blank=True)
    
    def __str__(self):
        return self.orgName

class Responsibility(models.Model):
    responsibility = models.CharField(max_length=500, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
   
    def __str__(self):
        return self.responsibility




