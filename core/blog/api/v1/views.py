from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrReadOnly


"""@api_view(["GET", "POST"])
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
        return Response(serilizers.data)"""


'''class PostListAPIView(ListCreateAPIView):
    """getting a list and create of posts. """
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializers
    permission_classes = [IsAdminUser]
'''

"""
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
        return Response({'detail':'item removed'}, status=status.HTTP_204_NO_CONTENT)"""


'''class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    """ Getting list update and delete of posts in details """
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializers
    permission_classes = [IsAdminUser]'''


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author"]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]

    # def list(self, request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     post = get_object_or_404(self.queryset, pk=pk)
    #     serializer = self.permission_classes(post)
    #     return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
