from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.blogList, name='blog_list'),
    path('blog_TableList', views.blogTableList, name='blog_TableList'),
    path('blog_Details/<str:pk>', views.blogDetails, name='blog_Details'),
    path('creat_Blog/',views.creatBlog, name='creat_Blog'),
    path('creat_Category/',views.creatCategory, name='creat_Category'),
    path('update_Blog/<str:pk>',views.updateBlog, name='update_Blog'),
    path('delete_Blog/<str:pk>',views.deleteBlog, name='delete_Blog'),
    
       
   ]