from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('authors/', views.AuthorList.as_view(), name='all_authors'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    
    
   
]