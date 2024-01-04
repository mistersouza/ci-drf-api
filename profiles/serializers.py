from rest_framework import serializers
from .models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    onwer = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id',
            'onwer',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image_url',
        ]
