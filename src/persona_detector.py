import os
import streamlit as st

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def detect_persona(message):

    msg = message.lower()

    technical_keywords = [
        "api",
        "token",
        "server",
        "authentication",
        "error",
        "log"
    ]

    frustrated_keywords = [
        "frustrated",
        "nothing works",
        "angry",
        "urgent",
        "terrible"
    ]

    executive_keywords = [
        "operations",
        "business",
        "impact",
        "revenue",
        "deadline"
    ]

    if any(
        word in msg
        for word in technical_keywords
    ):
        return "Technical Expert"

    if any(
        word in msg
        for word in frustrated_keywords
    ):
        return "Frustrated User"

    if any(
        word in msg
        for word in executive_keywords
    ):
        return "Business Executive"

    return "Business Executive"