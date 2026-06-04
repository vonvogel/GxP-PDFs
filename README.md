# GxP-PDFs

Source PDF repository for the GMP/GxP regulatory dashboard suite.
Stores original regulation PDFs referenced by GMPdash, GMPdashboardPDF, and related tools.

## Directory structure

```
PDF/
├── GMP-Human/       # EudraLex Volume 4 — Chapters 1–9, Parts II/IV, Annexes 1–21, Glossary
├── GMP-Veterinary/  # Regulations (EU) 2025/2091 and 2025/2154
├── GCP/             # Good Clinical Practice
├── GVP/             # Good Pharmacovigilance Practice
└── GMP-IMP/         # GMP for Investigational Medicinal Products
```

## PDF naming convention

Files follow the canonical naming from the GMP/GxP suite:

| Document | Filename |
|---|---|
| EudraLex Vol 4, Chapter 1 | `chapter_1.pdf` |
| EudraLex Vol 4, Annex 1 | `annex_1.pdf` |
| Regulation 2025/2091 | `reg_2025-2091.pdf` |
| Regulation 2025/2154 | `reg_2025-2154.pdf` |

See `eu-gmp-domain` skill for the full naming convention.

## Updates

When EUR-Lex publishes a revised PDF, replace the file here and rebuild
any downstream match data in `GMPdash` / `GMPdashboardPDF`.

## Related projects

- [GMPdash](https://github.com/vonvogel/GMPdash) — Self-contained regulatory dashboard
- [GMPdashboardPDF](https://github.com/vonvogel/GMPdashboardPDF) — Interactive PDF dashboard with highlights
