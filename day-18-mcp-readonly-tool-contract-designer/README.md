# Modul 18: MCP Server yang Bikin Tenang: Kontrak Tool Ketat, Akses Read-Only, dan Tes Lokal Sebelum Agen Menyentuh Data 🌱
> **Fokus Praktik:** Track 3: Software Engineer
## Mengapa Modul Ini Penting?
Hari 17 sudah menyambungkan file stok ke AI lewat MCP lokal dari sisi pengguna. Hari ini kita lihat sisi engineer: membuat server itu aman dipakai di produksi dengan schema input ketat, batas akses read-only, dan tes otomatis. Pilihan ini sejalan dengan tren MCP Production Guide 2026 dan tidak mengulang topik jejak jawaban di Hari 16.
## Alur Langkah Praktis
- 1. Kontrak: tulis schema zod per tool (enum, max, tanpa any)
- 2. Batas: daftarkan tool read-only saja + guard path ke satu folder
- 3. Bukti: tes vitest untuk input jahat, lalu cek lewat MCP Inspector
## Contoh Perintah / Spesimen Lokal
```bash
$ pnpm add @modelcontextprotocol/sdk zod
inputSchema: { sheet: z.enum(['stok','harga']), limit: z.number().int().max(200) }
guard: path.resolve(DATA_DIR, file).startsWith(DATA_DIR)
$ pnpm vitest run tests/mcp-sheets.test.ts
✓ menolak path '../secret.env'  ✓ menolak limit 9999  ✓ membaca 50 baris
$ npx @modelcontextprotocol/inspector node dist/server.js
Egress: 0 byte, semua lokal 🌱
```

## Template Prompt Siap Pakai: Perancang Kontrak Tool MCP Read-Only
> Engineer sering membuat MCP server terburu-buru dengan input tool yang tidak divalidasi, akses file yang terlalu lebar, dan tanpa tes. Prompt ini menghasilkan kontrak tool yang ketat (schema zod), guard akses read-only, dan daftar kasus tes vitest untuk input jahat. Hasilnya, server bisa diverifikasi secara lokal sebelum dipakai agen.

### System Instruction
```text
Kamu adalah senior TypeScript engineer yang membumi dan teliti, spesialis Model Context Protocol (MCP). Prioritasmu: keamanan dulu, kesederhanaan kedua, fitur ketiga. Selalu terapkan prinsip least privilege: daftarkan hanya operasi baca kecuali diminta eksplisit. Jangan pernah memakai z.any(), eval, Function constructor, atau eksekusi kode dinamis. Setiap path file wajib di-resolve dan dicek agar tetap berada di dalam direktori data yang diizinkan. Gunakan transport stdio dan jangan menambahkan panggilan jaringan keluar. Tulis penjelasan singkat dalam bahasa Indonesia yang santai dengan 'aku' dan 'kita', tanpa hype. Jika informasi kurang, tuliskan asumsimu dengan jelas daripada mengarang.
```

### User Prompt Template (1-Tap Copy)
```text
Aku sedang membangun MCP server lokal (TypeScript, @modelcontextprotocol/sdk, zod, vitest).

Sumber data: [SUMBER_DATA]
Kolom/struktur data: [STRUKTUR_DATA]
Pertanyaan yang perlu dijawab agen: [KEBUTUHAN_AGEN]
Direktori data yang diizinkan: [DIREKTORI_DATA]

Tolong buatkan:
1. Daftar tool minimal (read-only) beserta alasan singkat kenapa tiap tool dibutuhkan.
2. Schema zod untuk input setiap tool: pakai enum, batas angka (min/max), dan panjang string. Dilarang memakai any.
3. Fungsi guard path yang menolak traversal (../), symlink keluar folder, dan ekstensi di luar whitelist.
4. Kerangka handler tool yang mengembalikan data terbatas (dengan limit) dan pesan error yang jelas.
5. Minimal 6 kasus tes vitest: 3 input valid, 3 input jahat (path traversal, limit berlebih, nama sheet tidak dikenal).
6. Perintah verifikasi lokal (vitest + MCP Inspector) dan checklist singkat sebelum server dipakai agen.

Pisahkan tiap bagian dengan heading dan code block. Jaga setiap file tetap kecil dan punya satu tanggung jawab.
```

💡 **Tips Praktis:** Tulis tes untuk input jahat lebih dulu, sebelum handler-nya selesai. Kalau tes path traversal sudah merah lalu berubah hijau, kita tahu batas server itu benar-benar bekerja, bukan cuma kita kira bekerja. Mulai dari satu tool dulu dan biarkan tumbuh pelan-pelan. 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
