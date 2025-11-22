import requests

API_KEY = "pk.01417d1c60545ef937bdc2f2d3eb36db"

def geocode_place(place_name):
    url = "https://us1.locationiq.com/v1/search"
    params = {
        "key": API_KEY,
        "q": place_name,
        "format": "json",
        "limit": 1
    }

    try:
        res = requests.get(url, params=params, timeout=10)
        data = res.json()

        if isinstance(data, dict) and data.get("error"):
            return None, None, None

        if not data:
            return None, None, None

        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        display_name = data[0]["display_name"]

        return lat, lon, display_name

    except Exception as e:
        print("Geocoding error:", e)
        return None, None, None
