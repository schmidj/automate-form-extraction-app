from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import PdfFormatOption
import json

# Path to your PDF
input_file = "data/sea-sampling-CN-0003.pdf"

pipeline_options = PdfPipelineOptions(
    do_ocr=True,
    images_scale=3,
    generate_page_images=True
)

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=pipeline_options
        )
    }
)

# Initialize converter
converter = DocumentConverter()

# Convert document
result = converter.convert(input_file)

# Extract structured document
doc = result.document


for page in doc.pages.values():
    image = page.image
    image.save(f"page_{i}.png")

# Convert to dictionary (structured format)
doc_dict = doc.export_to_dict()

# Save as JSON
with open("output_results/output.json", "w", encoding="utf-8") as f:
    json.dump(doc_dict, f, indent=2, ensure_ascii=False)

print("Done! JSON saved as output.json")