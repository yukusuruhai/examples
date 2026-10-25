# Minimal 30-Line FastMCP Server in Python (Model Context Protocol)
import sys
import json

def get_product_stock(sku: str) -> str:
    """Cek stok dan harga produk dari database lokal secara real-time."""
    demo_db = {
        "KEMEJA-01": {"nama": "Kemeja Katun Polos", "stok": 14, "harga": 120000},
        "CELANA-02": {"nama": "Celana Chino Slim", "stok": 0, "harga": 185000}
    }
    item = demo_db.get(sku.upper())
    if not item:
        return f"Produk dengan SKU {sku} tidak ditemukan."
    return f"Nama: {item['nama']} | Stok: {item['stok']} unit | Harga: Rp {item['harga']:,}"

if __name__ == "__main__":
    # Sederhana: bisa dijalankan langsung dengan 'mcp run server.py' atau stdio loop
    try:
        from mcp.server.fastmcp import FastMCP
        mcp = FastMCP("yuksuruhai-tools")

        @mcp.tool()
        def cek_stok(kode_sku: str) -> str:
            """Cek stok dan harga barang toko."""
            return get_product_stock(kode_sku)

        mcp.run()
    except ImportError:
        # Fallback stdio jika package mcp belum terpasang
        if len(sys.argv) > 1:
            print(get_product_stock(sys.argv[1]))
        else:
            print("Gunakan: python server.py KEMEJA-01 (atau install mcp via 'pip install mcp')")
