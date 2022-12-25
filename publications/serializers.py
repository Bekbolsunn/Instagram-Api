# package imports
from rest_framework import serializers

# local import
from .models import Post
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    image = serializers.ImageField()
    file = serializers.FileField()
    description = serializers.CharField(max_length=255)
    total_likes = serializers.SerializerMethodField()
    liked_by = UserSerializer(many=True)
    views = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'image',
            'file',
            'description',
            'date_created',
            'liked_by',
            'total_likes',
            'views',
            'author',
        ]

    def get_total_likes(self, instance):
        return instance.total_likes.count()

    def get_total_likes_by(self, instance):
        return instance.liked_by.all().count()

    def get_total_views(self, instance):
        return instance.views.count()
