import os
from PIL import Image, ImageEnhance, ImageOps

SRC = "/Users/rahulra/.cursor/projects/Users-rahulra-claude-rahulkrishnanra/assets"
OUT = "/Users/rahulra/claude/rahulkrishnanra/src/assets/gallery"
os.makedirs(OUT, exist_ok=True)

# Ordered list of source files -> output index (must match captions in Gallery.jsx)
files = [
    "image-495acac2-806d-49ac-a3d8-b2b2c8801fab.png",
    "image-335df07d-a5a1-4d7e-9634-fc9ad3097dd5.png",
    "image-521fd1aa-9352-4017-a776-0eced40f8389.png",
    "image-deddc486-228d-4889-85b1-f9c787c0a22f.png",
    "image-88ce5343-82ad-4045-82e9-95df5b738c7c.png",
    "image-eba3b4ed-b832-422d-9791-f06cd9f178a2.png",
    "image-c73e00a2-eadc-40cf-87c2-0ccbb42f5541.png",
    "image-57736f8e-778b-4897-8903-a1128e4ca8ea.png",
    "image-b2026da2-512a-4474-9320-87e9bfff1c87.png",
    "image-03cadb2c-f21c-4cc8-b11b-9dd555f30b90.png",
    "image-fd280ed1-3a34-4dd7-bd4c-2eb16ef036d9.png",
    "image-83e905f1-dfe5-48bb-9225-2ef413cce68a.png",
    "image-6a8025fe-132b-4103-ac47-48988d82f5a3.png",
    "image-f67a7047-f596-4042-a213-c5e580e3af8b.png",
    "image-afd1b558-265b-4bb5-8b66-41394608ffef.png",
    "image-d0d349de-a50c-49fb-a860-c695c13a55c0.png",
]

MAX = 1400

for i, name in enumerate(files, start=1):
    path = os.path.join(SRC, name)
    im = Image.open(path)
    im = ImageOps.exif_transpose(im).convert("RGB")
    # resize to max long edge
    w, h = im.size
    scale = min(1.0, MAX / max(w, h))
    if scale < 1.0:
        im = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    # enhancements: brightness, contrast, color, sharpness
    im = ImageEnhance.Brightness(im).enhance(1.05)
    im = ImageEnhance.Contrast(im).enhance(1.10)
    im = ImageEnhance.Color(im).enhance(1.08)
    im = ImageEnhance.Sharpness(im).enhance(1.45)
    out = os.path.join(OUT, f"gallery-{i:02d}.jpg")
    im.save(out, "JPEG", quality=85, optimize=True, progressive=True)
    print(f"saved {out} {im.size}")

print("done")
