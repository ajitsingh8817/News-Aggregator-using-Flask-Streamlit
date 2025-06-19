import streamlit as st
import requests

API_URL = "http://localhost:5000/api/news"

st.set_page_config(page_title="News Aggregator", layout="wide")
st.title("📰 News Aggregator (Frontend)")

# Sidebar filters
country = st.sidebar.selectbox("Select Country", ["in", "us", "gb", "au", "ca"])
category = st.sidebar.selectbox("Select Category", [
    "general", "business", "entertainment", "health", "science", "sports", "technology"
])
query = st.sidebar.text_input("Search Keyword (optional)")

# Build API query
params = {
    "country": country,
    "category": category,
}
if query:
    params["q"] = query

# Fetch from backend
try:
    res = requests.get(API_URL, params=params)
    data = res.json()

    if data["status"] == "success":
        for article in data["articles"]:
            st.subheader(article["title"])
            if article["image"]:
                st.image(article["image"], width=600)
            st.write(article["description"])
            st.markdown(f"[Read More]({article['url']})")
            st.markdown("---")
    else:
        st.error("❌ Error: " + data.get("message", "Unknown Error"))

except Exception as e:
    st.error(f"Failed to connect to backend: {e}")
