from dataclasses import field
from statistics import mode
from unicodedata import category
from django.forms import ModelForm, forms, widgets
from .models import Blog, Category
from django import forms

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['blgoTiltle' ,'blgoauther', 'blogCategory', 'blgoDetails','blogImage' ]
    

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['blgoTiltle'].widget.attrs.update({'class':'input', 'placeholder': 'Title' })
        self.fields['blgoauther'].widget.attrs.update({'class':'Select', 'placeholder': 'Select Auther'})
        self.fields['blogCategory'].widget.attrs.update({'class':'select'})
        self.fields['blgoDetails'].widget.attrs.update({'class':'input', 'placeholder': 'You Text Here ......'})
        self.fields['blogImage'].widget.attrs.update({'class':'upload'})



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


    def __int__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'input', 'placeholder': 'Category Name' })

    