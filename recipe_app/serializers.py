from rest_framework import serializers
from .models import User, Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """
        Este serializador devuelve todos los atributos del modelo Ingredients
    """
    class Meta:
        model = Ingredient
        fields = '__all__'
        

class RecipeSerializer(serializers.ModelSerializer):
    """
        Este serializador devuelve todos los atributos del modelo Recipes
    """
    class Meta:
        model = Recipe
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
        Este serializador devuelve todos los atributos del modelo Users
    """
    class Meta:
        model = User
        fields = '__all__'
