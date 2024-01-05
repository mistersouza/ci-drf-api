from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image_url.url')

    def get_is_owner(self, object):
        request = self.context['context']
        return request.user == object.owner

    class Meta:
        model = Post
        filds = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image'
            'created_at',
            'updated_at',
            'title',
            'content',
            'image_url',
        ]