# Modul 20: Yang Rusak Juga Boleh Dibagi: Retro Mingguan Alur Sheet + MCP Lokal dari Log Kita Sendiri 🌱
> **Fokus Praktik:** Evaluasi & Belajar Bersama Komunitas
## Mengapa Modul Ini Penting?
Selama empat hari kita sudah merangkai jejak jawaban, MCP read-only, dan laporan pagi dari sheet, jadi wajar kalau sudah ada yang gagal di lapangan. Hari ini kita berhenti menambah fitur dan membaca log lokal bareng-bareng, supaya kegagalan jadi bahan belajar dan grup Telegram jadi tempat aman buat cerita, bukan buat dihakimi.
## Alur Langkah Praktis
- 1. Hitung: Berapa panggilan yang gagal dari total minggu ini?
- 2. Kelompokkan: Error apa yang paling sering muncul?
- 3. Pilih satu: Satu perbaikan kecil + satu cerita untuk dibagi ke komunitas
## Contoh Perintah / Spesimen Lokal
```bash
$ wc -l logs/mcp-calls.jsonl
214 panggilan tool minggu ini
$ jq -r 'select(.ok==false) | .error' logs/mcp-calls.jsonl | sort | uniq -c
5 DATE_FORMAT_MISMATCH · 3 TOOL_TIMEOUT · 1 FILE_LOCKED
Tingkat gagal: 9/214 (4,2%) · Cloud egress: 0 byte 🌱
```

## Template Prompt Siap Pakai: Retro Mingguan Alur Otomasi dari Log Lokal
> Banyak orang yang sudah merangkai sheet, MCP, dan model lokal berhenti di tengah jalan karena error kecil yang berulang tidak pernah dirangkum. Prompt ini mengubah ringkasan log mingguan menjadi retro yang jujur, tenang, dan punya satu perbaikan prioritas yang bisa dikerjakan dalam 30 menit.

### System Instruction
```text
Kamu adalah fasilitator retro alur otomasi yang membumi dan empatik. Gunakan 'aku' dan 'kita', sapa pengguna dengan 'kamu'. Tugasmu membaca ringkasan log yang diberikan dan HANYA menyimpulkan dari data itu. Jangan mengarang angka, jangan menebak penyebab tanpa menandainya sebagai dugaan. Validasi kelelahan pengguna tanpa berlebihan, hindari hype, dan selalu tutup dengan tepat SATU perbaikan prioritas yang realistis. Jika data tidak cukup untuk menyimpulkan sesuatu, katakan terus terang dan sarankan log tambahan apa yang perlu dicatat.
```

### User Prompt Template (1-Tap Copy)
```text
Aku ingin melakukan retro mingguan untuk alur otomasi [NAMA_ALUR].

Ringkasan log minggu ini (hasil perintah lokal):
[RINGKASAN_LOG]

Catatan pribadiku tentang minggu ini:
[CATATAN_PRIBADI]

Waktu yang aku punya untuk perbaikan minggu depan: [WAKTU_TERSEDIA]

Tolong susun retro dengan format berikut:
1. Gambaran Jujur: total panggilan, jumlah gagal, dan persentase gagal (hitung hanya dari data di atas).
2. Pola Error: kelompokkan error dari yang paling sering, lengkap dengan dugaan penyebab (tandai jelas mana fakta dan mana dugaan).
3. Yang Sudah Berjalan Baik: minimal satu hal yang layak dipertahankan.
4. Satu Perbaikan Prioritas: satu langkah konkret yang muat dalam [WAKTU_TERSEDIA], beserta cara mengecek bahwa perbaikannya berhasil di log minggu depan.
5. Cerita untuk Komunitas: draf 3 kalimat yang bisa aku bagikan ke grup belajar, berisi angka, pola, dan perbaikan yang aku pilih.
```

💡 **Tips Praktis:** Tempelkan angka mentah dari terminal, jangan versi yang sudah kamu rapikan di kepala. Retro yang jujur lahir dari data yang apa adanya. Kalau minggu ini error-nya nol, catat juga itu, karena minggu yang tenang pun layak dirayakan dan dibagi ke komunitas 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
