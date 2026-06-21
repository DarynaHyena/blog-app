from django.urls import path
from posts.views import *

urlpatterns = [
  path('posts/', posts_list_view, name='posts-list'),
  path('posts/detail/<int:pk>', posts_detail_view, name='posts-details'),
  
  path('authors/', authors_list_view, name='authors-list'),
  path('authors/detail/<int:pk>', authors_detail_view, name='authors-details'),
]