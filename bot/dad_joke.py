import requests


def get_dad_joke() -> str:
    response = requests.get(
        'https://icanhazdadjoke.com/',
        headers={'Accept': 'application/json'},
    )
    response.raise_for_status()

    return response.json()['joke']
