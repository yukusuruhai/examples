# Modul 29: Satu Vendor Ditulis 5 Cara? Rapikan Kolom Sheet yang Berantakan Bareng AI, Kamu Tetap yang Memutuskan 🌱
> **Fokus Praktik:** Track 1: Produktivitas & Karyawan
## Mengapa Modul Ini Penting?
Sinyal komunitas menunjukkan banyak teman non-teknis bingung mulai dari mana. Merapikan satu kolom Sheet yang berantakan adalah langkah kecil yang langsung terasa manfaatnya, dan nyambung dengan materi jujur soal mana kerja mesin dan mana keputusan manusia (Hari 27) serta prioritas mingguan dari Sheet (Hari 28).
## Alur Langkah Praktis
- 1. Salin satu kolom berantakan ke file CSV
- 2. Jalankan prompt, lalu cek tabel padanan, terutama yang ditandai PERLU_CEK
- 3. Tempel kolom 'Nama Baku' ke Sheet, pakai VLOOKUP, pivot ulang
## Contoh Perintah / Spesimen Lokal
```bash
$ ollama run qwen2.5:3b < prompt_rapikan_vendor.txt > padanan.csv
Input: vendor_oktober.csv (412 baris, 37 variasi nama)
Output: 9 nama baku, 3 ditandai PERLU_CEK
Cloud egress: 0 byte 🌱
```

## Template Prompt Siap Pakai: Perapi Kolom Sheet: Variasi Nama Jadi Satu Nama Baku
> Kolom yang diisi banyak orang (nama vendor, divisi, kota, produk) sering punya banyak variasi penulisan untuk hal yang sama, sehingga pivot table dan rekap jadi salah. Prompt ini mengelompokkan variasi tersebut menjadi nama baku dan menghasilkan tabel padanan yang bisa diperiksa manusia sebelum dipakai.

### System Instruction
```text
Kamu adalah asisten data yang teliti dan jujur. Tugasmu mengelompokkan variasi penulisan yang merujuk ke entitas yang sama menjadi satu nama baku. Aturan: (1) Jangan menebak kalau ragu. Tandai dengan status PERLU_CEK dan jelaskan alasannya singkat. (2) Jangan menghapus atau menggabungkan entri yang kemungkinan entitas berbeda, misalnya cabang berbeda atau nama mirip tapi beda perusahaan. (3) Pertahankan setiap nilai asli persis seperti input, termasuk salah ketiknya. (4) Keluarkan hasil hanya dalam format CSV yang diminta, tanpa teks tambahan. Keputusan akhir ada di tangan pengguna.
```

### User Prompt Template (1-Tap Copy)
```text
Berikut isi satu kolom dari spreadsheet-ku. Kolom ini berisi: [JENIS_DATA].

Aturan penamaan baku yang aku mau: [ATURAN_PENAMAAN]

Data (satu nilai per baris):
[DATA_KOLOM]

Buatkan tabel padanan dalam format CSV dengan kolom:
nilai_asli,nama_baku,status,alasan

- status diisi YAKIN atau PERLU_CEK
- alasan diisi singkat, maksimal 10 kata, wajib untuk PERLU_CEK
- setiap nilai asli yang unik muncul tepat satu kali

Di baris paling akhir, tambahkan ringkasan: jumlah nilai asli unik, jumlah nama baku, jumlah PERLU_CEK.
```

💡 **Tips Praktis:** Mulai dari kolom kecil dulu, cukup 30 sampai 50 baris, supaya kamu bisa cek semua hasilnya dan belajar pola salah AI-nya. Perhatikan baris PERLU_CEK. 'PT Maju Jaya Abadi' bisa jadi perusahaan yang berbeda, dan cuma kamu yang tahu konteksnya. Simpan tabel padanan yang sudah kamu periksa sebagai sheet terpisah, jadi bulan depan tinggal VLOOKUP tanpa perlu mengulang dari nol 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
