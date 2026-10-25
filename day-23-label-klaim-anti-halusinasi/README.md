# Modul 23: Boleh Kok AI Bilang 'Aku Tidak Tahu': Beri Label Setiap Klaim Sebelum Kamu Percaya Jawabannya 🌱
> **Fokus Praktik:** Edukasi Umum & Anti-Halusinasi
## Mengapa Modul Ini Penting?
Komunitas masih bingung mau mulai belajar AI dari mana (29 pertanyaan, 36 sinyal bingung), dan audiens makin sering bertanya apakah sebuah konten dibuat AI. Karena itu, kebiasaan pertama yang paling aman untuk orang non-teknis bukan prompt yang canggih. Yang paling aman adalah cara sederhana membedakan klaim yang benar-benar ada di sumber, klaim yang cuma dugaan, dan hal yang memang tidak diketahui AI.
## Alur Langkah Praktis
- 1. LABEL: Minta AI memberi tanda [ADA DI SUMBER] / [DUGAAN] / [TIDAK TAHU] beserta kutipan persisnya
- 2. PILIH: Tandai 3 klaim yang paling berisiko kalau keliru (angka, nama, tanggal)
- 3. COCOKKAN: Cari kutipannya di dokumen asli (Ctrl+F atau grep). Kalau tidak ketemu, turunkan jadi [DUGAAN]
## Contoh Perintah / Spesimen Lokal
```bash
$ pdftotext laporan-2025.pdf sumber.txt
$ ollama run llama3.2 "$(cat label-klaim.txt sumber.txt)" > klaim.md
$ grep -n "18,4%" sumber.txt
212: ...pertumbuhan mencapai 18,4% pada kuartal III...
$ grep -c "\[TIDAK TAHU\]" klaim.md
2  (AI jujur di 2 klaim)
Cloud egress: 0 byte 🌱
```

## Template Prompt Siap Pakai: Label Klaim Anti-Halusinasi: Pisahkan Fakta, Dugaan, dan 'Aku Tidak Tahu'
> Jawaban AI sering mencampur fakta dari dokumen dengan karangan yang terdengar meyakinkan, sehingga pengguna non-teknis sulit tahu mana yang perlu dicek. Prompt ini memaksa setiap klaim diberi label dan kutipan persis dari sumber, mengizinkan AI menjawab 'aku tidak tahu', lalu mengurutkan 3 klaim paling berisiko supaya verifikasinya cukup 10 menit.

### System Instruction
```text
Kamu adalah asisten verifikasi yang jujur dan teliti. Kamu HANYA boleh memakai informasi dari teks SUMBER yang diberikan pengguna. Untuk setiap klaim, beri satu label: [ADA DI SUMBER] jika ada kalimat di sumber yang mendukungnya, dan tulis kutipan persisnya kata demi kata; [DUGAAN] jika klaim itu kesimpulanmu sendiri yang tidak tertulis langsung, dan jelaskan alasannya dalam satu kalimat; [TIDAK TAHU] jika sumber tidak memuat informasinya. Jangan pernah mengarang kutipan, angka, nama, tanggal, atau nomor halaman. Lebih baik menjawab [TIDAK TAHU] daripada menebak. Gunakan bahasa Indonesia yang sederhana dan membumi.
```

### User Prompt Template (1-Tap Copy)
```text
Aku butuh jawaban yang bisa aku pertanggungjawabkan.

PERTANYAAN:
[PERTANYAAN]

SUMBER (satu-satunya rujukan yang boleh dipakai):
"""
[SUMBER_DATA]
"""

Konteks penggunaan: [KONTEKS_PENGGUNAAN]

Tolong kerjakan dengan format ini:
1. JAWABAN SINGKAT (maksimal 5 kalimat).
2. TABEL KLAIM dengan kolom: No | Klaim | Label ([ADA DI SUMBER]/[DUGAAN]/[TIDAK TAHU]) | Kutipan persis dari sumber atau alasan.
3. 3 KLAIM PALING BERISIKO: urutkan klaim yang paling merugikan kalau ternyata salah (angka, nama, tanggal, kewajiban hukum), beserta kata kunci yang bisa aku cari dengan Ctrl+F di dokumen asli.
4. CELAH INFORMASI: sebutkan apa yang tidak bisa dijawab dari sumber ini dan sumber tambahan apa yang perlu aku cari.

Kalau sumber tidak cukup untuk menjawab, katakan dengan jujur. Itu jauh lebih membantu daripada jawaban yang terdengar yakin.
```

💡 **Tips Praktis:** Perhatikan kata 'penyebab utama' di contoh tadi. Sumbernya hanya bilang kenaikan terjadi SETELAH peluncuran QRIS, bukan KARENA QRIS. AI yang jujur akan memberi label [DUGAAN] di situ. Kalau AI-mu malah menandainya [ADA DI SUMBER], itu sinyal untuk mengecek ulang. Kebiasaan kecil membedakan 'setelah' dan 'karena' ini yang menjaga laporan kita tetap bisa dipercaya 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
