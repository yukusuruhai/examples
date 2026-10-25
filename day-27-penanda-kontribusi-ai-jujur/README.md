# Modul 27: "Ini Konten AI Ya?" Iya, Dibantu AI. Begini Cara Kita Jujur soal Mana Kerja Mesin dan Mana Keputusan Manusia 🌱
> **Fokus Praktik:** Evaluasi & Belajar Bersama Komunitas
## Mengapa Modul Ini Penting?
Ada 6 komentar di media sosial yang bertanya apakah konten ini buatan AI, dan banyak pemula masih takut dicap "curang" kalau memakai AI. Materi hari ini menjawab pertanyaan itu secara terbuka, lalu mengajarkan satu kebiasaan kecil: mencatat bagian AI dan bagian manusia di sheet lokal, supaya rasa aman dan kepercayaan tumbuh bareng-bareng.
## Alur Langkah Praktis
- 1. Kerja: biarkan AI bantu draf, kamu cek fakta & nada
- 2. Catat: isi satu baris di log-jujur.csv (2 menit)
- 3. Ungkap: tulis satu kalimat jujur, misalnya 'draf dibantu AI, dicek oleh aku'
## Contoh Perintah / Spesimen Lokal
```bash
$ echo 'tanggal,pekerjaan,bagian_ai,bagian_aku' > log-jujur.csv
$ echo '2026-11-07,caption IG,draf awal,fakta+edit+terbit' >> log-jujur.csv
$ column -s, -t log-jujur.csv
Lokasi: disk lokal | Cloud egress: 0 byte 🌱
```

## Template Prompt Siap Pakai: Penanda Kontribusi AI: Catatan Jujur Mana Kerja Mesin, Mana Keputusan Manusia
> Banyak pekerja memakai AI tapi bingung atau takut mengungkapkannya, sementara pembaca dan atasan makin sering bertanya apakah suatu hasil kerja dibuat AI. Prompt ini mengubah catatan proses kerjamu menjadi satu baris log kontribusi yang siap ditempel ke sheet, ditambah kalimat pengungkapan singkat yang jujur dan tidak defensif.

### System Instruction
```text
Kamu adalah asisten pencatat transparansi kerja yang jujur dan membumi. Tugasmu memisahkan dengan tegas bagian pekerjaan yang dikerjakan AI dan bagian yang diputuskan atau diverifikasi manusia, hanya berdasarkan catatan proses yang diberikan. Jangan pernah melebih-lebihkan peran manusia atau mengecilkan peran AI. Jika informasi tidak cukup untuk menentukan siapa mengerjakan apa, tulis 'BELUM JELAS' dan ajukan satu pertanyaan klarifikasi. Gunakan bahasa Indonesia yang sederhana, hangat, dan tanpa jargon.
```

### User Prompt Template (1-Tap Copy)
```text
Aku baru menyelesaikan pekerjaan berikut dan ingin mencatat kontribusi AI secara jujur.

Jenis pekerjaan: [JENIS_PEKERJAAN]
Tanggal: [TANGGAL]

Catatan proses kerjaku (apa yang aku minta ke AI, apa yang aku ubah, apa yang aku cek):
[CATATAN_PROSES]

Audiens yang akan membaca hasilnya: [AUDIENS]

Tolong buatkan:
1. Satu baris CSV dengan format: tanggal,pekerjaan,bagian_ai,bagian_aku,status_verifikasi
2. Tabel singkat 2 kolom: 'Dikerjakan AI' dan 'Diputuskan/Dicek Manusia'
3. Satu kalimat pengungkapan (maksimal 25 kata) yang cocok untuk audiens di atas, jujur, tidak defensif, dan tidak berlebihan
4. Daftar bagian yang 'BELUM JELAS' beserta satu pertanyaan klarifikasi, jika ada
```

💡 **Tips Praktis:** Tulis catatan proses tepat setelah selesai kerja, jangan tunggu besok. Ingatan kita cepat kabur soal bagian mana yang diubah sendiri. Simpan hasil CSV-nya di laptopmu dan isi terus setiap hari. Setelah sebulan, kamu punya bukti nyata bahwa AI membantumu, tapi keputusan tetap di tanganmu 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
