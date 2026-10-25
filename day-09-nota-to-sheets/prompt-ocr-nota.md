# 🧾 Template Prompt: Ekstraksi Nota & Kwitansi Belanja ke JSON (Day 9)

## Prompt Vision AI (Untuk Diunggah Bersama Foto Nota ke AI)
```text
Lihat foto struk/nota/kwitansi pembelian yang saya lampirkan.
Ekstraksi data transaksi ini menjadi format JSON murni tanpa pembuka/penutup markdown (```json).

Format JSON yang wajib diikuti:
{
  "tanggal": "YYYY-MM-DD",
  "nama_toko": "Nama Toko / Vendor",
  "kategori": "Konsumsi | Operasional | Transportasi | Logistik | Lainnya",
  "daftar_barang": [
    {
      "nama": "Nama Item",
      "qty": 1,
      "harga_satuan": 0,
      "subtotal": 0
    }
  ],
  "pajak": 0,
  "total_akhir": 0,
  "metode_bayar": "CASH | QRIS | DEBIT | KREDIT | TRANSFER",
  "nomor_struk": "Nomor Struk atau null jika tidak terbaca",
  "keterangan": "Catatan ringkas"
}
```

## Pro-Tip dari Kirana:
- AI vision modern (Gemini 1.5 Flash/Pro, GPT-4o, Claude 3.5 Sonnet) sangat akurat membaca struk yang agak buram atau sedikit kusut.
- Kirim JSON hasil ekstraksi ini ke webhook Google Apps Script (`Code.gs`) agar transaksi langsung masuk ke baris Google Sheets secara otomatis.
