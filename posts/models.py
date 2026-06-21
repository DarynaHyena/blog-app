from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=100, verbose_name="Title")
  content = models.TextField(verbose_name="Text")
  author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title} - {self.author.name}"
  
  class Meta:
    verbose_name = "Пост"
    verbose_name_plural = "Пости"
    ordering = ["-created_at"]


class Author(models.Model):
  name = models.CharField(max_length=20, verbose_name="Name")
  bio = models.TextField(verbose_name="Bio")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name}"
  
  class Meta:
    verbose_name = "Автор"
    verbose_name_plural = "Автори"
    ordering = ["-created_at"]
