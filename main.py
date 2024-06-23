import streamlit as st
import requests
import pandas as pn
from datetime import datetime

api_key = '798b3252cf086c9ec2a6db57521fc2b5'
GEONAMES_USERNAME = 'eleanor.vardi'
geonames_url = 'http://api.geonames.org/timezoneJSON'


def get_timezone(lat, lon):
    url = f'{geonames_url}?lat={lat}&lng={lon}&username={GEONAMES_USERNAME}'
    response = requests.get(url)
    data = response.json()
    return data['time']


def format_time(time_str):
    time_obj = datetime.fromisoformat(time_str)
    formatted_time = time_obj.strftime('%A, %B %d, %Y %I:%M %p')
    return formatted_time

df = pn.read_csv('data/worldcities.csv')
cities = df['city']
st.title("My First Weather Checker App")
city = st.selectbox('Pick a city', cities)
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + api_key)
x = r.json()
y = x['main']
st.write('The weather in ', city, 'is ', x['weather'][0]['description'], '. temperature is: ', y['temp'])
lat = x['coord']['lat']
lon = x['coord']['lon']
current_time = get_timezone(lat, lon)
formatted_time = format_time(current_time)
st.write(f"The current time in {city} is {formatted_time}")
