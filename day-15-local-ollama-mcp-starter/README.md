# Modul 15: Otomasi Tanpa Boncos Token: Praktik Otomasi Lokal di Laptop Sendiri 🌱
> **Fokus Praktik:** Track 1: Produktivitas & Karyawan
## Mengapa Modul Ini Penting?
Menjawab pertanyaan berulang di Telegram tentang cara menghubungkan AI ke file lokal tanpa biaya API bulanan.
## Alur Langkah Praktis
- 1. Unduh model lokal
- 2. Tentukan folder data
- 3. Jalankan pipeline
## Contoh Perintah / Spesimen Lokal
```bash
npx @modelcontextprotocol/server
Latensi: 120ms
Biaya per eksekusi: Rp0 🌱
```

## Template Prompt Siap Pakai: Otomasi Berkas Lokal Tanpa Boncos Token (Ollama + MCP)
> Template instruksi untuk memerintahkan model lokal (Ollama) memilah dan merangkum berkas kerja lewat MCP filesystem dengan biaya Rp0 dan 0 byte cloud egress.

### System Instruction
```text
Kamu adalah asisten otomasi lokal yang teliti, hemat token, dan hanya merujuk pada isi berkas yang diberikan.
```

### User Prompt Template (1-Tap Copy)
```text
Tolong baca dan susun ringkasan terstruktur dari berkas kerja lokal berikut:
"""
[ISI_BERKAS_LOKAL]
"""

Format keluaran wajib:
1. Ringkasan Inti (maksimal 3 poin beserta kutipan baris/angka asli).
2. Daftar Tindak Lanjut (Action Items) yang jelas.
3. Peringatan jika ada data yang belum lengkap (jangan menebak angka).
```

💡 **Tips Praktis:** Jalankan bersama model lokal (seperti llama3 atau deepseek-r1 di Ollama) dan MCP server-filesystem agar 100% gratis (Rp0) dan data tidak keluar dari laptopmu 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
