import os
import django
from faker import Faker

# Initial setup to use Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_4_project.settings")
django.setup()

# Imports must be placed after inital setup
from user_app.models import User   # or user built-in User class

fake = Faker()
number_of_users = 8
for _ in range(number_of_users):
    u = User(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.ascii_email())
    u.save()
