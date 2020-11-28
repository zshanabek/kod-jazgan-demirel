from django.urls import path
from .views import PostListView, PostDetailView, search_post

urlpatterns = [
    path('posts', PostListView.as_view(), name='posts-list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='posts-detail'),
    path('search', search_post, name='search')
]
