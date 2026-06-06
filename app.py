import streamlit as st
import requests

S_URL = st.secrets["server_base_url"].rstrip("/")


st.title("🌤 AI Weather Agent")
city=st.text_input("Enter City")

question=st.text_input("what is the weather like")

if st. button("Ask Agent"):
    res=requests.post(f"{S_URL}/get_weather",params={
        "city":city,
        "question":question
    })

    st.success(res.json()["messages"][-1]["content"])
      