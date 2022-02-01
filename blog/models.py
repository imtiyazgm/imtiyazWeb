from django.db import models
from django.db.models.deletion import CASCADE
from users.models import Profile
import uuid

# for rich text editor 
from ckeditor.fields import RichTextField

from django.db.models.fields.files import ImageField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)   
    cat_intro = models.TextField(null=True, blank=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return (self.name)

class Blog(models.Model):
    blgoTiltle = models.CharField(max_length=50, null=True, blank=True)
    blgocreatedDate = models.DateField(auto_now_add=True)
    blgoauther=models.ForeignKey(Profile, on_delete=CASCADE, null=True, blank=True)
    blogCategory = models.ForeignKey(Category, on_delete=CASCADE, null=True, blank=True)
    blgoDetails = RichTextField(null=True, blank=True)
    blogImage = models.ImageField(null=True, blank=True, upload_to='blog_images/', default ='blog_images/default.jpeg')
    #blgoDetails = models.TextField(null=True, blank=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return (self.blgoTiltle)

