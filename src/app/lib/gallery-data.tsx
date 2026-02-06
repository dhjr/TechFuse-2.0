export type GalleryItem = {
  id: number;
  src: string;
  category: string;
  alt: string;
  width: number;
  height: number;
};

const IMAGE_COUNT = 27;

export const galleryImages: GalleryItem[] = Array.from(
    { length: IMAGE_COUNT },
    (_, i) => {
        const index = String(i + 1).padStart(2, "0");

        return {
            id: i + 1,
            src: `/techFuseGallery/glimpses of techfuse${index}.webp`,
            category: "Glimpses",
            alt: "Glimpses of TechFuse 2.0",
            width: 800,
            height: 600,
        };
    }
);

