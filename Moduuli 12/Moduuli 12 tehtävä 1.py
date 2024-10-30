import requests

def hae_vitsi():
    pyynto=requests.get('https://api.chucknorris.io/jokes/random')
    joke=pyynto.json()['value']
    return joke

print(hae_vitsi())
