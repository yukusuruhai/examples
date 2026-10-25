# Output JSON Tanpa Patah: Schema Validation & Pydantic / Zod (Day 11)

Banyak software engineer mengeluhkan respons AI yang format JSON-nya sering patah (broken json), format berubah-ubah, atau tipe data halusinasi saat dipasang di production.

Solusi industri: **Constrained Decoding & Runtime Schema Validation**.
- Di ekosistem Python: Gunakan **Pydantic V2** (`schema_validation.py`).
- Di ekosistem TypeScript / Node: Gunakan **Zod** (`schema_validation.ts`).

## Keuntungan:
1. Menjamin output model AI 100% *type-safe* sebelum dieksekusi ke database.
2. Mencegah kerentanan *token explosion* akibat loop retry tak berujung.
3. Memberikan pesan error deterministik jika AI menyimpang dari format yang diminta.
