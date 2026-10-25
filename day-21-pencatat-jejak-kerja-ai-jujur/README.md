# Modul 21: Iya, Ini Dibantu AI, dan Ini Catatannya: Memulai Kebiasaan Jejak Kerja AI yang Jujur untuk Siapa Pun 🌱
> **Fokus Praktik:** Publik & Semua Profesional (Kickoff Mingguan)
## Mengapa Modul Ini Penting?
Ada 6 komentar di media sosial yang bertanya "ini AI generated ya?". Ada juga 29 pertanyaan dari teman-teman non-teknis yang bingung harus mulai dari mana. Karena itu kickoff minggu ini mengajarkan satu kebiasaan paling dasar sebelum otomasi apa pun: mencatat jujur bagian mana yang dikerjakan AI dan bagian mana yang dikerjakan manusia, di file lokal milik sendiri.
## Alur Langkah Praktis
- 1. Kerjakan: pakai AI untuk draf, ringkasan, atau ide
- 2. Catat: tanggal | tugas | peran AI | suntinganmu
- 3. Ungkap: tulis label jujur saat membagikan hasil
## Contoh Perintah / Spesimen Lokal
```bash
$ echo "2026-11-01 | caption IG | AI: draf awal | aku: cek fakta & nada" >> ~/jejak-ai.log
$ tail -n 1 ~/jejak-ai.log
$ sha256sum ~/jejak-ai.log >> ~/jejak-ai.sha256
Egress cloud: 0 byte 🌱
```

## Template Prompt Siap Pakai: Pencatat Jejak Kerja AI & Label Keterbukaan
> Banyak profesional ragu atau defensif saat ditanya "ini pakai AI ya?" karena kontribusi manusianya tidak tercatat. Prompt ini mengubah cerita kerja yang berantakan menjadi satu baris log terstruktur dan satu label keterbukaan singkat yang jujur, siap dipakai di caption, laporan, atau email.

### System Instruction
```text
Kamu adalah asisten pencatat kerja yang jujur, ringkas, dan membumi. Tugasmu memisahkan dengan adil mana bagian yang dikerjakan AI dan mana yang dikerjakan manusia, tanpa melebih-lebihkan peran siapa pun. Jangan mengarang detail yang tidak disebutkan pengguna. Jika informasi kurang, tulis 'tidak disebutkan'. Gunakan bahasa Indonesia sehari-hari yang sopan, sapa pengguna dengan 'kamu', dan hindari istilah hype.
```

### User Prompt Template (1-Tap Copy)
```text
Bantu aku mencatat jejak kerja AI untuk tugas berikut.

Tanggal: [TANGGAL]
Tugas: [TUGAS]
Apa yang dikerjakan AI: [PERAN_AI]
Apa yang aku kerjakan/ubah sendiri: [SUNTINGAN_MANUSIA]
Tempat hasil ini dibagikan: [KANAL_PUBLIKASI]

Hasilkan tiga bagian:
1. LOG: tepat satu baris dengan format `TANGGAL | TUGAS | AI: ... | Manusia: ...` (maksimal 160 karakter).
2. LABEL: satu kalimat keterbukaan yang jujur dan hangat untuk [KANAL_PUBLIKASI] (maksimal 120 karakter).
3. CEK: daftar maksimal 3 hal yang sebaiknya aku verifikasi ulang sebelum dibagikan, berdasarkan peran AI di atas.
```

💡 **Tips Praktis:** Simpan baris LOG ke satu file lokal yang sama setiap hari, misalnya ~/jejak-ai.log. Setelah seminggu, baca ulang file itu. Kamu akan lihat sendiri seberapa besar peranmu yang selama ini nggak kelihatan, dan itu bekal paling tenang saat ada yang bertanya 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
