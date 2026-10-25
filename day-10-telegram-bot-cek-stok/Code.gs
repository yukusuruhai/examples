/**
 * Google Apps Script: API Sederhana Cek Stok Toko dari Google Sheets (Day 10)
 * Menjadikan Google Sheets sebagai database REST API gratis untuk bot Telegram.
 */

function doGet(e) {
  var skuQuery = (e.parameter.sku || "").toUpperCase().trim();
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();

  // Format Kolom: [0: SKU, 1: Nama Produk, 2: Stok, 3: Harga Satuan, 4: Status]
  // Contoh: ["KEMEJA-01", "Kemeja Katun Polos Hitam", 15, 125000, "Ready"]

  if (!skuQuery) {
    // Jika tidak ada parameter sku, kembalikan daftar seluruh barang yang ready
    var allItems = [];
    for (var i = 1; i < data.length; i++) {
      if (data[i][0]) {
        allItems.push({
          sku: data[i][0],
          nama: data[i][1],
          stok: Number(data[i][2]),
          harga: Number(data[i][3]),
          status: data[i][4] || "Ready"
        });
      }
    }
    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      total_items: allItems.length,
      data: allItems
    })).setMimeType(ContentService.MimeType.JSON);
  }

  // Cari spesifik berdasarkan SKU
  for (var j = 1; j < data.length; j++) {
    if (String(data[j][0]).toUpperCase().trim() === skuQuery) {
      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        found: true,
        item: {
          sku: data[j][0],
          nama: data[j][1],
          stok: Number(data[j][2]),
          harga: Number(data[j][3]),
          status: data[j][4] || (Number(data[j][2]) > 0 ? "Ready" : "Habis")
        }
      })).setMimeType(ContentService.MimeType.JSON);
    }
  }

  return ContentService.createTextOutput(JSON.stringify({
    status: "success",
    found: false,
    message: "SKU " + skuQuery + " tidak ditemukan."
  })).setMimeType(ContentService.MimeType.JSON);
}
