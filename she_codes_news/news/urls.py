from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("<int:pk>/", views.StoryView.as_view(), name="story"),
    path("", views.IndexView.as_view(), name="index"),
    path("add-story/", views.AddStoryView.as_view(), name="newStory"),
    path("<int:pk>/delete-story/", views.DeleteStoryView.as_view(), name="deleteStory"),
    path("category/<str:slug>/", views.CategoryView.as_view(), name="category"),
]
