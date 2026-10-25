# Modul 28: Senin Kewalahan? Ubah Tumpukan To-Do Minggu Lalu di Sheet Jadi 3 Prioritas Minggu Ini 🌱
> **Fokus Praktik:** Publik & Semua Profesional (Kickoff Mingguan)
## Mengapa Modul Ini Penting?
Hari ke-28 adalah kickoff mingguan, momen di mana profesional paling sering merasa kewalahan oleh sisa pekerjaan minggu lalu. Materi ini menyambung ajakan 'satu tugas capek, satu sheet' (Hari 26) jadi ritual mingguan konkret: AI membantu memilah, manusia tetap memutuskan, sejalan dengan prinsip jujur soal peran mesin dari Hari 27.
## Alur Langkah Praktis
- 1. Kumpulkan: salin semua sisa tugas ke 1 kolom Sheet
- 2. Pilah: AI kelompokkan jadi Lanjut / Delegasi / Lepas + alasannya
- 3. Putuskan: kamu pilih maks. 3 prioritas, sisanya dijadwal ulang
## Contoh Perintah / Spesimen Lokal
```bash
$ wc -l todo-minggu-lalu.csv  → 23
$ ollama run qwen2.5:7b "Kelompokkan: Lanjut/Delegasi/Lepas" < todo-minggu-lalu.csv
Output: triase.csv (Lanjut 9 · Delegasi 6 · Lepas 8)
Egress cloud: 0 byte 🌱
```

## Template Prompt Siap Pakai: Triase Kickoff Mingguan: Dari Tumpukan To-Do ke 3 Prioritas
> Membantu profesional yang kewalahan oleh sisa tugas minggu lalu untuk memilah daftar panjang menjadi kategori Lanjut, Delegasi, dan Lepas, lalu mengusulkan kandidat prioritas sesuai kapasitas nyata, tanpa mengambil alih keputusan akhir.

### System Instruction
```text
Kamu adalah asisten perencanaan mingguan yang membumi dan realistis. Tugasmu memilah, bukan memutuskan. Selalu tampilkan alasan singkat untuk setiap pengelompokan agar pengguna bisa mengoreksi. Jangan pernah mengusulkan lebih dari 3 prioritas. Jika total estimasi melebihi kapasitas, katakan dengan jujur dan sarankan apa yang dilepas. Hindari bahasa hype atau menghakimi; validasi bahwa sisa tugas adalah hal wajar. Gunakan bahasa Indonesia santai dengan sapaan 'kamu'.
```

### User Prompt Template (1-Tap Copy)
```text
Aku bekerja sebagai [PERAN]. Minggu ini kapasitas efektifku sekitar [KAPASITAS_JAM] jam untuk pekerjaan fokus.

Berikut sisa tugas dari minggu lalu (satu baris per tugas):
[DAFTAR_TUGAS]

Tolong lakukan ini:
1. Kelompokkan setiap tugas ke dalam salah satu kategori: LANJUT (penting & harus aku sendiri), DELEGASI (bisa dikerjakan orang lain), atau LEPAS (sudah tidak relevan / dampaknya kecil). Beri alasan 1 kalimat per tugas.
2. Beri estimasi kasar jam untuk tugas di kategori LANJUT.
3. Usulkan maksimal 3 KANDIDAT prioritas yang muat dalam kapasitasku, beserta alasannya.
4. Tulis 1 pertanyaan klarifikasi jika ada tugas yang ambigu.

Format output sebagai tabel dengan kolom: Tugas | Kategori | Alasan | Estimasi Jam, supaya bisa langsung aku tempel ke Sheet. Ingat: keputusan akhir tetap di aku.
```

💡 **Tips Praktis:** Pakai prompt yang sama setiap Senin dan simpan hasilnya di tab Sheet baru per minggu. Setelah 4 minggu, kamu akan lihat pola tugas yang selalu 'terbawa', dan biasanya itu kandidat terbaik untuk didelegasikan atau dilepas selamanya. 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
