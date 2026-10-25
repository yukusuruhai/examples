/**
 * Google Apps Script Webhook: Penerima Data Nota Otomatis ke Google Sheets
 * Pasang skrip ini di menu Extensions -> Apps Script pada Google Sheets Anda.
 * Deploy sebagai "Web App" dengan akses "Anyone" (Siapa saja).
 */

function doPost(e) {
  try {
    var rawData = e.postData.contents;
    var data = JSON.parse(rawData);

    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

    // Buat header otomatis jika sheet masih kosong
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        "Tanggal",
        "Nama Toko",
        "Kategori",
        "Total Akhir (IDR)",
        "Metode Bayar",
        "Nomor Struk",
        "Keterangan",
        "Waktu Input"
      ]);
    }

    // Tambahkan baris transaksi baru
    sheet.appendRow([
      data.tanggal || new Date().toISOString().split("T")[0],
      data.nama_toko || "-",
      data.kategori || "Umum",
      data.total_akhir || 0,
      data.metode_bayar || "CASH",
      data.nomor_struk || "-",
      data.keterangan || "-",
      new Date().toLocaleString("id-ID")
    ]);

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "Data nota berhasil disimpan ke spreadsheet"
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
