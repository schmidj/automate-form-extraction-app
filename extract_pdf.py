from docling.document_converter import DocumentConverter
import json

# Path to your PDF
input_file = "data/URSUS CREEK AREA 24_Redacted_Catalog-pages-1.pdf"

# Initialize converter
converter = DocumentConverter()

# Convert document
result = converter.convert(input_file)

# Extract structured document
doc = result.document

# Convert to dictionary (structured format)
doc_dict = doc.export_to_dict()

# Save as JSON
with open("output_results/output.json", "w", encoding="utf-8") as f:
    json.dump(doc_dict, f, indent=2, ensure_ascii=False)

print("Done! JSON saved as output.json")