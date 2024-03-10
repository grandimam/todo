from django.urls import path
from .views import PollDetailView
from .views import PollListingView
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('polls/', PollListingView.as_view(), name='listing'),
    path('detail/<int:pk>/', PollDetailView.as_view(), name='detail'),
    path('login/', auth_views.LoginView.as_view(template_name=''))
]
