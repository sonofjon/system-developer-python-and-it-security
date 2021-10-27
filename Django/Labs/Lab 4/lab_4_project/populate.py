from user_app.models import User   # or user built-in User class

u = User(first_name="First", last_name="Last", email="First.Last@domain.com")
u.save()
