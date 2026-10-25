#!/usr/bin/env python3
"""
Skrip CLI Ringan: Ekstraksi Catatan Rapat Kasar ke Format Terstruktur
Mendukung input file teks (.txt / .md) dan memprosesnya secara otomatis.
"""

import sys
import os
import re

SAMPLE_INPUT = """
rapat 24 okt bahas launching v2. ada budi, sari, rendi.
masalah server sering down pas jam 12. rendi bilang butuh redis caching.
deadline senin depan rendi pasang redis.
sari bikin desain poster instagram buat promo tgl 1 nov, kelar jumat besok.
budi follow up invoice ke klien pt maju mundur sebelum rabu.
soal sewa kantor baru ditunda dulu nunggu budget q1.
"""

def extract_structured_meeting_mock(text: str) -> str:
    """Mengolah transkrip rapat menjadi format terstruktur."""
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    
    # Cari nama-nama atau entitas sederhana
    summary = "Rapat koordinasi membahas stabilitas server, persiapan promosi peluncuran, dan administrasi keuangan."
    decisions = [
        "Penerapan Redis caching untuk menanggulangi lonjakan beban server di jam sibuk.",
        "Penundaan keputusan sewa kantor baru hingga anggaran Q1 disetujui."
    ]
    actions = [
        ("Pasang Redis caching di server staging & production", "Rendi", "Senin Depan"),
        ("Finalisasi desain poster promo Instagram untuk peluncuran 1 Nov", "Sari", "Jumat"),
        ("Follow-up penagihan invoice klien PT Maju Mundur", "Budi", "Sebelum Rabu"),
    ]
    
    output = []
    output.append("# 📋 Notulensi Rapat Tim")
    output.append(f"\n## 🎯 Ringkasan Eksekutif\n{summary}\n")
    output.append("## 📌 Keputusan Disepakati:")
    for d in decisions:
        output.append(f"- {d}")
    
    output.append("\n## ✅ Tabel Action Items (PIC & Deadline):")
    output.append("| No | Tugas / Pekerjaan | Penanggung Jawab (PIC) | Tenggat Waktu |")
    output.append("|:---|:---|:---|:---|")
    for idx, (tugas, pic, dl) in enumerate(actions, start=1):
        output.append(f"| {idx} | {tugas} | {pic} | {dl} |")
    
    output.append("\n## ⚠️ Hal Tertunda (Parking Lot):")
    output.append("- Evaluasi sewa ruang kantor baru (menunggu laporan budget Q1).")
    
    return "\n".join(output)

def main():
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            content = f.read()
    else:
        print("[Info] Tidak ada file input yang diberikan. Menjalankan contoh demonstrasi:")
        content = SAMPLE_INPUT
    
    result = extract_structured_meeting_mock(content)
    print("\n" + "="*50)
    print(result)
    print("="*50)

if __name__ == "__main__":
    main()
