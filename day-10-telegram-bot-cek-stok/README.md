# Pangkas 80% Waktu Cek Stok: Google Sheets + Bot Telegram Toko (Day 10)

Kelelahan admin toko online biasanya bukan karena melayani pembeli serius, melainkan menjawab pertanyaan berulang: *"Kak warna hitam ready?", "Kak size L ada?"*.

Dengan arsitektur Rp0 ini:
1. Data inventori diperbarui staf/admin dari HP via **Google Sheets**.
2. **Google Apps Script** (`Code.gs`) membuka endpoint API instan tanpa server berbayar.
3. **Bot Telegram** (`telegram_stock_bot.py`) membaca stok secara real-time dan langsung menjawab pelanggan dalam <1 detik.

## Langkah Cepat Pemasangan:
1. Buat Google Sheets dengan kolom: `SKU`, `Nama Produk`, `Stok`, `Harga Satuan`.
2. Buka menu **Extensions** ➔ **Apps Script**, salin `Code.gs`.
3. Klik **Deploy** ➔ **New Deployment** (Web App, Anyone access).
4. Masukkan URL hasil deploy ke `SHEETS_API_URL` di `telegram_stock_bot.py`.
5. Jalankan `python telegram_stock_bot.py`!
