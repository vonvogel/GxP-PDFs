#!/usr/bin/env python3
"""
Regenerate index.json for each PDF folder.

Usage:
    python3 update_index.py

Reads all .pdf files in PDF/GMP-Human/, PDF/GMP-Veterinary/, PDF/GCP/, PDF/GVP/,
PDF/GMP-IMP/ and writes/updates index.json in each folder with:

  - filename
  - title (from known metadata or derived from filename)
  - publication_date (ISO date or null)
  - download_date (current UTC timestamp)
  - sha256 (hex digest of file contents)

Existing entries are preserved if the sha256 matches; otherwise they are updated.
New entries are added. Deleted PDFs are removed from the index.

Edit KNOWN_TITLES and KNOWN_DATES below to add new documents.
"""

import json
import hashlib
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "PDF"

KNOWN_TITLES = {
    # GMP-Human — EudraLex Volume 4
    "chapter_1.pdf": "EudraLex Volume 4, Chapter 1 — Pharmaceutical Quality System",
    "chapter_2.pdf": "EudraLex Volume 4, Chapter 2 — Personnel",
    "chapter_3.pdf": "EudraLex Volume 4, Chapter 3 — Premises and Equipment",
    "chapter_4.pdf": "EudraLex Volume 4, Chapter 4 — Documentation",
    "chapter_5.pdf": "EudraLex Volume 4, Chapter 5 — Production",
    "chapter_6.pdf": "EudraLex Volume 4, Chapter 6 — Quality Control",
    "chapter_7.pdf": "EudraLex Volume 4, Chapter 7 — Outsourced Activities",
    "chapter_8.pdf": "EudraLex Volume 4, Chapter 8 — Complaints, Quality Defects and Product Recalls",
    "chapter_9.pdf": "EudraLex Volume 4, Chapter 9 — Self Inspection",
    "part_ii.pdf": "EudraLex Volume 4, Part II — Basic Requirements for Active Substances used as Starting Materials",
    "part_iv.pdf": "EudraLex Volume 4, Part IV — GMP Requirements for Advanced Therapy Medicinal Products",
    "annex_1.pdf": "EudraLex Volume 4, Annex 1 — Manufacture of Sterile Medicinal Products",
    "annex_2.pdf": "EudraLex Volume 4, Annex 2 — Manufacture of Biological Active Substances and Medicinal Products for Human Use",
    "annex_3.pdf": "EudraLex Volume 4, Annex 3 — Manufacture of Radiopharmaceuticals",
    "annex_6.pdf": "EudraLex Volume 4, Annex 6 — Manufacture of Medicinal Gases",
    "annex_7.pdf": "EudraLex Volume 4, Annex 7 — Manufacture of Herbal Medicinal Products",
    "annex_8.pdf": "EudraLex Volume 4, Annex 8 — Sampling of Starting and Packaging Materials",
    "annex_9.pdf": "EudraLex Volume 4, Annex 9 — Manufacture of Liquids, Creams and Ointments",
    "annex_10.pdf": "EudraLex Volume 4, Annex 10 — Manufacture of Pressurised Metered Dose Aerosol Preparations for Inhalation",
    "annex_11.pdf": "EudraLex Volume 4, Annex 11 — Computerised Systems",
    "annex_12.pdf": "EudraLex Volume 4, Annex 12 — Use of Ionising Radiation in the Manufacture of Medicinal Products",
    "annex_14.pdf": "EudraLex Volume 4, Annex 14 — Manufacture of Medicinal Products Derived from Human Blood or Plasma",
    "annex_15.pdf": "EudraLex Volume 4, Annex 15 — Qualification and Validation",
    "annex_16.pdf": "EudraLex Volume 4, Annex 16 — Certification by a Qualified Person and Batch Release",
    "annex_17.pdf": "EudraLex Volume 4, Annex 17 — Parametric Release",
    "annex_19.pdf": "EudraLex Volume 4, Annex 19 — Reference and Retention Samples",
    "annex_21.pdf": "EudraLex Volume 4, Annex 21 — Importation of Medicinal Products",
    # GMP-Veterinary
    "reg_2025-2091.pdf": "Commission Implementing Regulation (EU) 2025/2091 — GMP for veterinary medicinal products",
    "reg_2025-2154.pdf": "Commission Implementing Regulation (EU) 2025/2154 — GMP for active substances in veterinary medicinal products",
}

KNOWN_DATES = {
    "chapter_1.pdf": "2013-01-31",
    "chapter_2.pdf": "2014-03-01",
    "chapter_4.pdf": "2011-01-01",
    "chapter_6.pdf": "2014-11-01",
    "chapter_7.pdf": "2012-06-01",
    "chapter_8.pdf": "2014-08-01",
    "part_ii.pdf": "2014-08-01",
    "part_iv.pdf": "2017-11-22",
    "annex_1.pdf": "2022-08-25",
    "annex_2.pdf": "2018-01-01",
    "annex_3.pdf": "2008-09-01",
    "annex_6.pdf": "2009-07-01",
    "annex_7.pdf": "2008-09-01",
    "annex_11.pdf": "2011-01-01",
    "annex_14.pdf": "2011-03-30",
    "annex_15.pdf": "2015-10-01",
    "annex_16.pdf": "2015-10-01",
    "annex_17.pdf": "2018-01-01",
    "annex_19.pdf": "2005-12-14",
    "reg_2025-2091.pdf": "2025-01-01",
    "reg_2025-2154.pdf": "2025-01-01",
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def update_folder(folder_path):
    index_path = folder_path / "index.json"
    existing = {}
    if index_path.exists():
        try:
            for entry in json.loads(index_path.read_text()):
                existing[entry["filename"]] = entry
        except Exception:
            pass

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    items = []

    for pdf in sorted(folder_path.glob("*.pdf")):
        fname = pdf.name
        old = existing.get(fname, {})
        old_hash = old.get("sha256")
        new_hash = sha256_file(pdf)

        items.append({
            "filename": fname,
            "title": KNOWN_TITLES.get(fname, fname.replace("_", " ").replace(".pdf", "").title()),
            "publication_date": KNOWN_DATES.get(fname),
            "download_date": now if old_hash != new_hash else old.get("download_date", now),
            "sha256": new_hash,
        })

    with open(index_path, "w") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    return len(items)


def main():
    folders = ["GMP-Human", "GMP-Veterinary", "GCP", "GVP", "GMP-IMP"]
    for folder in folders:
        fp = ROOT / folder
        fp.mkdir(parents=True, exist_ok=True)
        n = update_folder(fp)
        print(f"  {folder}: {n} entries")


if __name__ == "__main__":
    main()
