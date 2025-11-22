import requests

class PlacesAgent:
    def get_places(self, lat, lon):
        query = f"""
        [out:json][timeout:15];
        (
          node["tourism"="attraction"](around:5000,{lat},{lon});
        );
        out 5;
        """
        url = "https://overpass-api.de/api/interpreter"

        try:
            res = requests.post(url, data=query, timeout=15)
            data = res.json()

            return [
                {
                    "name": el["tags"].get("name", "Unnamed place"),
                    "lat": el.get("lat"),
                    "lon": el.get("lon")
                }
                for el in data.get("elements", [])[:5]
            ]
        except:
            return None
