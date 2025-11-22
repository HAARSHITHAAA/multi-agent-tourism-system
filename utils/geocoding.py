import requests

def geocode_place(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place_name, "format": "json", "limit": 1}
    headers = {"User-Agent": "TourismApp/1.0"}

    try:
        res = requests.get(url, params=params, headers=headers, timeout=8)
        data = res.json()
        if not data:
            return None, None, None
        return float(data[0]["lat"]), float(data[0]["lon"]), data[0]["display_name"]
    except:
        return None, None, None
