# Modul 16: Angka Ini Dari Mana? Membangun Jejak Jawaban AI yang Bisa Kita Cek Sendiri 🌱
> **Fokus Praktik:** Edukasi Umum & Anti-Halusinasi
## Mengapa Modul Ini Penting?
Hari 12–15 sudah membahas arsitektur lokal, template prompt, dan hemat token. Hari ini kita masuk ke kepercayaan: setiap jawaban AI harus bisa ditelusuri ke sel sumbernya dan dicatat di log lokal yang saling terkunci hash, mengikuti tren ledger penalaran yang bisa diverifikasi dan MCP server lokal.
## Alur Langkah Praktis
- 1. Wajibkan sitasi: setiap angka harus menyebut tab & sel (mis. Penjualan!B14)
- 2. Cocokkan otomatis: skrip membaca sel itu, kalau beda maka ditolak
- 3. Catat & kunci: tulis ke jejak.log dengan hash baris sebelumnya
## Contoh Perintah / Spesimen Lokal
```bash
$ npx -y @modelcontextprotocol/server-filesystem ./laporan-oktober
$ PREV=$(tail -1 jejak.log | sha256sum | cut -c1-16)
$ echo "$(date -I) | omzet Q3 | sel B14 | prev:$PREV" >> jejak.log
Egress cloud: 0 byte (Ollama lokal) 🌱
```

## Template Prompt Siap Pakai: Jejak Jawaban AI: Rujukan Sel Spreadsheet & Verifikasi Hash
> Template prompt anti-halusinasi yang mewajibkan AI mencantumkan alamat sel/baris asli dari tabel sebelum ringkasan dikirim ke atasan atau klien.

### System Instruction
```text
Kamu adalah asisten audit data. Dilarang menyebutkan angka tanpa mencantumkan alamat sel atau baris sumbernya secara eksplisit.
```

### User Prompt Template (1-Tap Copy)
```text
Berikut adalah data tabel dari spreadsheet kerja kita:
"""
[DATA_TABEL_SHEET]
"""

Tolong buatkan ringkasan laporan dengan aturan ketat:
1. Setiap angka WAJIB diikuti rujukan baris/kolom aslinya dalam tanda kurung siku, contoh: Rp 12.500.000 [Baris 4, Kolom Omzet].
2. Jika ada pertanyaan yang angkanya tidak tersedia di tabel, tulis dengan jujur: [BELUM ADA DI TABEL — JANGAN DITEBAK].
3. Buat 1 baris log ringkas di akhir dalam format: TANGGAL | TOPIK | SEL_RUJUKAN | STATUS_VERIFIKASI.
```

💡 **Tips Praktis:** Simpan baris log verifikasi ke file lokal dan kunci dengan sha256sum agar jejak laporanmu selalu bisa ditelusuri ulang 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
