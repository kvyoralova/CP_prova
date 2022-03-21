import streamlit as st #'import _ as _' means that you're "assigning" a shorter "variable" to the library
st.header("Hello world") #the text function displays the text between quotes and brackets
title = st.text_input("Gimme a movie title:")
st.write("The current movie title is ", title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

import json, requests 

# add your own APIkey
APIkey = '70e487a499248adf2ee563c7908c7ac0'
location = st.text_input('Give me a city you want to know the weather: ')

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=&units=metric' + location + '&appid=' + APIkey
# print(url)

# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

print(weatherData['main']['temp_max']) 
