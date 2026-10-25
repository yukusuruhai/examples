#!/usr/bin/env python3
"""
Dual-Tier Model Router (Local Ollama Rp0 First -> Cloud Fallback) (Day 12)
Memprioritaskan GPU lokal untuk tugas privasi & murah, fallback ke cloud jika beban berat.
"""

import os
import json
import urllib.request
import urllib.error

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
LOCAL_MODEL = os.getenv("LOCAL_MODEL", "deepseek-r1:8b")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

def query_local_ollama(prompt: str, model: str = LOCAL_MODEL) -> str:
    """Mengirim kueri ke server Ollama lokal dengan biaya token Rp0."""
    url = f"{OLLAMA_HOST}/api/generate"
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    
    with urllib.request.urlopen(req, timeout=15) as res:
        data = json.loads(res.read().decode("utf-8"))
        return data.get("response", "")

def query_cloud_openrouter(prompt: str, model: str = "deepseek/deepseek-chat") -> str:
    """Fallback ke cloud inference via OpenRouter jika GPU lokal sedang offline / sibuk."""
    if not OPENROUTER_API_KEY:
        return "[Simulasi Cloud Fallback] Jawaban dari OpenRouter Cloud (API Key belum diisi)."

    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=payload, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}"
    })
    
    with urllib.request.urlopen(req, timeout=30) as res:
        data = json.loads(res.read().decode("utf-8"))
        return data["choices"][0]["message"]["content"]

def route_dual_tier(prompt: str, force_cloud: bool = False) -> str:
    """Orkestrator Dual-Tier: Prioritaskan GPU lokal terlebih dahulu."""
    if not force_cloud:
        try:
            print(f"⚡ [Tier 1: Local] Mencoba inference via GPU lokal ({LOCAL_MODEL})...")
            return query_local_ollama(prompt)
        except Exception as e:
            print(f"⚠️ [Tier 1 Offline / Timeout] {e}. Beralih ke Tier 2 (Cloud)...")
    
    print("☁️ [Tier 2: Cloud] Melakukan inferensi melalui cloud...")
    return query_cloud_openrouter(prompt)

def main():
    test_prompt = "Jelaskan dalam 2 kalimat kenapa arsitektur hybrid model lokal menghemat biaya AI."
    print("=== Demo Dual-Tier Model Router (YukSuruhAI) ===")
    response = route_dual_tier(test_prompt)
    print("\n[Hasil Respons]:")
    print(response)

if __name__ == "__main__":
    main()
