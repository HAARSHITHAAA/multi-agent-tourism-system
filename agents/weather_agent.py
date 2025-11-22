import requests

class WeatherAgent:
    def get_weather(self, lat, lon):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,weather_code",
            "timezone": "auto"
        }

        try:
            res = requests.get(url, params=params, timeout=8)
            data = res.json()
            return data.get("current", {})
        except:
            return None
