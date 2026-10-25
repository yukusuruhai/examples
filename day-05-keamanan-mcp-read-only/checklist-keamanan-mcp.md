# 5 Checklist Keamanan MCP di Laptop Kerja 🌱

1. **Beri Izin Satu Folder Khusus (`Scoped Directory`)**: Jangan pernah arahkan MCP ke root `/home/user`. Buat satu folder khusus seperti `~/ruang-baca-ai`.
2. **Utamakan Mode Baca Saja (`Read-Only`)**: Untuk analisis laporan dan spreadsheet, matikan tool `write_file` atau `delete_file`.
3. **Pisahkan File Kredensial (`.env`)**: Pastikan file password, token API, atau rekening pribadi tidak berada di dalam folder yang diakses MCP.
4. **Gunakan Model Lokal untuk Data Sensitif**: Jalankan Ollama di laptop sendiri agar 0 byte data keluar ke jaringan internet.
5. **Simpan Log Panggilan Tool**: Catat setiap kali AI membaca berkas sehingga kita selalu tahu berkas mana saja yang disentuh 🌱
