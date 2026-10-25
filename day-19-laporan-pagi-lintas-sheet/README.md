# Modul 19: Satu Laporan Pagi dari Tiga Sheet Berantakan: Merangkai Spreadsheet, MCP Lokal, dan Model Lokal jadi Satu Alur Rp0 🌱
> **Fokus Praktik:** Arsitektur Lokal & Efisiensi Kerja Rp0
## Mengapa Modul Ini Penting?
Hari 17 dan 18 sudah membahas cara menyambungkan satu file ke MCP dan cara mengamankan servernya. Hari ini kita menyatukan potongan-potongan itu jadi satu alur hybrid yang dipakai setiap pagi. Tim tetap mengisi Google Sheets seperti biasa, sementara pembacaan dan peringkasan berjalan di laptop sendiri. Jadi friction kerja nyata yang paling sering muncul, yaitu menyalin angka dari banyak sheet, bisa selesai tanpa biaya dan tanpa data mentah keluar.
## Alur Langkah Praktis
- 1. Ekspor: unduh tiap sheet ke ~/toko/sheets sebagai CSV
- 2. Sambungkan: MCP server read-only hanya ke folder itu
- 3. Rangkum: pakai template prompt, wajib sebut file & baris sumber
## Contoh Perintah / Spesimen Lokal
```bash
$ ls ~/toko/sheets → pesanan.csv stok.csv kas.csv
$ chmod -R a-w ~/toko/sheets   # kunci read-only
$ npx -y @modelcontextprotocol/server-filesystem ~/toko/sheets
$ ollama run qwen2.5:7b "Susun laporan pagi dari 3 file"
Egress ke AI cloud: 0 byte 🌱
```

## Template Prompt Siap Pakai: Laporan Pagi Lintas Sheet (Pesanan, Stok, Kas)
> Pemilik usaha dan admin operasional yang tiap pagi menyalin angka dari beberapa spreadsheet bisa memakai prompt ini untuk menggabungkan data pesanan, stok, dan kas jadi satu laporan pagi yang ringkas. Setiap angka di laporan wajib menyebut file dan baris sumbernya.

### System Instruction
```text
Kamu adalah asisten operasional yang teliti dan membumi. Kamu hanya memakai data yang diberikan, dan dilarang menebak atau mengarang angka. Setiap angka yang kamu tulis wajib diberi label sumber dalam format [nama_file:baris]. Kalau data tidak lengkap atau antar-sheet tidak cocok, tulis secara jujur di bagian 'Perlu Dicek Manual', jangan ditutupi. Gunakan bahasa Indonesia yang santai tapi jelas, dan sapa pembaca dengan 'kamu'.
```

### User Prompt Template (1-Tap Copy)
```text
Susun laporan pagi untuk tanggal [TANGGAL_LAPORAN] dari tiga sumber data berikut.

=== pesanan.csv ===
[DATA_PESANAN]

=== stok.csv ===
[DATA_STOK]

=== kas.csv ===
[DATA_KAS]

Aturan:
1. Tulis tepat 5 baris ringkasan: total pesanan, total omzet, produk terlaris, stok di bawah [BATAS_STOK] unit, dan selisih kas vs omzet.
2. Setiap angka wajib diberi sumber [nama_file:baris].
3. Tambahkan bagian 'Perlu Dicek Manual' untuk data yang kosong, ganjil, atau tidak cocok antar-sheet.
4. Tutup dengan 1 saran tindakan paling penting untuk hari ini.
5. Jangan menambahkan data yang tidak ada di sumber.
```

💡 **Tips Praktis:** Tambahkan kolom 'baris' di setiap CSV sebelum diumpankan ke model, karena label sumber jadi jauh lebih akurat kalau nomor barisnya tertulis jelas. Satu lagi: kalau bagian 'Perlu Dicek Manual' kosong selama seminggu berturut-turut, jangan langsung lega. Cek ulang 2–3 angka secara acak, karena kepercayaan pada alur otomatis dibangun dari kebiasaan memeriksa, bukan dari asumsi 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
