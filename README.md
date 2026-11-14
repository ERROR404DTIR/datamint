<div align="center">

![Animated project banner](assets/banner.svg)

# DataMint

**Generate reproducible synthetic datasets from JSON schemas. Supports IDs, strings, integers, decimals, booleans, choices and dates; exports JSON or CSV.**

![MIT](https://img.shields.io/badge/license-MIT-8b5cf6) ![Local-first](https://img.shields.io/badge/privacy-local--first-06b6d4)

</div>

## Quick start

```bash
python app.py schema.example.json --count 100 --seed 7 --format csv -o sample.csv
```

## Features

Generate reproducible synthetic datasets from JSON schemas. Supports IDs, strings, integers, decimals, booleans, choices and dates; exports JSON or CSV.

- Minimal setup; no account or telemetry.
- Clear, local-first workflow.
- Responsive interface where applicable.

## Requirements

A modern browser. No package manager, build step, server, or external CDN is required.

## Tests

```bash
python -m unittest -v
```

## Privacy and safety

- Browser tools process data locally and do not upload it.
- StoragePeek only reads the storage of the current origin; review changes before deleting entries.
- ExifWipe re-encodes a copy and never modifies the original image.
- MockForge binds to loopback only by default.

## License

MIT. See [LICENSE](LICENSE).
