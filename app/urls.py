from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('profile/<username>/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('authors/', views.AuthorList.as_view(), name='all_authors'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]