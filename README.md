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

## License & Attribution

EudraLex Volume 4 is published by the European Commission and, under the
[Commission Decision of 12 December 2011 on the reuse of Commission documents](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011D0833),
is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

### Attribution

Contains public sector information from EudraLex Volume 4 (Good Manufacturing
Practice guidelines), © European Union, 1998–2025. Source: European Commission,
[Public Health website](https://health.ec.europa.eu/medicinal-products/eudralex/eudralex-volume-4_en).

### Modifications

The original PDFs have been renamed to a canonical naming convention for
automated tooling and may have been re-hosted in this repository.

### Endorsement Disclaimer

This repository is an unofficial mirror. The European Union emblem, the
European Commission logo, and the EMA logo are not used in a way that implies
endorsement, sponsorship, or affiliation with this project.

### Legal Disclaimer

This repository is an unofficial copy provided for convenience and
informational purposes only. It may not reflect the most recent regulatory
updates. The only authentic and legally binding versions of these documents
are those published in the Official Journal of the European Union or hosted on
the official [European Commission EudraLex portal](https://health.ec.europa.eu/medicinal-products/eudralex_en).
