import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")


weather_params = {
    "lat": 22.353439,
    "lon": 82.722191,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_='+12073897130',
        to='+918770058355'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will not rain today",
        from_='+12073897130',
        to='+918770058355'
    )
