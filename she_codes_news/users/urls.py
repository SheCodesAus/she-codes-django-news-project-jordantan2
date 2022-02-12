from django.urls import path
from .views import CreateAccountView
from . import views

app_name = 'users'

urlpatterns = [
    path('<int:pk>', views.ProfileView.as_view(), name="profile"),
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('My-Stories/', views.MyStoriesView.as_view(), name='My-Stories'),
]