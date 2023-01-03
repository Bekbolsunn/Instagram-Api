# package imports
from rest_framework import serializers

# local import
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=150)
    # image = serializers.ImageField()
    # description = serializers.CharField(max_length=255)

    class Meta:
        model = Post
        fields = '__all__'
