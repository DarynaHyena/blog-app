from django.shortcuts import render
from posts.models import Post, Author

def posts_list_view(request):
  posts = Post.objects.all()
  context = {
    'posts': posts,
  }
  print(context)
  return render(
    request,
    'posts/list.html',
    context
  )

def posts_detail_view(request, pk):
  pass

def authors_list_view(request):
  pass

def authors_detail_view(request, pk):
  pass