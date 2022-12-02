from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    THEMES = (
        ('light', 'White'),
        ('dark', 'Black'),
        ('secondary', 'Grey'),
        ('primary', 'Blue'),
        ('success', 'Green'),
        ('warning', 'Yellow'),
        ('danger', 'Red'),
        ('info', 'Teal'),
    )
    bio = models.TextField(max_length=500, blank=True)
    num_recipes_saved = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name="Number of Servings")
    num_recipes_posted = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name="Total Time")
    profile_image = models.ImageField(upload_to='images/profileImages/',
                                      default='images/profileImages/default_profile.png', null=True, blank=True, verbose_name="Profile Image")
    theme = models.CharField(default=THEMES[0], max_length=9, choices=THEMES)

    def __str__(self):
        return f"{self.username}"

    def get_full_name(self) -> str:
        return super().get_full_name()

    def get_username(self) -> str:
        return super().get_username()


class Recipe(models.Model):
    RATINGS = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.TextField(max_length=64)
    instructions = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    description = models.TextField(max_length=500)
    date_posted = models.DateField(
        default=date.today, verbose_name="Date Posted")
    num_servings = models.IntegerField(null=True,validators=[MinValueValidator(1)])
    min = models.IntegerField(null=True, validators=[
                              MinValueValidator(1), MaxValueValidator(1000)])
    rating = models.IntegerField(null=True, default=0,choices=RATINGS)
    savers = models.ManyToManyField(
        User, blank=True, related_name="saved_recipes")
    image = models.ImageField(upload_to='myCookbook/images/recipeImages',
                              default='myCookbook/images/recipeImages/defaultImage.jpeg', blank=True, verbose_name="Recipe Image")
    def __str__(self):
        return f"{self.name}"
    
        
class Ingredient(models.Model):
    UNITS = (
        ('NA', 'NA'),
        ('Lbs', 'Pounds'),
        ('Oz', 'Ounces'),
        ('C', 'Cups'),
        ('Tb', 'Tablespoon'),
        ('Ts', 'Teaspoon')
    )
    recipe = models.ForeignKey(Recipe,default=1, on_delete=models.CASCADE)
    name = models.TextField(max_length=64, null=True)
    amount = models.FloatField(default=0.0, validators=[
                               MinValueValidator(0.0)])
    units = models.CharField(max_length=3, null=True, choices=UNITS)

    def __str__(self):
        return f"{self.amount} {self.units} {self.name}"
