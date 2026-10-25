# Modul 26: Bukan Orang IT dan Bingung Mulai dari Mana? Satu Tugas Capek, Satu Sheet Catatan, 7 Hari Belajar AI dengan Rp0 🌱
> **Fokus Praktik:** Arsitektur Lokal & Efisiensi Kerja Rp0
## Mengapa Modul Ini Penting?
Ada 29 pertanyaan dan 36 sinyal bingung di komunitas soal cara memulai AI untuk non-teknis. Jadi setelah lima hari materi verifikasi yang cukup teknis, hari ini kita turunkan ritmenya ke satu kebiasaan kecil yang bisa diukur. Sekalian kita jawab komentar 'ini AI generated ya?' dengan contoh nyata cara pakai AI secara jujur dan tercatat.
## Alur Langkah Praktis
- 1. Pilih: 1 tugas melelahkan (cek sensitif atau tidak)
- 2. Coba: lokal untuk data pribadi, gratis untuk data umum
- 3. Catat: tugas | prompt | hasil | menit hemat | perlu koreksi?
## Contoh Perintah / Spesimen Lokal
```bash
$ ollama pull llama3.2:3b
$ ollama run llama3.2:3b "Ringkas jadi 5 poin:" < ~/belajar-ai/notulen-senin.txt > ~/belajar-ai/hasil-1.md
Tersimpan: ~/belajar-ai/hasil-1.md (2.1 KB)
Cloud egress: 0 byte 🌱
```

## Template Prompt Siap Pakai: Pemandu 7 Hari Pertama Belajar AI untuk Non-Teknis
> Pekerja non-teknis sering bingung mau mulai belajar AI dari mana, lalu berhenti karena kebanyakan pilihan. Prompt ini mengubah satu tugas yang melelahkan menjadi rencana latihan 7 hari yang terukur. Isinya klasifikasi sensitivitas data (lokal atau cloud gratis), prompt latihan harian, dan format log sheet untuk mencatat hasil dengan jujur.

### System Instruction
```text
Kamu adalah mentor belajar AI yang membumi dan sabar untuk pekerja non-teknis. Gunakan kata 'aku' dan 'kamu', bahasa Indonesia sehari-hari yang sopan, tanpa jargon. Kalau istilah teknis tidak bisa dihindari, jelaskan dalam satu kalimat sederhana. Jangan menjanjikan hasil berlebihan dan jangan memakai nada menakut-nakuti. Selalu periksa apakah data dalam tugas itu sensitif (data pribadi, keuangan, pelanggan, atau internal perusahaan). Kalau sensitif, sarankan pemrosesan lokal di laptop. Kalau tidak sensitif, layanan AI gratis boleh dipakai. Kalau informasi dari pengguna kurang, katakan dengan jujur apa yang belum kamu ketahui, jangan mengarang.
```

### User Prompt Template (1-Tap Copy)
```text
Aku bekerja sebagai [PEKERJAAN]. Tugas yang paling menguras tenagaku setiap minggu adalah: [TUGAS_MELELAHKAN]. Alat yang aku punya saat ini: [ALAT_TERSEDIA]. Waktu luang untuk belajar per hari: [WAKTU_HARIAN].

Tolong bantu aku dengan langkah berikut:
1. Klasifikasikan sensitivitas data dalam tugas ini (SENSITIF / UMUM) beserta alasan singkat, lalu rekomendasikan jalurnya: model lokal di laptop atau layanan AI gratis.
2. Pecah tugas ini menjadi 7 latihan harian kecil (Hari 1 sampai Hari 7) yang makin meningkat, masing-masing selesai dalam [WAKTU_HARIAN].
3. Untuk setiap hari, tuliskan satu prompt latihan siap salin dalam bahasa Indonesia.
4. Buatkan header tabel sheet untuk log belajar dengan kolom: Hari | Tugas | Prompt Dipakai | Jalur (Lokal/Cloud) | Hasil Singkat | Menit Dihemat | Perlu Koreksi? (Ya/Tidak) | Catatan.
5. Tutup dengan 3 tanda jujur bahwa AI BELUM cocok untuk tugas ini, supaya aku tahu kapan harus tetap mengerjakannya secara manual.
```

💡 **Tips Praktis:** Jangan ukur kemajuanmu dari banyaknya alat yang sudah kamu coba. Ukur dari kolom 'Menit Dihemat' dan 'Perlu Koreksi?' di sheet-mu. Kalau di hari ketujuh ternyata AI cuma membantu di 3 dari 7 latihan, itu tetap temuan berharga, karena sekarang kamu tahu persis di mana AI berguna untuk pekerjaanmu. 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
