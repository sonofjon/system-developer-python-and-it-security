import requests

api_url = "https://api.github.com/users/sonofjon/repos"

response = requests.get(api_url)
for repo in response.json():
    print(repo["name"])
