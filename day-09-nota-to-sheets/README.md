# Ubah Foto Nota & Kwitansi Jadi Laporan Kas Google Sheets (Day 9)

Otomasi pencatatan pembukuan dan kas operasional langsung dari foto struk belanja menggunakan AI Vision dan Google Sheets.

## Komponen:
1. `prompt-ocr-nota.md`: Prompt instruksi untuk AI Vision membaca foto struk.
2. `Code.gs`: Kode Google Apps Script webhook yang otomatis menambahkan baris baru ke tabel Google Sheets Anda.

## Cara Pemasangan (5 Menit):
1. Buka Google Sheets baru.
2. Klik menu **Extensions** (Ekstensi) ➔ **Apps Script**.
3. Salin isi `Code.gs` ke editor, lalu klik simpan (Save).
4. Klik **Deploy** ➔ **New deployment** (Penerapan baru).
5. Pilih jenis **Web app**:
   - Execute as: *Me (email Anda)*
   - Who has access: *Anyone* (Siapa saja)
6. Salin URL Web App yang dihasilkan.
7. Saat Anda atau bot AI mengirim JSON hasil pembacaan nota ke URL tersebut (via HTTP POST), data transaksi otomatis tercatat rapi di Google Sheets tanpa koding server sendiri!
