import os
import streamlit as st
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_response(
    query,
    persona,
    retrieved_docs
):

    context = "\n\n".join(
        [doc.page_content for doc in retrieved_docs]
    )

    prompt = f"""
You are a customer support assistant.

Detected Persona:
{persona}

Knowledge Base Context:
{context}

User Query:
{query}

Rules:

1. ONLY use information from the provided context.
2. Do not invent information.
3. If information is unavailable, say so.

Persona Style:

Technical Expert:
- Detailed
- Technical
- Root cause focused
- Step-by-step

Frustrated User:
- Empathetic
- Reassuring
- Action oriented

Business Executive:
- Concise
- Outcome focused
- Minimal technical jargon

Generate the response.
"""

    response = model.generate_content(
        prompt
    )

    return response.text