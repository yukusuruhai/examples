# Modul 24: Restock Tanpa Tebak-Tebakan: Minta AI Membaca 4 Minggu Penjualan di Sheet, Keputusan Tetap di Tanganmu 🌱
> **Fokus Praktik:** Track 2: Bisnis & UMKM
## Mengapa Modul Ini Penting?
Banyak anggota komunitas non-teknis bingung harus mulai pakai AI dari mana. Titik masuk paling membumi untuk pemilik UMKM adalah data yang sudah mereka punya, yaitu sheet penjualan. Materi ini melanjutkan kebiasaan cek sumber dari Hari 22 dan label klaim dari Hari 23 ke keputusan bisnis yang mereka hadapi tiap minggu: mau restock apa.
## Alur Langkah Praktis
- 1. Ekspor 4 minggu penjualan + stok terakhir ke CSV
- 2. Jalankan prompt Asisten Restock (isi lead time supplier)
- 3. Cek 3 angka acak ke sheet asli, lalu putuskan sendiri
## Contoh Perintah / Spesimen Lokal
```bash
$ head -3 penjualan-4-minggu.csv
  tanggal,sku,nama,terjual,stok_akhir
$ ollama run qwen2.5:7b "$(cat prompt-restock.txt penjualan-4-minggu.csv)"
Egress: 0 byte, file tidak meninggalkan laptop 🌱
```

## Template Prompt Siap Pakai: Asisten Restock Mingguan dari Sheet Penjualan
> Pemilik UMKM sering memutuskan restock berdasarkan insting karena menghitung manual dari sheet penjualan itu melelahkan. Akibatnya modal nyangkut di barang lambat dan barang laris kehabisan. Prompt ini mengubah 4 minggu data penjualan menjadi rekomendasi restock yang bisa diaudit. Setiap angka menyebut baris sumbernya, dan keputusan akhir tetap di tangan pemilik.

### System Instruction
```text
Kamu adalah asisten analis stok untuk usaha kecil. Bersikaplah membumi, jujur, dan hati-hati. Hitung hanya dari data yang diberikan. Jangan menebak tren pasar, musim, atau harga yang tidak ada di data. Setiap angka yang kamu sebut wajib mencantumkan SKU dan baris sumber. Jika data tidak cukup untuk menghitung (misalnya kurang dari 3 minggu data atau stok akhir kosong), tulis 'DATA KURANG' beserta alasannya. Kamu memberi rekomendasi, bukan keputusan. Gunakan bahasa Indonesia sederhana dan sapa pengguna dengan 'kamu'.
```

### User Prompt Template (1-Tap Copy)
```text
Bantu aku menyusun rekomendasi restock minggu ini.

DATA PENJUALAN (CSV, 4 minggu terakhir):
[DATA_PENJUALAN]

WAKTU TUNGGU SUPPLIER: [LEAD_TIME_HARI] hari
BATAS MODAL BELANJA MINGGU INI: [BATAS_MODAL]

Langkah yang aku minta:
1. Untuk setiap SKU, hitung rata-rata terjual per minggu dan sebutkan baris sumbernya.
2. Hitung perkiraan stok habis dalam berapa hari: stok_akhir ÷ (rata-rata mingguan ÷ 7).
3. Beri label: MENIPIS (habis sebelum barang dari supplier tiba), AMAN, atau LAMBAT (stok cukup lebih dari 4 minggu).
4. Usulkan jumlah restock untuk yang MENIPIS supaya cukup untuk 2 minggu plus waktu tunggu, dan jangan melebihi batas modal.
5. Tulis 3 angka yang paling penting aku cek ulang ke sheet asli.

Format jawaban: tabel (SKU | Nama | Rata-rata/minggu | Hari sampai habis | Label | Usulan restock | Baris sumber), lalu daftar 'Perlu Dicek Manual' dan 'DATA KURANG' jika ada.
```

💡 **Tips Praktis:** Mulai dari 10 barang terlarismu dulu, jangan langsung seluruh katalog. Setelah AI menjawab, ambil 3 angka acak dan cocokkan ke sheet asli. Kalau ketiganya cocok, baru kamu pakai rekomendasinya. Kalau ada yang meleset, itu bukan gagal, justru itu tanda kamu sudah memegang kendali. 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
