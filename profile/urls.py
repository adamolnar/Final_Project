from . import views
from django.urls import path



urlpatterns = [
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'), 
    path('logout/', views.logout_and_redirect, name='logout_and_redirect'),
]