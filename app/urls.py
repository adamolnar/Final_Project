from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'), 
    path('post/<slug:slug>/update/', views.PostUpdateView, name='post-update'),  
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/like/', views.PostLikeView.as_view(), name='post-like'), 
    path('post/<slug:slug>/comment/update/',views.CommentUpdateView.as_view(), name='comment-update'),
    path('post/<slug:slug>/comment/delete/',views.CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),  
    path('explore/', views.ExploreView.as_view(), name='explore'),
]