# UI Data Contracts

## Pagination
- `{ total, page, pageSize, items: [...] }`

## Metadata
- Every metric includes `provenance: { source, asOf, modelVersion? }`

## Units
- Numeric fields carry `unit` when ambiguous. Example: `%`, `points`, `plays/g`.

## Download
- CSV and JSON endpoints mirror table schemas.
