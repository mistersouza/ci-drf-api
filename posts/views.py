from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly

# Views
class PostList(APIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PostDetail(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object_or_404(self, post_id):
        try:
            post = Post.objects.get(id=post_id)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, post_id):
        post = self.get_object_or_404(post_id)
        serializer = PostSerializer(
            post,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, post_id):
        post = self.get_object_or_404(post_id)
        serializer = PostSerializer(
            post,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, post_id):
        post = self.get_object_or_404(post_id)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )