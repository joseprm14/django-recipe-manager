from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recipes/details/<int:pk>/', views.RecipeGetDetailedAPIView),
    path('generic/users/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('generic/users/', views.UserListCreateAPIView.as_view()),
    path('generic/users/<int:pk>/update/', views.UserUpdateAPIView.as_view()),
    path('generic/users/<int:pk>/destroy/', views.UserDestroyAPIView.as_view()),
    path('recipes/<int:pk>/', views.RecipeRetrieveAPIView.as_view()),
    path('recipes/', views.RecipeListCreateAPIView.as_view()),
    path('recipes/<int:pk>/update/', views.RecipeUpdateAPIView.as_view()),
    path('recipes/<int:pk>/destroy/', views.RecipeDestroyAPIView.as_view()),
    path('ingredients/<int:pk>/', views.IngredientRetrieveAPIView.as_view()),
    path('ingredients/', views.IngredientListCreateAPIView.as_view()),
    path('ingredients/<int:pk>/update/', views.IngredientUpdateAPIView.as_view()),
    path('ingredients/<int:pk>/destroy/', views.IngredientDestroyAPIView.as_view()),
]
