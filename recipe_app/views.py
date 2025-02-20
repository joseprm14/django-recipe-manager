from rest_framework import viewsets, generics, permissions, authentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User, Recipe, Ingredient
from .serializers import UserSerializer, RecipeSerializer, IngredientSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
        ViewSet para la clase User con CRUD completo
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
@permission_classes([permissions.AllowAny]) # Mientras que la mayoria de views requieren estar autenticado, esta puede ser utilizada por cualquiera
def RecipeGetDetailedAPIView(request, pk):
    """
        API View que enlaza los modelos de Recipes e Ingredients para devolver la informacion completa de una receta y sus ingredientes
    """
    try:
        # Se comprueba que la receta con ese id existe
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response({"error": f'No existe la receta de id {pk}'}, status=status.HTTP_404_NOT_FOUND)
    recipe = RecipeSerializer(recipe).data
    ingredients = IngredientSerializer(Ingredient.objects.filter(recipe_id=pk), many=True).data

    ingredient_list = []
    total_calories = 0
    for i in ingredients:
        # Para cada ingrediente se añade su info a la lista y se suma su valor calorico al total
        ingredient_list.append({'name': i['name'], 'amount': i['amount']})
        total_calories += i['calories']
    response = {
        'id': recipe['id'], 
        'name': recipe['name'], 
        'time': recipe['time'], 
        'description': recipe['description'], 
        'total_calories': total_calories, 
        'ingredients': ingredient_list,
    }
    return Response(response, status=status.HTTP_302_FOUND)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
        Vista generica para obtener un usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    """
        Vista generica para crear un usuario y listar todos los usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateAPIView(generics.UpdateAPIView):
    """
        Vista generica para actualizar un usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class UserDestroyAPIView(generics.DestroyAPIView):
    """
        Vista generica para eliminar un usuario
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class RecipeRetrieveAPIView(generics.RetrieveAPIView):
    """
        Vista generica para obtener una receta
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    """
        Vista generica para crear una receta y listar todas las recetas
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeUpdateAPIView(generics.UpdateAPIView):
    """
        Vista generica para actualizar una receta
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class RecipeDestroyAPIView(generics.DestroyAPIView):
    """
        Vista generica para eliminar una receta
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class IngredientRetrieveAPIView(generics.RetrieveAPIView):
    """
        Vista generica para obtener un ingrediente
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientListCreateAPIView(generics.ListCreateAPIView):
    """
        Vista generica para crear un ingrediente y listar todos los ingredientes
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientUpdateAPIView(generics.UpdateAPIView):
    """
        Vista generica para actualizar un ingrediente
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    def perform_update(self, serializer):
        instance = serializer.save()

class IngredientDestroyAPIView(generics.DestroyAPIView):
    """
        Vista generica para eliminar un ingrediente
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
