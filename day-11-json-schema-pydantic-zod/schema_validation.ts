import { z } from "zod";

// Skema Validasi Runtime Zod untuk Pipeline AI
export const TransactionItemSchema = z.object({
  product_code: z.string().min(1, "Kode produk wajib diisi"),
  quantity: z.number().int().positive("Kuantitas wajib berupa bilangan bulat positif"),
  unit_price: z.number().nonnegative("Harga tidak boleh negatif")
});

export const CustomerOrderSchema = z.object({
  customer_name: z.string().min(2, "Nama pembeli minimal 2 karakter"),
  payment_method: z.enum(["QRIS", "TRANSFER", "COD", "UNKNOWN"]),
  items: z.array(TransactionItemSchema).min(1, "Minimal terdapat 1 item"),
  notes: z.string().nullable().optional(),
  is_urgent: z.boolean().default(false)
});

export type CustomerOrder = z.infer<typeof CustomerOrderSchema>;

export function parseAndValidateLLMJson(rawOutput: string): CustomerOrder {
  let cleaned = rawOutput.trim();
  if (cleaned.startsWith("```")) {
    cleaned = cleaned.replace(/^```[a-z]*\n?/i, "").replace(/\n?```$/i, "");
  }
  const parsed = JSON.parse(cleaned);
  return CustomerOrderSchema.parse(parsed);
}
