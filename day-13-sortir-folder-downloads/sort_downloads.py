#!/usr/bin/env python3
"""
Skrip Pintar: Sortir Otomatis Folder Downloads Berdasarkan Isi Dokumen (Day 13)
Membaca 50 kata pertama isi file teks / dokumen, mendeteksi jenis dokumen,
dan memindahkannya otomatis ke folder arsip yang rapi.
"""

import os
import sys
import shutil
import re
from pathlib import Path

# Kategori folder tujuan berdasarkan kata kunci isi dokumen
CATEGORIES = {
    "Faktur_Pajak": ["faktur pajak", "djp", "nomor seri faktur", "ppn", "npwp"],
    "Invoices": ["invoice", "tagihan", "total tagihan", "rekening pembayaran", "due date", "jatuh tempo"],
    "Proposal_Kerjasama": ["proposal", "latar belakang", "kerjasama", "ruang lingkup", "penawaran kerjasama"],
    "Laporan_Keuangan": ["neraca", "laba rugi", "arus kas", "saldo awal", "jurnal penyesuaian"],
    "Notulensi_Rapat": ["notulensi", "notulen", "daftar hadir rapat", "action items", "agenda rapat"]
}

def extract_first_words(file_path: Path, word_limit: int = 50) -> str:
    """Membaca isi awal dokumen teks dengan aman."""
    suffix = file_path.suffix.lower()
    text = ""

    try:
        if suffix in [".txt", ".md", ".csv"]:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read(2048)
        elif suffix == ".pdf":
            # Ekstraksi PDF jika pypdf terpasang, jika tidak baca raw string
            try:
                import pypdf
                reader = pypdf.PdfReader(str(file_path))
                if reader.pages:
                    text = reader.pages[0].extract_text() or ""
            except ImportError:
                with open(file_path, "rb") as f:
                    raw = f.read(4096)
                    text = re.sub(rb"[^\x20-\x7E]", b" ", raw).decode("ascii", errors="ignore")
        elif suffix in [".docx"]:
            try:
                import docx
                doc = docx.Document(str(file_path))
                text = " ".join([p.text for p in doc.paragraphs[:5]])
            except ImportError:
                text = ""
    except Exception:
        text = ""

    words = text.split()[:word_limit]
    return " ".join(words).lower()

def detect_category(sample_text: str, filename: str) -> str:
    """Mendeteksi kategori dokumen berdasarkan isi teks atau nama file."""
    combined = (sample_text + " " + filename).lower()
    
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in combined:
                return category
    return "Arsip_Umum"

def sort_downloads_folder(folder_path: Path, is_dry_run: bool = True):
    """Memindai dan merapikan folder dokumen."""
    print(f"🔍 Memindai direktori: {folder_path.resolve()} (Dry-Run: {is_dry_run})")
    
    supported_extensions = [".txt", ".md", ".pdf", ".docx", ".csv"]
    files_to_process = [
        f for f in folder_path.iterdir()
        if f.is_file() and f.suffix.lower() in supported_extensions and not f.name.startswith(".")
    ]

    if not files_to_process:
        print("ℹ️ Tidak ditemukan file dokumen di folder ini.")
        return

    stats = {}

    for file_path in files_to_process:
        sample_text = extract_first_words(file_path)
        category = detect_category(sample_text, file_path.name)
        
        target_dir = folder_path / category
        target_path = target_dir / file_path.name

        print(f"📄 '{file_path.name}' ➔ Kategori: [{category}]")
        stats[category] = stats.get(category, 0) + 1

        if not is_dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file_path), str(target_path))

    print("\n📊 Ringkasan Penataan Dokumen:")
    for cat, count in stats.items():
        print(f"  • {cat}: {count} file")
        
    if is_dry_run:
        print("\n💡 Ini adalah simulasi (Dry Run). Untuk memindahkan file secara nyata, jalankan:")
        print("   python sort_downloads.py --apply")

def main():
    target_dir = Path.home() / "Downloads"
    is_apply = "--apply" in sys.argv
    
    # Memungkinkan kustomisasi folder via argumen CLI
    custom_dirs = [a for a in sys.argv[1:] if not a.startswith("--")]
    if custom_dirs and os.path.exists(custom_dirs[0]):
        target_dir = Path(custom_dirs[0])

    print("=== Bot Sortir Folder Downloads Otomatis (YukSuruhAI Day 13) ===")
    sort_downloads_folder(target_dir, is_dry_run=not is_apply)

if __name__ == "__main__":
    main()
