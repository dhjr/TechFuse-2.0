from PIL import Image
import os

# Configuration
GALLERY_PATH = "public/techFuseGallery"
MAX_SIZE = (1920, 1920)
QUALITY = 85

def resize_images():
    if not os.path.exists(GALLERY_PATH):
        print(f"Directory not found: {GALLERY_PATH}")
        return

    count = 0
    saved_space = 0

    for filename in os.listdir(GALLERY_PATH):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            filepath = os.path.join(GALLERY_PATH, filename)
            
            try:
                original_size = os.path.getsize(filepath)
                with Image.open(filepath) as img:
                    # Check if resize is needed
                    if img.width > MAX_SIZE[0] or img.height > MAX_SIZE[1]:
                        img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
                        
                        # Save back to the same path
                        img.save(filepath, quality=QUALITY, optimize=True)
                        
                        new_size = os.path.getsize(filepath)
                        saved_space += (original_size - new_size)
                        count += 1
                        print(f"Resized {filename}: {original_size/1024/1024:.2f}MB -> {new_size/1024/1024:.2f}MB")
                    else:
                        print(f"Skipped {filename} (already small enough)")
                        
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print(f"\nCompleted! Resized {count} images.")
    print(f"Total space saved: {saved_space/1024/1024:.2f} MB")

if __name__ == "__main__":
    resize_images()
