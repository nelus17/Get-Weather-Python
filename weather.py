import pyowm

city = input("What city are you interested in? ")

owm = pyowm.OWM("Your API KEY")

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("In the city " + city + " now " + str(temperature) + " celsius")
print("Also in the specified city " + w.get_detailed_status() + " and wind speed is " + str(w.get_wind()['speed']) + " m/s")
print("Humidity is the " + city + " is " + str(w.get_humidity()))
