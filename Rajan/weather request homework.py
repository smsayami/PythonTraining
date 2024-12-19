import requests
city =input("please type the name of city :\n")
city_weather =requests.get('http://api.weatherapi.com/v1/current.json?key=4f33cfe373ec4ec2a68175917240112&q=irving&aqi=no')
current_weather =city_weather.json()
temperature_in_C =current_weather['current']['temp_c']
temperature_in_F =current_weather['current']['temp_f']
print('The current temperature of' ,city, 'is:')
print('Temperature in Celsius:', temperature_in_C,)
print('Temperature in Fahrenheit:', temperature_in_F,)