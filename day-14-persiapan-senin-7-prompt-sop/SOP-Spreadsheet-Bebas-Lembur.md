# 📊 SOP Standar Operasional: Spreadsheet Bebas Lembur (Day 14)

**Tujuan:** Menghilangkan kebiasaan lembur akibat rumus Excel/Google Sheets yang rusak, data input berantakan, dan rekonsiliasi manual setiap akhir pekan.

---

## 1. Aturan Emas Struktur Tabel (One-Table Principle)
1. **Satu Baris = Satu Entitas Transaksi:** Jangan pernah menggabungkan sel (merge cells) di dalam area data mentah. Merge cells hanya diperbolehkan di laporan cetak akhir.
2. **Kunci Tipe Data per Kolom:** Satu kolom hanya boleh memuat satu tipe data (misal: Kolom Tanggal hanya berisi tanggal valid YYYY-MM-DD, jangan dicampur catatan teks seperti "belum lunas").
3. **Gunakan Validasi Data (Dropdown):** Kolom status, metode pembayaran, dan kategori wajib menggunakan *Data Validation List* untuk mencegah salah ketik (*human typo*).

---

## 2. Alur Rutinitas Mingguan (15 Menit di Jumat Sore)
- **Langkah 1 (Audit Data Kosong):** Jalankan filter pada kolom primer untuk mendeteksi baris tanpa ID atau nominal Rp0.
- **Langkah 2 (Snapshot Backup):** Duplikasi tab data aktif menjadi tab arsip mingguan dengan format nama `Data_YYYYWW` (misal: `Data_2026W42`).
- **Langkah 3 (Kunci Rumus Summary):** Gunakan formula dinamis `QUERY` atau `SUMIFS` pada tab dashboard terpisah, bukan menghitung manual dengan kalkulator HP.

---

## 3. Checklist Kesiapan Senin Pagi
- [ ] Semua transaksi Jumat telah terinput.
- [ ] Tab Dashboard Laporan menampilkan angka saldo yang cocok dengan rekening bank/kas fisik.
- [ ] Status pekerjaan minggu depan sudah memiliki PIC penanggung jawab.
