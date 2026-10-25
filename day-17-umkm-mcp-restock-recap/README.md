# Modul 17: Tanya Gudang Sendiri: Menyambungkan File Stok Toko ke AI lewat MCP Lokal 🌱
> **Fokus Praktik:** Track 2: Bisnis & UMKM
## Mengapa Modul Ini Penting?
Hari 14 membahas template prompt spreadsheet dan Hari 16 membahas cara melacak asal jawaban AI. Sekarang kita naik satu tingkat ke tren MCP server lokal. AI membaca file stok langsung di laptop Pak Hendra, jadi tidak ada lagi salin-tempel data dan file tidak perlu diunggah ke mana pun.
## Alur Langkah Praktis
- 1. Siapkan folder: ekspor stok & penjualan ke CSV di ~/Toko/Stok
- 2. Sambungkan konektor: daftarkan server-filesystem di konfigurasi klien MCP
- 3. Perintah ringkas: pakai template ‘Rekap Restok’ dan minta sumber baris di tiap jawaban
## Contoh Perintah / Spesimen Lokal
```bash
Terminal: npx -y @modelcontextprotocol/server-filesystem ~/Toko/Stok
Akses: hanya ~/Toko/Stok (baca saja)
File: stok_gudang.csv, penjualan_oktober.csv
Model: lokal via Ollama → 0 byte ke cloud 🌱
```

## Template Prompt Siap Pakai: Rekap Restok Mingguan dari File Stok Lokal (MCP)
> Pemilik toko kecil biasanya mencocokkan file stok gudang dan catatan penjualan secara manual setiap malam untuk tahu barang apa yang perlu dipesan ulang. Prompt ini membaca kedua file lewat MCP filesystem lokal, menghitung perkiraan hari sampai stok habis, lalu menyusun daftar restok berprioritas lengkap dengan sumber baris supaya bisa dicek ulang.

### System Instruction
```text
Kamu adalah asisten operasional toko UMKM yang teliti dan membumi. Gunakan hanya data dari file yang tersedia lewat alat MCP filesystem, dan jangan mengarang angka. Setiap angka yang kamu tulis wajib menyebut nama file dan nomor barisnya. Kalau data kurang atau tidak konsisten, katakan terus terang dan sebutkan apa yang perlu dilengkapi. Gunakan bahasa Indonesia sederhana, sapa pengguna dengan ‘kamu’, dan hindari istilah teknis yang tidak perlu.
```

### User Prompt Template (1-Tap Copy)
```text
Baca file stok [FILE_STOK] dan file penjualan [FILE_PENJUALAN] dari folder yang sudah terhubung.

Tugas:
1. Hitung rata-rata penjualan harian per barang selama [PERIODE_HARI] hari terakhir.
2. Hitung perkiraan hari sampai stok habis (stok saat ini ÷ rata-rata harian).
3. Tandai barang yang perkiraan habisnya kurang dari [LEAD_TIME_HARI] hari sebagai PRIORITAS PESAN.
4. Tandai barang yang tidak terjual sama sekali di periode tersebut sebagai STOK LAMBAT.

Format jawaban:
- Tabel: Nama Barang | Stok | Rata-rata/Hari | Perkiraan Habis (hari) | Status | Sumber (file:baris)
- Ringkasan 3 kalimat untuk pemilik toko.
- Daftar data yang hilang atau janggal (kalau ada).

Jangan menebak angka yang tidak ada di file.
```

💡 **Tips Praktis:** Mulai dengan akses baca saja ke satu folder khusus, jangan sambungkan seluruh folder Dokumen. Pastikan juga nama barang di file stok dan file penjualan ditulis persis sama (misalnya ‘Gula Pasir 1kg’, bukan ‘gula 1 kg’). Kalau penulisannya beda, AI akan menganggapnya dua barang berbeda. Rapikan namanya sekali, dan rekap malam-malam berikutnya bakal jauh lebih ringan. 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
