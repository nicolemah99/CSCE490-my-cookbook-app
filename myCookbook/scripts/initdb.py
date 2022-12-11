import csv
from myCookbook.models import User,Recipe,Category,Review
from django.utils.text import slugify

FNAME1 = "myCookbook/seeddata/users.csv"
FNAME2 = "myCookbook/seeddata/recipes.csv"
FNAME3 = "myCookbook/seeddata/categories.csv"
FNAME4 = "myCookbook/seeddata/reviews.csv"

def run():
    print(f'Reading file: {FNAME3}')
    with open(FNAME3) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            name  = row["name"]

            Category.objects.get_or_create(name=name)

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

            User.objects.get_or_create(username=username,first_name=first_name,last_name=last_name,email=email,bio=bio, slug=slug, is_staff=True, password='1234')

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
            cat1 = Category.objects.get(name=row['category1'])
            cat2 = Category.objects.get(name=row['category2'])

            slug = slugify(name+author.first_name)

            Recipe.objects.get_or_create(author=author,name=name, slug=slug, instructions=instructions, ingredients=ingredients, description=description, num_servings=num_servings, min=min,image=image)
            recipe = Recipe.objects.get(slug=slug)
            recipe.categories.add(cat1,cat2)

    print(f'Reading file: {FNAME4}')
    with open(FNAME4) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            reviewer = User.objects.get(username=row['reviewer'])
            recipe  = Recipe.objects.get(name=row["recipe"])
            subject  = row["subject"]
            rating = row["rating"]
            review = row["review"]

            Review.objects.get_or_create(reviewer=reviewer,recipe=recipe,subject=subject,rating=rating,review=review)
