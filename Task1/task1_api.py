import requests
import matplotlib.pyplot as plt

api_key = "9bc3fbaa41cc34bcfe20e6e5898e10cd"

# List of cities (You can change names anytime)
cities = ["Hyderabad", "Visakhapatnam"]

temperatures = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if "main" in data:
        temp = data["main"]["temp"]
        temperatures.append(temp)
        print(city, "Temperature:", temp)
    else:
        print("Error for", city)

# Graph
plt.bar(cities, temperatures)
plt.title("Temperature of Different Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.show()