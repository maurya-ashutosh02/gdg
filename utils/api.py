# utils/api.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
from gtts import gTTS
import base64
import tempfile
# Load environment variables (from .env)
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -----------------------------
# Helper functions for Gemini
# -----------------------------
def summarize_paper(text: str):
    """Use Gemini to summarize research paper text into sections."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    You are an academic assistant. Summarize this research paper into the following sections:
    - TL;DR Summary
    - Abstract Summary
    - Methodology Overview
    - Results & Findings
    - Limitations

    Return your answer as structured JSON with keys:
    tldr, abstract, methodology, results, limitations.

    Research Paper:
    {text[:15000]}
    """
    response = model.generate_content(prompt)
    return _extract_json(response.text)


def chat_with_paper(query: str, context: str):
    """Ask Gemini a question about the uploaded paper."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    You are a research assistant. Based on the following paper, answer clearly and concisely.

    Paper:
    {context[:10000]}

    Question:
    {query}
    """
    response = model.generate_content(prompt)
    return {"answer": response.text}


def extract_insights(text: str):
    """Extract keywords, datasets, and algorithms from the paper."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    From this research paper text, extract the following:
    - Top 5 keywords
    - Datasets used
    - Algorithms mentioned

    Return JSON with keys: keywords, datasets, algorithms.
    Text:
    {text[:10000]}
    """
    response = model.generate_content(prompt)
    return _extract_json(response.text)


def simplify_summary(text: str):
    """Simplify the summary for a younger audience."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    Simplify this research summary as if explaining to a 15-year-old. Use short, clear sentences:
    {text[:4000]}
    """
    response = model.generate_content(prompt)
    return {"simplified": response.text}


def future_research_ideas(text: str):
    """Suggest possible future research directions."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    Based on this paper, suggest 3-5 possible future research directions or open problems.
    Return a numbered list.
    {text[:8000]}
    """
    response = model.generate_content(prompt)
    return {"suggestions": response.text.splitlines()}


# -----------------------------
# API Dispatcher
# -----------------------------
def call_api(path: str, payload: dict):
    text = payload.get("text", "")
    query = payload.get("query", "")
    context = payload.get("context", "")

    if path == "/summarize":
        return summarize_paper(text)
    elif path == "/chat":
        return chat_with_paper(query, context)
    elif path == "/extract":
        return extract_insights(text)
    elif path == "/simplify":
        return simplify_summary(text)
    elif path == "/future-work":
        return future_research_ideas(text)
    elif path == "/tts":
        return generate_tts(payload.get("text", ""))
    elif path == "/compare":
        return compare_papers(payload.get("text_a", ""), payload.get("text_b", ""))


    else:
        return {"error": f"Unknown path: {path}"}


# -----------------------------
# Helper: Extract JSON safely
# -----------------------------
import json, re

def _extract_json(response_text: str):
    """Extract and safely parse JSON from model output."""
    try:
        json_text = re.search(r'\{.*\}', response_text, re.DOTALL).group(0)
        return json.loads(json_text)
    except Exception:
        # fallback heuristic if model doesn't return proper JSON
        return {"raw_response": response_text}


def generate_tts(text: str):
    """Generate an MP3 from text and return it as base64 for Streamlit playback."""
    text = text.strip()
    if not text:
        return {"error": "Empty text — nothing to read."}

    try:
        # Shorten overly long text to avoid gTTS limit
        if len(text) > 4500:
            text = text[:4500] + " ... summary truncated."

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts = gTTS(text=text, lang="en", slow=False, tld="com")
            tts.save(tmp.name)
            with open(tmp.name, "rb") as f:
                audio_bytes = f.read()

        # Encode to base64 for Streamlit playback
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

        os.remove(tmp.name)
        return {"audio_base64": audio_base64}

    except Exception as e:
        return {"error": f"TTS generation failed: {str(e)}"}
    
def compare_papers(text_a: str, text_b: str):
        """Use Gemini to compare two research papers and return structured insights."""
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        You are an academic comparison assistant.

        Compare these two research papers and provide:
        1. 3–5 key differences between them
        2. 3–5 key similarities
        3. A short summary paragraph highlighting which paper offers stronger contributions or novelty

        Format your response as JSON with keys:
        - "differences": [list of strings]
        - "similarities": [list of strings]
        - "summary": "string"

        --- PAPER A ---
        {text_a[:15000]}

        --- PAPER B ---
        {text_b[:15000]}
        """

        response = model.generate_content(prompt)
        return _extract_json(response.text)
