from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import PostSerializers
from blog.models import Post
from django.shortcuts import get_object_or_404



@api_view(["GET", "POST"])
@permission_classes([IsAdminUser])
def postlist(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serilizers = PostSerializers(posts, many=True) 
        return Response(serilizers.data)

    elif request.method == "POST":
        serilizers = PostSerializers(data=request.data)
        serilizers.is_valid(raise_exception=True)
        serilizers.save()
        return Response(serilizers.data)

@api_view(["GET", "PUT", "DELETE"])
def postdetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = PostSerializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE" :
        post.delete()
        return Response({'detail':'item removed'}, status=status.HTTP_204_NO_CONTENT)

