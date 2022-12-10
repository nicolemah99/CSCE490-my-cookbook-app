from datetime import date
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True)
    num_recipes_saved = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name="Number of Recipes Saved")
    num_recipes_posted = models.IntegerField(
        default=0, validators=[MinValueValidator(0)], verbose_name="Number of Recipes Posted")
    profile_image = models.ImageField(upload_to='myCookbook/images/recipeImages',
                                      default='myCookbook/images/recipeImages/default_profile.png', null=True, blank=True, verbose_name="Profile Image")

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User,self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"

class Recipe(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    slug = models.SlugField(null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="recipes")
    instructions = models.TextField(null=True)
    ingredients = models.TextField(null=True)
    description = models.TextField(max_length=500)
    date_posted = models.DateField(
        default=date.today, verbose_name="Date Posted")
    num_servings = models.IntegerField(null=True,validators=[MinValueValidator(1)])
    min = models.IntegerField(null=True, validators=[
                              MinValueValidator(1), MaxValueValidator(1000)])
    savers = models.ManyToManyField(
        User, blank=True, related_name="saved_recipes")
    image = models.ImageField(upload_to='myCookbook/images/recipeImages',
                              default='myCookbook/images/recipeImages/defaultImage.jpeg', blank=True, verbose_name="Recipe Image")
    def __str__(self):
        return f"{self.name}"

    def toggle_saver(self, user):
        user_saved = self.savers.filter(id=user.id).exists()
        if user_saved:
            self.savers.remove(user)
        else:
            self.savers.add(user)

    def saver_count(self):
        return len(self.savers.all())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + self.author.first_name)
        super(Recipe,self).save(*args, **kwargs)

class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="reviews")
    subject = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])
    review = models.TextField(max_length=500)


    def __str__(self):
        return f"{self.subject}"
