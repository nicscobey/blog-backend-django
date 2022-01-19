from api.models import Blog
from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, SerializerMethodField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email",
                  "first_name", "last_name", "groups"]


class BlogSerializer(ModelSerializer):

    # author = SerializerMethodField('get_id_from_author')
    # author = UserSerializer()

    class Meta:
        model = Blog
        fields = ["id", "title", "subtitle", "content",
                  "theme", "created_at", "updated_at", "author"]

    # def get_id_from_author(self, blog):
    #     author = blog.author.id
    #     print(author)
    #     print('🌴🌴🌴')
    #     return author

    # def create(self, request):
    #     if request.method == 'POST':
    #         print('🌴🌴🌴')
    #         print(self)
    #         print(request)


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
