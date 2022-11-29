# Generated by Django 4.1.3 on 2022-11-28 18:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myCookbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='quantity',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='amount',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='myCookbook.RecipeIngredient', to='myCookbook.ingredient'),
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myCookbook.ingredient'),
        ),
    ]
