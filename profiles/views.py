from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Profile
from .serializers import ProfileSerializer


# Views
class ProfileList(APIView):
    def get(self, request): 
        profiles = Profile.objects.all() 
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

class ProfileDetail(APIView):
    serializer_class = ProfileSerializer
    def get(self, request, profile_id):
        profile = get_object_or_404(Profile, id=profile_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    def put(self, request, profile_id):
        profile = get_object_or_404(Profile, id=profile_id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
