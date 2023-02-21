"""
This code uses the Geopy library to geocode a user's input for a city name,
and then uses the PyEphem library to calculate the sunrise and sunset times for that location (in UTC).

Script by: MrLunk
https://github.com/mrlunk/
"""

from geopy.geocoders import Nominatim
import ephem
from datetime import datetime

# Create a geolocator object
geolocator = Nominatim(user_agent="my_app")

# Get user input for city
city = input("Enter a city name: ")

# Use geolocator to get coordinates
location = geolocator.geocode(city)

# Set observer location using coordinates
observer = ephem.Observer()
observer.lat = str(location.latitude)
observer.lon = str(location.longitude)

# Set sunrise and sunset times
sun = ephem.Sun(observer)
sunrise = observer.previous_rising(sun).datetime()
sunset = observer.next_setting(sun).datetime()

# Print coordinates and UTC times of sunrise and sunset
print(f"Latitude: {location.latitude}\nLongitude: {location.longitude}")
print(f"Sunrise: {sunrise:%Y-%m-%d %H:%M:%S UTC}")
print(f"Sunset: {sunset:%Y-%m-%d %H:%M:%S UTC}")
