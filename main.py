import requests
print("Bem vindo ao Weather Knowing")
print("Digite a lagitude do lugar para saber a temperatura:")
latitude = input()
print("Agora digite a longitude")
longitude = input()

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lang":"en","lon":longitude,"lat":latitude}

headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': "91cb73748dmshb3114ab1814c01cp10c4c8jsn3cf6518beb44"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()
texto = open("texto.csv", "w+")
aux = "Temperatura da cidade " + response['data'][0]['city_name'] + "  ---->  " + str(response['data'][0]['temp'])+ "ºC"
texto.write(aux)