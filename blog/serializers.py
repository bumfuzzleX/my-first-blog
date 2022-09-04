from rest_framework import serializers
from .models import Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author' ,'title', 'content', 'image', 'created_date', 'published_date')
