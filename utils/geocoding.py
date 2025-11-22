import requests

def geocode_place(place_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place_name, "format": "json", "limit": 1}
    
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; TourismApp/1.0; +https://example.com)",
        "Accept-Language": "en-US,en;q=0.5"
    }

    try:
        res = requests.get(url, params=params, headers=headers, timeout=10)
        data = res.json()
        if not data:
            return None, None, None
        return float(data[0]["lat"]), float(data[0]["lon"]), data[0]["display_name"]
    except:
        return None, None, None
