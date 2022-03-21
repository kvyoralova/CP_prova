import streamlit as st #'import _ as _' means that you're "assigning" a shorter "variable" to the library
st.header("Hello world") #the text function displays the text between quotes and brackets
title = st.text_input("Gimme a movie title:", "- insert a title here -")
st.write("The current movie title is ", title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")

     
import json, requests 
import streamlit as st

#add your own APIkey
APIkey = '70e487a499248adf2ee563c7908c7ac0'
location = st.text_input('Give me a city you want to know the weather: ', "London")

#check API documentation to see what structure of URL is needed to access the data
#http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
#print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
#print(response.text)  


#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
st.write(weatherData) 

#pprint(weatherData)
st.write("The maximum temperature at", location, "is", weatherData['main']['temp_max'])


#add your own APIkey
APIkey = '70e487a499248adf2ee563c7908c7ac0'
location = st.radio("Give me a city you want to know the weather",('Prague', 'Rome', 'London'))

#check API documentation to see what structure of URL is needed to access the data
#http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
#print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
#print(response.text)  


#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
#print(weatherData) 

#pprint(weatherData)
st.write("The maximum temperature at", location, "is", weatherData['main']['temp_max'])

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", weatherData['main']['temp']+"°C", "1.2 °F")
col2.metric("Wind", weatherData['wind']['speed']+"kmh", "-8%")
col3.metric("Humidity", weatherData['main']['humidity']+"%", "4%")
