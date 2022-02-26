import requests
from twilio.rest import Client

# api key of openweather
api_key = "Your API key"
end_point = "https://api.openweathermap.org/data/2.5/onecall"

# twilio account info
account_sid = "twilio sid"
auth_token = "twilio token"

# Location of Area whose weather you want
my_lat = 30.913170
my_long = 75.849541

weather_params = {
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

# api call from openweather website
api = requests.get(end_point, params=weather_params)
api.raise_for_status()
weather_data = api.json()

will_rain = False

# checking weather of first 12 hours of day
weather_hourly = weather_data["hourly"][:12]
for i in range(12):
    weather_id = weather_hourly[i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    # message format for sms
    message = client.messages.create(
        body="It's going to rain today, bring an Umbrella",
        # temp. mobile no. given by twilio
        from_="phone_no",
        # mobile no. should registered in twilio website to send sms.
        to='any_phone_no'
    )

    print(message.status)