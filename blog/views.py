from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Post

# Create your views here.

class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Post.objects.all()