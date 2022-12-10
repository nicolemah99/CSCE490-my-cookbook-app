from django import template
from myCookbook import views
from datetime import datetime

register = template.Library()

def newIngredients(ingredients):
    newIngredients =[]
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

def convertDate(value):
    return value.date()
register.filter('convertDate',convertDate)