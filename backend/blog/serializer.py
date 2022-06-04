
from rest_framework import serializers

from blog.models import BlogPost, BlogPost_History
from blog.models import BlogStatuses
from users.models import UserRoles


class AbstractBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ("is_active",)
        extra_kwargs = {
            "author": {"required": False},
            "id": {"read_only": True}

        }
        fields = '__all__'


class BlogPostSerializer(AbstractBlogPostSerializer):
    class Meta(AbstractBlogPostSerializer.Meta):
        model = BlogPost

    def create(self, validated_data):
        usertype = self.context["request"].user.user_role
        if(usertype == UserRoles.ADMIN):
            validated_data["status"] = BlogStatuses.INTIALREVIEW
        return super().create(validated_data)
 


class BlogPost_ReviewSerializer(AbstractBlogPostSerializer):
    class Meta(AbstractBlogPostSerializer.Meta):
        model = BlogPost_History
        extra_kwargs = {
            "author": {"required": False},
            "id": {"read_only": True},
            "basepost":{"required": False}
        }

    def create(self, validated_data):
        validated_data["status"] = BlogStatuses.DRAFT
        return super().create(validated_data)
