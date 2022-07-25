import requests, json
api_address='http://api.openweathermap.org/data/2.5/weather?appid=Your Api&q='
city_name=input("Enter the name of city : ")
url = api_address + city_name
json_data = requests.get(url).json()
print(json_data)
