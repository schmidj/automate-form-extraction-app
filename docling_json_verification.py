import json
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from pdf2image import convert_from_path

pages = convert_from_path("data/sea-sampling-CN-0003.pdf", first_page=1, last_page=1)
pages[0].save("output_results/page1.png")

# Load JSON
with open("output_results/output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load your original PDF page as image (convert PDF → PNG first if needed)
image = Image.open("output_results/page1.png").convert("RGB")
draw = ImageDraw.Draw(image)

# Scale coordinates from PDF to image
page = data["pages"]["1"]
print(page)

pdf_width = page["size"]["width"]
pdf_height = page["size"]["height"]
print(f"PDF dimensions: {pdf_width} x {pdf_height}")

img_width, img_height = image.size
print(f"Image dimensions: {img_width} x {img_height}")

scale_x = img_width / pdf_width
scale_y = img_height / pdf_height

for t in data.get("texts", []):
    prov = t.get("prov", [])
    
    if not prov:
        continue
    
    bbox = prov[0].get("bbox", None)
    
    if not bbox:
        continue

    # Extract coordinates
    x0 = bbox["l"] * scale_x
    x1 = bbox["r"] * scale_x

    y0 = (pdf_height - bbox["t"]) * scale_y
    y1 = (pdf_height - bbox["b"]) * scale_y

    draw.rectangle([x0, y0, x1, y1], outline="red", width=3)

# Save result
plt.imshow(image)
plt.axis("off")
plt.savefig("output_results/Docling/debug_Docling.png", bbox_inches="tight", dpi=300)

print("Saved image as debug_overlay.png")