from django import template
from myCookbook import views

register = template.Library()

def newIngredients(ingredients):
    newIngredients =[]
    new = []
    newIngredients = ingredients.split(":")
    newIngredients = views.grouper(3,newIngredients)
    return newIngredients
    
register.filter('newIngredients', newIngredients)

def newInstructions(instructions):
    print(instructions)
    newInstructions = instructions.replace(';',',').split(':')
    print(newInstructions)
    return newInstructions

register.filter('newInstructions',newInstructions)