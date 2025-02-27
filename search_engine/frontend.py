import json

import requests
import streamlit as st

st.title("GIR exercise - 2024W")

text_input = st.text_input(
    "Enter a search query 👇",
)

if text_input:
    url = "http://localhost:6000/ir-search-service"
    response = requests.get(
        url=url,
        data=json.dumps({"text": text_input, "size": 10}),
        headers={"Content-Type": "application/json"},
    )
    docs = response.json()["documents"]
    for i, doc in enumerate(docs):
        st.write(f"### {i+1}: ", doc["_id"])
        with st.expander("Details", expanded=True):
            code = f"""{json.dumps(doc, indent=2)}"""
            st.code(code, language="json")
