from django.contrib import admin
from django.urls import path, include
from main_app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('webapp', views.webapp, name='webapp'),
    path('CommentList', views.CommentList.as_view(), name='CommentList'),
    path('forum_post', views.forum_post, name='forum_post')
]