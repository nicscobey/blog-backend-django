from django.shortcuts import render
from rest_framework import serializers
from api.models import Blog
from api.serializers import BlogSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class BlogViews(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
