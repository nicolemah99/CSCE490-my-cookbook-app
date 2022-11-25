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
    num_recipes_saved = models.IntegerField(default=0)
    num_recipes_posted = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='myCookbook/static/myCookbook/images',
                                      default='myCookbook/static/myCookbook/images/default_profile.png', blank=True, verbose_name="Profile Image")
    theme = models.CharField(max_length=9, choices=THEMES)

    def __str__(self):
        return f"{self.name}"

    def get_full_name(self) -> str:
        return super().get_full_name()

    def get_username(self) -> str:
        return super().get_username()

class Recipe(models.Model):
    RATINGS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.TextField(max_length=64)
    description = models.TextField(max_length=500)
    date_posted = models.DateField(default=date.today, verbose_name = "Date Posted")
    num_servings = models.IntegerField(default=0)
    min = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(1000)])
    rating = models.PositiveSmallIntegerField(choices=RATINGS)
    savers = models.ManyToManyField(User, blank=True, related_name="saved_recipes")

class RecipeIngredient(models.Model):
    UNITS = (
        ('Lbs', 'Pounds'),
        ('Oz', 'Ounces'),
        ('C', 'Cups'),
        ('Tb', 'Tablespoon'),
        ('Ts', 'Teaspoon')
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    quantity = models.DecimalField(decimal_places= 2,max_digits=3)
    units = models.CharField(max_length=3, choices= UNITS)