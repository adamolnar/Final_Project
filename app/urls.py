from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path('blog/authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('blog/authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('post/create/', views.post_new, name='post-create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'), 
    path('post/<slug:slug>/update/', views.post_edit, name='post-update'),  
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/like/', views.PostLikeView.as_view(), name='post-like'), 
    path('post/<slug:slug>/comment/update/',views.CommentUpdateView.as_view(), name='comment-update'),
    path('post/<slug:slug>/comment/delete/',views.CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/update', views.edit_profile, name='profile-update'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),  
    path('explore/', views.ExploreView.as_view(), name='explore'),
]