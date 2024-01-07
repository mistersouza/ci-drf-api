from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    '''
    The Comment model serializer enhances
    the output for lists of Comment instances by
    including three additional fields.
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, object):
        request = self.context['request']
        return request.user == object.owner
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'post',
            'created_at',
            'updated_at',
            'content'
        ]

class CommentsDetailSerializer(CommentSerializer):
    '''
    The Comment model serializer is utilized within the Detail view. 
    The 'Post' field is designated as read-only,
    eliminating the need for its explicit assignment during updates.
    '''
    post = serializers.ReadOnlyField(source='owner.post.id')