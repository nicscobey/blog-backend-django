from django.shortcuts import render
from rest_framework import serializers
from api.models import Blog
from api.serializers import BlogSerializer, UserSerializer, GroupSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class BlogViews(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def create_blog(request):
        blog_obj = Blog(title=request.title, subtitle=request.subtitle,
                        content=request.content, theme=request.theme, author=request.author)
        return blog_obj


class UserViews(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class GroupViews(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (JWTAuthentication,)
