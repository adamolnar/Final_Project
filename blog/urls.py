from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'), 
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/publish/', views.PublishPostView.as_view(), name='publish-post'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/like/', views.PostLikeView.as_view(), name='post-like'), 
    path('post/<int:pk>/comment/update/',views.CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment/delete/',views.CommentDeleteView.as_view(), name='comment-delete'),
    path('drafts/author/', views.DraftPostAuthorListView.as_view(), name='draft-post-author-list'),
]