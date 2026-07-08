from router import route_claim

import streamlit as st
from extractor import extract_text, extract_fields
import json

st.set_page_config(page_title="Insurance Claim Agent")

st.title("🚗 Autonomous Insurance Claims Processing Agent")

uploaded_file = st.file_uploader(
    "Upload FNOL Document",
    type=["pdf", "txt"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("📄 FNOL Document")
    st.text_area("Document Text", text, height=300)

    if st.button("Process Claim"):

        with st.spinner("Extracting information..."):

            fields = extract_fields(text)

            route = route_claim(fields)

            st.subheader("✅ Extracted Fields")
            st.json(fields)

            st.subheader("🚦 Routing Result")
            st.json(route)

    