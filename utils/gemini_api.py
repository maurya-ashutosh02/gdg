# utils/gemini_api.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_summarize(text):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    Summarize this research paper text in structured sections:
    - TL;DR Summary
    - Abstract Summary
    - Methodology Overview
    - Results & Findings
    - Limitations

    Text:
    {text[:15000]}
    """
    response = model.generate_content(prompt)
    return response.text

def gemini_chat(query, context):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    You are a research paper assistant. Based on the paper content below,
    answer this question clearly and accurately.

    Paper:
    {context[:10000]}

    Question:
    {query}
    """
    response = model.generate_content(prompt)
    return response.text
