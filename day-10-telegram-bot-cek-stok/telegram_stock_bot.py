#!/usr/bin/env python3
"""
Bot Telegram Cek Stok Toko (Real-Time dari Google Sheets) (Day 10)
Menggunakan polling atau webhook ringan tanpa dependensi berlebih.
"""

import os
import sys
import json
import urllib.request
import urllib.parse

# Konfigurasi: isi token Telegram dan URL Web App Google Apps Script
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "BOT_TOKEN_DISINI")
SHEETS_API_URL = os.getenv("SHEETS_API_URL", "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec")

def query_stock_from_sheets(sku: str) -> dict:
    """Membaca data stok langsung dari Google Apps Script Web App."""
    if not SHEETS_API_URL or "YOUR_SCRIPT_ID" in SHEETS_API_URL:
        # Data demo jika URL belum dikonfigurasi
        demo_stock = {
            "KEMEJA-01": {"nama": "Kemeja Katun Polos Hitam", "stok": 15, "harga": 125000},
            "CELANA-02": {"nama": "Celana Chino Slim Fit", "stok": 0, "harga": 185000},
            "JAKET-03": {"nama": "Jaket Parka Outdoor", "stok": 4, "harga": 275000}
        }
        item = demo_stock.get(sku.upper())
        if item:
            return {"status": "success", "found": True, "item": item}
        return {"status": "success", "found": False, "message": f"SKU {sku} tidak ditemukan."}

    try:
        url = f"{SHEETS_API_URL}?sku={urllib.parse.quote(sku)}"
        req = urllib.request.Request(url, headers={"User-Agent": "YukSuruhAI-StockBot/1.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        return {"status": "error", "message": str(e)}

def format_stock_response(query_result: dict, sku: str) -> str:
    """Format pesan balasan ramah pelanggan khas Indonesia."""
    if not query_result.get("found"):
        return f"🌱 Maaf kak, produk dengan kode `{sku.upper()}` belum terdaftar di stok kami. Coba pastikan lagi kode produknya ya!"

    item = query_result["item"]
    stok = item.get("stok", 0)
    nama = item.get("nama", "Produk")
    harga = item.get("harga", 0)

    if stok > 0:
        return (
            f"✅ *Stok Tersedia!*\n\n"
            f"📦 *Produk:* {nama}\n"
            f"🏷 *Kode SKU:* `{sku.upper()}`\n"
            f"📊 *Sisa Stok:* {stok} unit\n"
            f"💰 *Harga:* Rp {harga:,}\n\n"
            f"Mau dibantu order sekarang kak? Silakan kirim alamat dan jumlah pesanan ya 🌱"
        )
    else:
        return (
            f"⚠️ *Stok Sedang Kosong*\n\n"
            f"📦 *Produk:* {nama}\n"
            f"🏷 *Kode SKU:* `{sku.upper()}`\n"
            f"Mohon maaf kak, stok untuk varian ini saat ini sedang habis. Perkiraan restock 3-5 hari ke depan ya! 🌱"
        )

def main():
    print("=== Demo Cek Stok Toko YukSuruhAI (Google Sheets + Telegram) ===")
    test_skus = ["KEMEJA-01", "CELANA-02", "SEPATU-99"]
    for sku in test_skus:
        res = query_stock_from_sheets(sku)
        formatted = format_stock_response(res, sku)
        print(f"\n--- Kueri SKU: {sku} ---")
        print(formatted)

if __name__ == "__main__":
    main()
