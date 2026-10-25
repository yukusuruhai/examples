#!/usr/bin/env python3
"""
Mengunci Schema Validation & Pydantic V2 di Pipeline AI (Day 11)
Mencegah JSON patah atau halusinasi tipe data saat menerima respons dari model LLM.
"""

import json
from typing import List, Literal, Optional
from pydantic import BaseModel, Field, ValidationError

class TransactionItem(BaseModel):
    product_code: str = Field(description="Kode SKU produk yang valid")
    quantity: int = Field(gt=0, description="Jumlah barang wajib lebih dari 0")
    unit_price: int = Field(ge=0, description="Harga satuan dalam IDR")

class CustomerOrderSchema(BaseModel):
    customer_name: str = Field(min_length=2, description="Nama pelanggan")
    payment_method: Literal["QRIS", "TRANSFER", "COD", "UNKNOWN"]
    items: List[TransactionItem]
    notes: Optional[str] = None
    is_urgent: bool = False

def validate_llm_json_response(raw_llm_output: str) -> dict:
    """Membersihkan markdown backticks dan memvalidasi tipe data secara ketat."""
    # 1. Bersihkan potensi bungkus ```json ... ```
    cleaned = raw_llm_output.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        cleaned = "\n".join(lines).strip()

    # 2. Parsing JSON dasar
    parsed_dict = json.loads(cleaned)

    # 3. Validasi skema runtime Pydantic V2
    validated = CustomerOrderSchema.model_validate(parsed_dict)
    return validated.model_dump()

def main():
    print("=== Demo Schema Validation Pydantic V2 ===")
    
    # Contoh output LLM yang valid
    valid_payload = """
    ```json
    {
      "customer_name": "Rudi Hartono",
      "payment_method": "TRANSFER",
      "items": [
        {"product_code": "KEMEJA-01", "quantity": 2, "unit_price": 120000}
      ],
      "is_urgent": true
    }
    ```
    """
    
    try:
        data = validate_llm_json_response(valid_payload)
        print("✅ Berhasil memvalidasi respons AI:")
        print(json.dumps(data, indent=2))
    except ValidationError as e:
        print("❌ Skema gagal:", e)

    # Contoh payload rusak (quantity <= 0)
    invalid_payload = '{"customer_name": "B", "payment_method": "BITCOIN", "items": [{"product_code": "X", "quantity": 0, "unit_price": 100}]}'
    try:
        validate_llm_json_response(invalid_payload)
    except ValidationError as e:
        print("\n✅ Terdeteksi validasi gagal seperti yang diharapkan:")
        for err in e.errors():
            print(f"- Field '{err['loc']}': {err['msg']}")

if __name__ == "__main__":
    main()
