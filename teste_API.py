import requests


def buscar_dados():
    request = requests.get("https://api.github.com/users/peeemax")
    print(request.json())

buscar_dados()