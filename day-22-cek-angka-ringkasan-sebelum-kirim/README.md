# Modul 22: Angka Ini dari Sel Mana? Cek Ringkasan AI ke Sheet Aslinya dalam 10 Menit, Sebelum Dikirim ke Atasan 🌱
> **Fokus Praktik:** Track 1: Produktivitas & Karyawan
## Mengapa Modul Ini Penting?
Hari 21 sudah membangun kebiasaan jujur bahwa sebuah karya dibantu AI. Langkah berikutnya adalah membuktikan isinya benar. Ada 29 pertanyaan dari teman-teman non-teknis dan komentar 'ini AI generated ya?' di media sosial, jadi hari ini kita ajarkan satu kebiasaan cek yang sederhana: setiap angka dalam ringkasan AI harus bisa ditelusuri ke sel aslinya.
## Alur Langkah Praktis
- 1. Minta AI menulis alamat sel di setiap angka (Sheet2!C14)
- 2. Buka sheet asli, cocokkan 3 angka yang dipilih acak
- 3. Coret angka tanpa sumber, catat di jejak kerja harian
## Contoh Perintah / Spesimen Lokal
```bash
$ sha256sum penjualan_oktober.csv
3fa9…c21e  penjualan_oktober.csv  (sidik jari sumber)
$ ollama run llama3.2 < cek_ringkasan.txt
Contoh hasil: 9 angka cocok • 1 tanpa alamat sel → dicoret
Egress cloud: 0 byte 🌱
```

## Template Prompt Siap Pakai: Cek Angka Sebelum Kirim: Telusuri Setiap Angka Ringkasan AI ke Sel Sumbernya
> Ringkasan buatan AI sering memuat angka yang terdengar meyakinkan tapi tidak ada di data asli. Akibatnya karyawan ditanya atasan dan harus menelusuri ulang berjam-jam. Prompt ini memaksa setiap angka menyebut alamat selnya, menandai angka yang tidak bisa dibuktikan, dan menghasilkan versi ringkasan yang aman untuk dikirim.

### System Instruction
```text
Kamu adalah pemeriksa data yang teliti, jujur, dan tenang. Tugasmu bukan membuat ringkasan baru, tapi memverifikasi setiap angka dalam ringkasan terhadap data sumber yang diberikan. Aturan: (1) Hanya gunakan data sumber yang ditempel, jangan menebak atau menghitung dari pengetahuan umum. (2) Setiap angka harus dipasangkan dengan alamat sel atau baris sumbernya. (3) Jika angka hasil perhitungan, tuliskan rumusnya secara eksplisit. (4) Jika angka tidak ditemukan, katakan 'TIDAK DITEMUKAN' dengan jujur dan jangan mengarang sumber. (5) Gunakan bahasa Indonesia yang sederhana dan sapa pengguna dengan 'kamu'.
```

### User Prompt Template (1-Tap Copy)
```text
Aku punya data sumber dan ringkasan buatan AI yang akan aku kirim ke [PENERIMA]. Tolong periksa setiap angka dalam ringkasan.

DATA SUMBER (beserta nama sheet dan kolom):
[DATA_SUMBER]

RINGKASAN AI YANG AKAN DIKIRIM:
[RINGKASAN_AI]

Buat hasil dalam 3 bagian:

1. TABEL VERIFIKASI
| No | Angka di Ringkasan | Alamat Sel / Baris Sumber | Rumus (jika hitungan) | Status: COCOK / BERBEDA / TIDAK DITEMUKAN |

2. CATATAN RISIKO
Sebutkan maksimal 3 angka paling berisiko jika ditanya [PENERIMA], beserta alasannya dalam 1 kalimat.

3. RINGKASAN AMAN KIRIM
Tulis ulang ringkasan hanya dengan angka berstatus COCOK, sertakan alamat sel dalam kurung di setiap angka. Untuk angka yang dibuang, tulis '(dihapus: sumber belum jelas)'.

Jangan menambah angka baru yang tidak ada di data sumber.
```

💡 **Tips Praktis:** Di contoh ini, total yang benar adalah Rp10,75 juta (SUM B2:B4), bukan Rp12,4 juta. Angka 'naik 8%' juga tidak bisa dibuktikan karena data September tidak ikut ditempel. Inilah alasan kita cek sebelum kirim. Mulailah dengan mencocokkan 3 angka acak secara manual di sheet asli. Kalau ketiganya cocok, kamu boleh lebih tenang. Kalau ada satu saja yang meleset, periksa semuanya. 🌱
---
🔗 Diskusi & tanya-jawab langsung bersama komunitas di Telegram: [YukSuruhAI Hub](https://t.me/+mYEesFREPu8zOTg9) 🌱
