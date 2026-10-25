import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

// 1. Inisialisasi Server MCP Stdio
const server = new Server(
  { name: "yuksuruhai-sqlite-tools", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// 2. Daftarkan Daftar Tool yang Tersedia
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "cek_stok_produk",
    description: "Cek stok dan harga produk dari database lokal secara real-time.",
    inputSchema: {
      type: "object",
      properties: { kode_sku: { type: "string", description: "SKU produk" } },
      required: ["kode_sku"]
    }
  }]
}));

// 3. Tangani Eksekusi Tool (Handler)
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "cek_stok_produk") {
    const sku = String(request.params.arguments?.kode_sku);
    // Contoh pembacaan cepat dari database / in-memory inventory
    const demoDb: Record<string, { nama: string; stok: number; harga: number }> = {
      "KEMEJA-01": { nama: "Kemeja Katun Polos", stok: 14, harga: 120000 },
      "CELANA-02": { nama: "Celana Chino Slim", stok: 0, harga: 185000 }
    };
    const item = demoDb[sku.toUpperCase()];
    if (!item) return { content: [{ type: "text", text: `Produk dengan SKU ${sku} tidak ditemukan.` }] };
    return {
      content: [{ type: "text", text: `Nama: ${item.nama} | Stok: ${item.stok} unit | Harga: Rp ${item.harga.toLocaleString('id-ID')}` }]
    };
  }
  throw new Error("Tool tidak dikenal");
});

// 4. Jalankan Transport Stdio
const transport = new StdioServerTransport();
await server.connect(transport);
