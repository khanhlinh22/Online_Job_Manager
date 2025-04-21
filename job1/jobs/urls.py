from django.contrib import admin
from django.urls import path, re_path, include
from .admin import admin_site
from rest_framework.routers import DefaultRouter
from  . import views

r= DefaultRouter()
r.register('categories', views.CategoryViewsSet, basename='cate')
r.register('recruitments', views.RecruitmentViewSet, basename='recruitment')
r.register('news', views.NewViewSet, basename='new')
r.register('users', views.UserViewSet, basename='user')
r.register('comments', views.CommentViewSet, basename='comment')


urlpatterns = [
    path('',include(r.urls))

]
