# YukSuruhAI — Contoh, Template & Skrip Otomasi Praktis 🌱

Selamat datang di repositori resmi contoh kode, template prompt, dan skrip otomasi **YukSuruhAI**.

Repositori ini ditujukan untuk siapa saja yang ingin menerapkan kecerdasan buatan (AI) secara praktis, teruji, dan bebas dari *hype* kosong. Seluruh materi di sini disusun menggunakan prinsip **Satu Tema, Tiga Lensa**:
1. **Lensa Awam (Track 1 — Yuk Pakai AI):** Template prompt siap pakai untuk produktivitas kerja harian tanpa koding.
2. **Lensa Bisnis / UMKM (Track 2 — Yuk Otomasi):** Menghubungkan spreadsheet, bot chat, dan alur operasional untuk memangkas biaya dan waktu.
3. **Lensa Software Engineer (Track 3 — Yuk Bikin AI):** Arsitektur agen AI, Model Context Protocol (MCP), constrained schema decoding, dan model open-weights lokal (Rp0 token).

---

## 🌐 Katalog & Portal Web Interaktif
Kunjungi portal interaktif kami untuk **1-tap copy** prompt langsung dari HP:  
👉 **[https://yukusuruhai.github.io/examples/](https://yukusuruhai.github.io/examples/)**

Bergabung ke grup diskusi dan tanya jawab gratis:  
💬 **[Telegram Komunitas YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9)**

---

## 📂 Daftar Direktori Contoh & Template

| Hari | Topik & Lensa | File & Aset yang Disediakan |
|:---|:---|:---|
| **Hari 1** | **Kamus 15 Prompt Sakti Anti-Pusing** (Awam & Bisnis) | [`day-01-kamus-prompt-anti-pusing/kamus-prompt.md`](day-01-kamus-prompt-anti-pusing/kamus-prompt.md) |
| **Hari 6** | **MCP Server Pertamamu dalam 30 Baris Kode** (Engineer) | [`day-06-mcp-server-30-baris/server.ts`](day-06-mcp-server-30-baris/server.ts), [`server.py`](day-06-mcp-server-30-baris/server.py) |
| **Hari 8** | **Otomasi Notulensi Rapat & Action Items** (Produktivitas) | [`day-08-notulensi-rapat/extract_meeting_notes.py`](day-08-notulensi-rapat/extract_meeting_notes.py), [`prompt-notulensi.md`](day-08-notulensi-rapat/prompt-notulensi.md) |
| **Hari 9** | **Ekstraksi Nota & Kwitansi ke Google Sheets** (Bisnis/UMKM) | [`day-09-nota-to-sheets/Code.gs`](day-09-nota-to-sheets/Code.gs), [`prompt-ocr-nota.md`](day-09-nota-to-sheets/prompt-ocr-nota.md) |
| **Hari 10** | **Pangkas 80% Cek Stok: Google Sheets + Bot Telegram** (Bisnis) | [`day-10-telegram-bot-cek-stok/Code.gs`](day-10-telegram-bot-cek-stok/Code.gs), [`telegram_stock_bot.py`](day-10-telegram-bot-cek-stok/telegram_stock_bot.py) |
| **Hari 11** | **Output JSON Tanpa Patah (Pydantic / Zod)** (Engineer) | [`day-11-json-schema-pydantic-zod/schema_validation.py`](day-11-json-schema-pydantic-zod/schema_validation.py), [`schema_validation.ts`](day-11-json-schema-pydantic-zod/schema_validation.ts) |
| **Hari 12** | **Arsitektur Model Lokal 8B Rp0 via Ollama** (Engineer & Bisnis) | [`day-12-ollama-local-model-rp0/setup-ollama.sh`](day-12-ollama-local-model-rp0/setup-ollama.sh), [`local_router.py`](day-12-ollama-local-model-rp0/local_router.py) |
| **Hari 13** | **Sortir Otomatis Folder Downloads Berdasarkan Isi** (Awam & Dev) | [`day-13-sortir-folder-downloads/sort_downloads.py`](day-13-sortir-folder-downloads/sort_downloads.py) |
| **Hari 14** | **Persiapan Senin: 7 Template Prompt & SOP Bebas Lembur** (Semua) | [`day-14-persiapan-senin-7-prompt-sop/7-prompt-eksekusi-mandiri.md`](day-14-persiapan-senin-7-prompt-sop/7-prompt-eksekusi-mandiri.md), [`SOP-Spreadsheet-Bebas-Lembur.md`](day-14-persiapan-senin-7-prompt-sop/SOP-Spreadsheet-Bebas-Lembur.md) |

---

## 🛠️ Cara Menggunakan Repositori Ini

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/yukusuruhai/examples.git
   cd examples
   ```

2. **Jalankan Skrip Pilihanmu**:
   - Skrip Python hanya menggunakan pustaka standar atau dependensi minimal (`pip install httpx pydantic` jika diperlukan).
   - Skrip TypeScript dapat dijalankan langsung dengan `npx tsx <file>.ts` atau `bun <file>.ts`.

---

## 📜 Lisensi
Seluruh kode dan template prompt dalam repositori ini berlisensi **MIT**. Bebas digunakan, dimodifikasi, dan diterapkan untuk bisnis maupun keperluan pribadi Anda.
