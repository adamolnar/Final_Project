from . import views
from django.urls import path


urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>/',
         views.AuthorDetailView.as_view(), name='author-detail'),
    path('message-author/<int:author_id>/',
         views.MessageAuthorView.as_view(), name='message-author'),
    path('request-author-access/', views.RequestAuthorAccessView.as_view(),
         name='request-author-access'),

]
