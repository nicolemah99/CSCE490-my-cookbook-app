import csv
from myCookbook.models import User,Recipe

FNAME = "scripts/initdb.py"
def run():
    print(f'Reading file: {FNAME}')
    with open(FNAME) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f'Processsing: {row}')
            username = row["username"]
            first_name  = row["first_name"]
            last_name  = row["last_name"]
            email = row["email"]
            bio = row["bio"]

            User.objects.get_or_create(username=username,first_name=first_name,last_name=last_name,email=email,bio=bio)