#!/usr/bin/env bash
set -e

echo "=== Setup Model Lokal 8B Rp0 via Ollama (YukSuruhAI Day 12) ==="

# 1. Deteksi apakah Ollama sudah terpasang
if ! command -v ollama &> /dev/null; then
    echo "📦 Mengunduh dan memasang Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama sudah terpasang di sistem."
fi

# 2. Tarik model open-weights yang efisien di GPU consumer / laptop
# DeepSeek-R1 8B (penalaran) atau Qwen 2.5 7B (instruksi cepat)
MODEL_NAME=${1:-"deepseek-r1:8b"}

echo "📥 Mengunduh model: $MODEL_NAME..."
ollama pull "$MODEL_NAME"

echo ""
echo "🚀 Pengujian cepat model lokal:"
ollama run "$MODEL_NAME" "Sapa rekan-rekan komunitas YukSuruhAI dalam 1 kalimat ramah!"

echo ""
echo "✅ Siap digunakan! Endpoint lokal: http://localhost:11434"
