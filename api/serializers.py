from api.models import Blog
from rest_framework.serializers import ModelSerializer


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "subtitle", "content",
                  "theme", "created_at", "updated_at"]
