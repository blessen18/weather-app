# Weather App

A Python command-line app that shows current weather for any city
using the OpenWeatherMap API.

## Features
- Temperature, feels-like, condition, humidity and wind speed
- Error handling for invalid cities, bad keys and network issues

## Setup
1. Clone the repo
2. Create a virtual environment and install dependencies:
   pip install -r requirements.txt
3. Get a free API key from openweathermap.org
4. Copy `.env.example` to `.env` and add your key
5. Run: python weather_app.py

## Built with
Python, requests, python-dotenv