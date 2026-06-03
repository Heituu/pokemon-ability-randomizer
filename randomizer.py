import requests
import random

url = "https://pokeapi.co/api/v2/ability"

response = requests.get(url, params={"limit" : 371})

dados = response.json()

hab = dados["results"]

abilities = []

for i in hab:
    abilities.append(i["name"])

n = input("Número de habilidades: ")
num = int(n)

print (random.sample(abilities, k=num))
