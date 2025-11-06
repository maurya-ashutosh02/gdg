import requests

MOCK_BASE_URL = "http://localhost:8000"

def call_api(path: str, payload: dict, timeout: int = 60):
    url = f"{MOCK_BASE_URL}{path}"
    try:
        resp = requests.post(url, json=payload, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        # Mock fallback
        if path == "/summarize":
            return {
                "tldr": "This paper proposes a hybrid attention mechanism.",
                "abstract": "Combines CNN and Transformer blocks.",
                "methodology": "Two-stage architecture with feature fusion.",
                "results": "Improves accuracy by 5%.",
                "limitations": "Not robust on noisy datasets."
            }
        if path == "/chat":
            return {"answer": "It introduces a hybrid attention model improving both efficiency and accuracy."}
        if path == "/extract":
            return {
                "keywords": ["attention", "transformer", "efficiency"],
                "datasets": ["ImageNet", "CIFAR-10"],
                "algorithms": ["ResNet-50", "ViT"]
            }
        if path == "/simplify":
            return {"simplified": "The paper mixes two ways of focusing on data to make models faster and smarter."}
        if path == "/future-work":
            return {"suggestions": ["Try on more datasets", "Reduce memory cost", "Add robustness tests."]}
        if path == "/tts":
            return {"audio_url": "https://example.com/voice.mp3"}
        return {"error": "Mock data returned."}
