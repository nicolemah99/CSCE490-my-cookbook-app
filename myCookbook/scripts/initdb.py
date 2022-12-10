import csv
from myCookbook.models import User,Recipe,Category
from django.utils.text import slugify

FNAME1 = "myCookbook/seeddata/users.csv"
FNAME2 = "myCookbook/seeddata/recipes.csv"
FNAME3 = "myCookbook/seeddata/categories.csv"

def run():
    print(f'Reading file: {FNAME1}')
    with open(FNAME1) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            username = row["username"]
            first_name  = row["first_name"]
            last_name  = row["last_name"]
            email = row["email"]
            bio = row["bio"]
            slug = slugify(username)

            User.objects.get_or_create(username=username,first_name=first_name,last_name=last_name,email=email,bio=bio, slug=slug)

    print(f'Reading file: {FNAME2}')
    with open(FNAME2) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            print(row['author'])
            author = User.objects.get(username=row['author'])
            name  = row["name"]
            instructions  = row["instructions"]
            ingredients = row["ingredients"]
            description = row["description"]
            num_servings = row["num_servings"]
            min = row["min"]
            image = row["image"]
            slug = slugify(name+author.first_name)

            Recipe.objects.get_or_create(author=author,name=name, slug=slug, instructions=instructions, ingredients=ingredients, description=description, num_servings=num_servings, min=min,image=image)
    
    print(f'Reading file: {FNAME3}')
    with open(FNAME3) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            name  = row["name"]

            Category.objects.get_or_create(name=name)