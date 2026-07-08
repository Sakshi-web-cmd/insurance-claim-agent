import pdfplumber
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    return ""


def extract_fields(text):

    prompt = f"""
Extract the following fields from this FNOL document.

Return ONLY valid JSON.

Fields:
- Policy Number
- Policyholder Name
- Effective Dates
- Date
- Time
- Location
- Description
- Claimant
- Third Parties
- Contact Details
- Asset Type
- Asset ID
- Estimated Damage
- Claim Type
- Attachments
- Initial Estimate

Document:
{text}
"""

    response = model.generate_content(prompt)

    response_text = response.text.strip()

    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "").replace("```", "").strip()

    print(response_text)   # Optional: helps with debugging

    return json.loads(response_text)