# Sortir Otomatis Folder Downloads Berdasarkan Isi Dokumen (Day 13)

Folder `Downloads` di laptop sering kali menumpuk ratusan file dengan nama acak seperti `Scan_00129.pdf`, `Invoice_baru(1).pdf`, atau `Unduhan_final.docx`.

Skrip Python ini:
1. Membaca 50 kata pertama isi file dokumen secara lokal (tanpa mengirim isi file ke internet).
2. Mendeteksi apakah file tersebut merupakan Faktur Pajak, Invoice tagihan, Proposal kerjasama, atau Laporan keuangan.
3. Memindahkannya secara otomatis ke subfolder arsip yang rapi.

## Cara Menggunakan:
```bash
# 1. Mode Simulasi (Dry-Run aman, tidak memindahkan file)
python sort_downloads.py

# 2. Mode Eksekusi Nyata
python sort_downloads.py --apply

# 3. Menjalankan di folder kustom tertentu
python sort_downloads.py /path/ke/folder/kamu --apply
```
