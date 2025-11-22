import streamlit as st
from utils.geocoding import geocode_place
from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent

st.title("🌍 Multi-Agent Tourism System")

place = st.text_input("Enter a place to visit:")

if st.button("Search"):
    if not place.strip():
        st.warning("Please enter a place.")
        st.stop()

    lat, lon, name = geocode_place(place)

    if not lat:
        st.error("I’m not aware this place exists.")
        st.stop()

    st.success(f"Location found: {name}")

    weather_agent = WeatherAgent()
    places_agent = PlacesAgent()

    weather = weather_agent.get_weather(lat, lon)
    places = places_agent.get_places(lat, lon)

    st.subheader("☁️ Weather")
    if weather:
        st.json(weather)
    else:
        st.write("Weather API failed.")

    st.subheader("📍 Nearby Attractions")
    if places:
        for p in places:
            st.write(f"- {p['name']}")
    else:
        st.write("No attractions found.")
