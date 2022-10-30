from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import IndexView, PostCreateView, PostListView, PostDetailView, PostCreateView

# Create your tests here.


class TestUrl(SimpleTestCase):

    def test_index_url_reverse(self):
        """
        Test that the index view returns the correct URL.
        """
        url = reverse('blog:index')
        self.assertEquals(resolve(url).func.view_class, IndexView)


    def test_post_list_url_reverse(self):
        """
        Test that the post list view returns the correct URL.
        """
        url = reverse('blog:post-list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_post_detail_url_reverse(self):
        """
        Test that the post detail view returns the correct URL.
        """
        url = reverse('blog:post-detail', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
