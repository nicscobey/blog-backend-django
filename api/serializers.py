from api.models import Blog, Comment, Reply
from django.contrib.auth.models import User, Group
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, SerializerMethodField
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    # password = make_password(validated_data['password'])
    def validate_password(self, value: str) -> str:
        return make_password(value)

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
                  "theme", "created_at", "updated_at", "author", "published"]

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


class CommentSerializer(ModelSerializer):

    # author = UserSerializer()
    # blog = BlogSerializer()

    class Meta:
        model = Comment
        fields = ["id", "created_at", "updated_at",
                  "author", "content", "blog"]


class ReplySerializer(ModelSerializer):

    # author = UserSerializer()
    # blog = BlogSerializer()

    class Meta:
        model = Reply
        fields = ["id", "created_at", "updated_at",
                  "author", "content", "comment"]


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
