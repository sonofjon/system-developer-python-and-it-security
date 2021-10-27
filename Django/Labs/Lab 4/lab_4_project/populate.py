import os
import django

# Initial setup to use Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab_4_project.settings")
django.setup()

# Imports must be placed after inital setup
from user_app.models import User   # or user built-in User class

u = User(first_name="First", last_name="Last", email="First.Last@domain.com")
u.save()
