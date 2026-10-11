"""LLM clients. Anything with `complete(prompt) -> str` works; `model_id` is logged for reproducibility."""
import os
import time


class GeminiLLM:
    def __init__(self, model, temperature=0.0):
        from google import genai  # pip install google-genai
        from google.genai import types
        # no default timeout: a dead connection would hang a run forever; 120 s then the retry loop takes over
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(timeout=120_000))
        self.model_id = model
        self.temperature = temperature
        self.usage = {"prompt_tokens": 0, "completion_tokens": 0, "calls": 0}

    def complete(self, prompt, retries=6):
        from google.genai import types
        for attempt in range(retries + 1):
            try:
                r = self.client.models.generate_content(
                    model=self.model_id, contents=prompt,
                    config=types.GenerateContentConfig(temperature=self.temperature))
                u = r.usage_metadata
                self.usage["calls"] += 1
                self.usage["prompt_tokens"] += (u.prompt_token_count or 0) if u else 0
                self.usage["completion_tokens"] += ((u.candidates_token_count or 0) + (u.thoughts_token_count or 0)) if u else 0  # thinking is billed as output
                return r.text or ""
            except Exception:
                if attempt == retries:
                    raise
                time.sleep(min(60, 5 * 2 ** attempt))  # free-tier 429 asks for ~25s


class MockLLM:
    """Deterministic stand-in for tests and dry runs. `script` is a callable(prompt) -> str."""
    model_id = "mock"

    def __init__(self, script):
        self.script = script
        self.usage = {"prompt_tokens": 0, "completion_tokens": 0, "calls": 0}

    def complete(self, prompt):
        self.usage["calls"] += 1
        return self.script(prompt)
