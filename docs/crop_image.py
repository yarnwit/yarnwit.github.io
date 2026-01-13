from PIL import Image
import os

try:
    img_path = 'user_input_files/Myresume.png'
    output_path = 'public/images/profile.jpg'
    
    if os.path.exists(img_path):
        img = Image.open(img_path)
        width, height = img.size
        
        # Estimate the crop size for a standard resume photo (usually top left)
        # Assuming a reasonable square size relative to the document
        # Let's crop a square of about 400x400 pixels or 25% of width, whichever is smaller but reasonable
        
        crop_size = min(width // 3, height // 4, 500)
        
        # If the image is very small, just use it as is, otherwise crop top-left
        if width > 200 and height > 200:
            # Crop box: (left, top, right, bottom)
            # Adding a small margin if needed, but user said top-left corner
            left = 0
            top = 0
            right = crop_size
            bottom = crop_size
            
            cropped_img = img.crop((left, top, right, bottom))
            cropped_img = cropped_img.convert('RGB') # Ensure RGB for JPEG
            cropped_img.save(output_path, quality=95)
            print(f"Image cropped and saved to {output_path}")
        else:
            img.convert('RGB').save(output_path)
            print("Image too small to crop, saved original.")
    else:
        print("Source image not found.")
except Exception as e:
    print(f"Error: {e}")
