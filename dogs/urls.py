from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import DogListView, CategoriesListView, DogCreateView, DogUpdateView, DogDeleteView, IndexView

app_name = DogsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('dogs/<int:pk>/', DogListView.as_view(), name='category_dogs'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]

