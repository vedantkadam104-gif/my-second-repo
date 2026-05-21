import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

temp = data['current_condition'][0]['temp_C']
description = data['current_condition'][0]['weatherDesc'][0]['value']
humidity = data['current_condition'][0]['humidity']

print("City:", city)
print("Temperature:", temp, "°C")
print("Weather:", description)
print("Humidity:", humidity, "%")