from django.urls import path
from . import views
from .views import (
    PostLiveView, UserPostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostLiveView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', PostCreateView.as_view(), name='add_post'),
    path('contact/', views.ContactView.as_view(), name='blog-contact'),
    path('calendar/', views.calendar_404, name='blog-calendar'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]












# path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),