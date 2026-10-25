# Arsitektur Rp0 di Laptop Sendiri: Menjalankan Model Lokal 8B via Ollama (Day 12)

Kenapa harus membayar ratusan ribu hingga jutaan rupiah per bulan jika tugas merangkum dokumen dan klasifikasi teks internal bisa dijalankan gratis di GPU laptop sendiri?

## The Hybrid Stack
- **Data Rahasia / Dokumen Kantor:** Diproses 100% lokal di mesin sendiri menggunakan model open-weights (DeepSeek-R1 8B atau Qwen 2.5 7B) via **Ollama**.
- **Tugas Penalaran Kompleks:** Diteruskan secara terfilter ke cloud inference (DeepSeek-V3 / Claude) via router cerdas.

## Cara Menggunakan:
1. Pasang Ollama & tarik model:
   ```bash
   chmod +x setup-ollama.sh
   ./setup-ollama.sh
   ```
2. Jalankan router pengujian:
   ```bash
   python local_router.py
   ```
