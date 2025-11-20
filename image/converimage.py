from PIL import Image
import os

def convert_to_1920x1080(input_path, output_path="converted.jpg"):
    """
    Convert any image to exactly 1920x1080 resolution.
    - Crops excess parts to avoid distortion
    - Converts RGBA → RGB if saving as JPEG
    """

    img = Image.open(input_path)

    target_size = (1920, 1080)
    target_ratio = target_size[0] / target_size[1]
    img_ratio = img.width / img.height

    if img_ratio > target_ratio:
        # Wider → fit height, crop width
        new_height = target_size[1]
        new_width = int(new_height * img_ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        left = (new_width - target_size[0]) // 2
        img = img.crop((left, 0, left + target_size[0], target_size[1]))
    else:
        # Taller → fit width, crop height
        new_width = target_size[0]
        new_height = int(new_width / img_ratio)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        top = (new_height - target_size[1]) // 2
        img = img.crop((0, top, target_size[0], top + target_size[1]))

    # 🔑 Convert RGBA → RGB if saving as JPEG
    if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
        img = img.convert("RGB")

    img.save(output_path)
    print(f"✅ Converted and cropped: {input_path} → {output_path}")

if __name__ == "__main__":
    source = input("Enter the path to your source image: ").strip()
    if os.path.isfile(source):
        convert_to_1920x1080(source, "converted.jpg")
    else:
        print("❌ File not found. Please check the path and try again.")
