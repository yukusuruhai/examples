# Bikin MCP Server Pertamamu dalam 30 Baris Kode (Day 6)

Panduan praktis membangun server **Model Context Protocol (MCP)** sederhana untuk menghubungkan AI ke database inventori lokal.

## Mengapa MCP?
Tanpa MCP, AI bekerja terisolasi dan rawan halusinasi. Dengan MCP, AI bisa memanggil fungsi lokal (`tools`) seperti mengecek stok gudang secara real-time tanpa mengekspos seluruh data ke cloud publik.

## Cara Menjalankan

### Versi TypeScript / Node.js
1. Pasang dependensi:
   ```bash
   pnpm add @modelcontextprotocol/sdk
   ```
2. Jalankan:
   ```bash
   npx tsx server.ts
   ```

### Versi Python
1. Pasang dependensi:
   ```bash
   pip install mcp
   ```
2. Jalankan:
   ```bash
   python server.py
   ```

### Menghubungkan ke Claude Desktop / Cursor
Tambahkan konfigurasi berikut ke file konfigurasi Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "yuksuruhai-inventory": {
      "command": "python",
      "args": ["/path/ke/day-06-mcp-server-30-baris/server.py"]
    }
  }
}
```
AI Anda sekarang dapat langsung menjawab pertanyaan seperti: *"Berapa stok KEMEJA-01 sekarang?"* dengan akurasi 100%.
