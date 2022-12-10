from django import template
from myCookbook import views

register = template.Library()

def newIngredients2(ingredients):
    print(ingredients)
    newIngredients =[]
    
    for i in ingredients:
        str = ''
        for item in i:
            str = str + ' ' + item
        str = str.lstrip(' ')
        newIngredients.append(str)

    return newIngredients
    
register.filter('newIngredients', newIngredients2)

def newIngredients(ingredients):
    print(ingredients)
    newIngredients =[]
    new = []
    newIngredients = ingredients.split(":")
    newIngredients = views.grouper(3,newIngredients)
    print(newIngredients)
    return newIngredients
    
register.filter('newIngredients', newIngredients)