from django.urls import path, include
from . import views

app_name = "api-v1"

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')
urlpatterns = router.urls


# urlpatterns = [
    # path("post/", views.PostListAPIView.as_view(), name="post-list"),
    # path("post/<int:pk>/", views.PostDetailAPIView.as_view(), name="post-detail"),
    # path("post/<int:pk>/", views.PostViewSet.as_view({'get': 'list', 'get': 'retrieve'}), name="post-list"),
    # path("post/<int:pk>/", views.PostViewSet.as_view({'get': 'retrieve'}), name="post-detail"),  
# ]