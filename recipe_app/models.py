from django.db import models

class User(models.Model):
    """
        Modelo de los usuarios de la aplicación
    """
    # Solo puede haber un usuario para cada email
    email = models.CharField(max_length=255, unique=True)
    name = models.TextField()



class Recipe(models.Model):
    """
        Modelo de las recetas de la aplicación
    """
    # Cada receta tendrá el nombre, su tiempo de cocina y una descripción
    name = models.TextField()
    time = models.IntegerField() # Tiempo en minutos
    description = models.TextField()
    


class Ingredient(models.Model):
    """
        Cada instancia de esta clase contiene el nombre de un ingrediente, su cantidad y valor calorico y a que receta pertenece
    """
    name = models.CharField(max_length=255)
    amount = models.IntegerField() # Cantidad en miligramos
    calories = models.IntegerField() # Valor calorico en kilocalorias
    # recipe es la clave foranea de Recipes, relacionando ambas tablas
    # Al eliminar una receta se eliminaran sus ingredientes, de ahi on_delete=models.CASCADE
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    
    class Meta:
        # Con esto se establece que no se puede repetir un par name recipe
        unique_together = ('name', 'recipe')

