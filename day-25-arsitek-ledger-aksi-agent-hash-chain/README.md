# Modul 25: Agent-mu Kemarin Ngapain Aja? Catat Setiap Aksinya di Log Berantai Hash yang Bisa Kamu Verifikasi Sendiri 🌱
> **Fokus Praktik:** Track 3: Software Engineer
## Mengapa Modul Ini Penting?
Tren 'hash-chained ledger untuk penalaran AI' dan komentar audiens yang meragukan konten AI sama-sama menunjukkan satu kebutuhan: jejak kerja AI yang bisa dibuktikan, bukan sekadar dipercaya. Setelah Hari 23 membahas label klaim di sisi jawaban, hari ini kita turun ke sisi engineer: membuat catatan aksi agent yang tidak bisa diubah diam-diam, cukup dengan file lokal dan sha256.
## Alur Langkah Praktis
- 1. Bungkus pemanggilan tool: catat {seq, waktu, tool, argumen ringkas, hasil ringkas}
- 2. Rantai: hash = sha256(prev + JSON baris), lalu append ke agent-ledger.jsonl
- 3. Verifikasi: jalankan verify-ledger sebelum review, dan simpan hash terakhir di tempat terpisah
## Contoh Perintah / Spesimen Lokal
```bash
$ tail -n 1 agent-ledger.jsonl
{"seq":42,"tool":"write_file","path":"src/report.ts","prev":"9f2c…e1","hash":"a71e…3b"}
$ node verify-ledger.mjs agent-ledger.jsonl
42/42 baris valid · rantai utuh
$ sed -i 's/report.ts/rahasia.ts/' agent-ledger.jsonl && node verify-ledger.mjs agent-ledger.jsonl
RANTAI PUTUS di seq 42: hash tidak cocok
Egress cloud: 0 byte 🌱
```

## Template Prompt Siap Pakai: Arsitek Ledger Aksi Agent: Log Berantai Hash yang Bisa Diverifikasi Lokal
> Engineer yang menjalankan agent AI sering tidak bisa membuktikan aksi apa saja yang dilakukan agent, dalam urutan apa, dan apakah log-nya pernah diubah. Prompt ini merancang skema ledger JSONL berantai hash, kode pembungkus pemanggilan tool, dan skrip verifikasi yang berjalan sepenuhnya di mesin lokal tanpa dependensi cloud.

### System Instruction
```text
Kamu adalah senior software engineer yang membumi dan teliti, spesialis observability dan audit trail untuk sistem agent AI. Kamu merancang solusi paling sederhana yang benar: file JSONL append-only, hash SHA-256 dari library standar bahasa yang diminta, tanpa database atau layanan eksternal kecuali diminta. Kamu dilarang memakai eval, new Function, exec dinamis, atau deserialisasi tidak aman. Kamu wajib menyamarkan argumen sensitif (token, password, isi .env) sebelum dicatat. Kamu jujur tentang batasan: hash chain mendeteksi perubahan, tetapi tidak mencegah penghapusan seluruh file, sehingga kamu selalu menyarankan penyimpanan hash terakhir (anchor) di tempat terpisah. Jika informasi dari pengguna kurang, tuliskan asumsimu secara eksplisit, jangan mengarang detail stack.
```

### User Prompt Template (1-Tap Copy)
```text
Aku ingin memasang ledger aksi berantai hash untuk agent AI-ku.

Stack agent: [AGENT_STACK]
Bahasa untuk kode: [BAHASA_KODE]
Titik pemanggilan tool saat ini (tempel potongan kode): 
[POTONGAN_KODE_TOOL]
Data yang tidak boleh tercatat mentah: [DATA_SENSITIF]

Tolong hasilkan:
1. Skema satu baris ledger (field, tipe, contoh), termasuk seq, timestamp ISO, tool, argumen ringkas, hasil ringkas, prev, hash.
2. Aturan kanonikalisasi JSON supaya hash konsisten (urutan key, encoding).
3. Fungsi pembungkus yang mencatat setiap pemanggilan tool secara append-only, beserta penyamaran data sensitif.
4. Skrip verifikasi CLI yang membaca ledger dari baris pertama dan melaporkan seq pertama yang rantainya putus, dengan exit code non-zero jika gagal.
5. Tiga unit test: rantai utuh, satu baris diubah, satu baris dihapus.
6. Daftar batasan jujur dan cara menyimpan anchor hash terakhir.

Jaga setiap file di bawah 300 baris dan pisahkan tanggung jawab (penulis ledger, verifikator, penyamar data).
```

💡 **Tips Praktis:** Mulai dari satu agent kecil dan satu tool saja dulu, misalnya write_file. Setelah ledger-nya jalan, sengaja ubah satu baris dengan tanganmu sendiri lalu jalankan verifikatornya. Melihat rantainya putus di depan mata bikin kita benar-benar paham cara kerjanya. Simpan juga hash terakhir di luar folder ledger, misalnya di commit message git, supaya penghapusan seluruh file pun tetap ketahuan 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
