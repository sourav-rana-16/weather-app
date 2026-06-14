from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if request.method == "POST":
        city = request.POST.get("city")
    else:
        city = "Chandigarh"

    api_key = "4f3a4d0e42ffa50df564c0a2ae210527"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    params = {
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            raise KeyError

        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        humidity=data["main"]["humidity"]
        wind=data["wind"]["speed"]
        day = datetime.date.today()

        context = {
            "description": description,
            "icon": icon,
            "temp": temp,
            "humidity": humidity,
            "wind": wind,
            "day": day,
            "city": city,
            "exception_occurred": False,
        }

    except Exception:
        messages.error(request, "City not found!")

        context = {
            "description": "Clear Sky",
            "icon": "01d",
            "temp": 25,
            "day": datetime.date.today(),
            "city": "Chandigarh",
            "exception_occurred": True,
        }

    return render(request, "home.html", context)