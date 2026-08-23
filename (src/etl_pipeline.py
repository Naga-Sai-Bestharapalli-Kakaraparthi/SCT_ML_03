import os
import glob
import logging
import numpy as np
import cv2
from typing import Tuple, List, Dict, Generator

# Configure logging for production observability
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class ImageETLPipeline:
    """ETL Pipeline for extracting, transforming, and loading image dataset features."""

    def __init__(self, raw_data_dir: str, img_size: Tuple[int, int] = (64, 64)):
        self.raw_data_dir = raw_data_dir
        self.img_size = img_size
        self.categories = ["Cat", "Dog"]

    def extract_batch(self, batch_size: int = 32) -> Generator[List[Tuple[str, str]], None, None]:
        """Extract step: Yields file paths in batches to prevent memory overhead."""
        all_files: List[Tuple[str, str]] = []
        for category in self.categories:
            path = os.path.join(self.raw_data_dir, category, "*.[jJ][pP][gG]")
            files = glob.glob(path)
            all_files.extend([(f, category) for f in files])

        logging.info(f"Discovered {len(all_files)} total records.")
        
        for i in range(0, len(all_files), batch_size):
            yield all_files[i:i + batch_size]

    def transform(self, file_batch: List[Tuple[str, str]]) -> Tuple[np.ndarray, np.ndarray]:
        """Transform step: Validates, resizes, normalizes, and extracts flattened features."""
        features, labels = [], []
        
        for img_path, label_str in file_batch:
            try:
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue  # Handle corrupt images
                
                # Image processing standardisation
                resized = cv2.resize(img, self.img_size)
                normalized = resized.astype(np.float32) / 255.0
                
                features.append(normalized.flatten())
                labels.append(0 if label_str == "Cat" else 1)
            except Exception as e:
                logging.warning(f"Error processing {img_path}: {e}")
                continue

        return np.array(features), np.array(labels)

    def run_pipeline(self) -> Dict[str, np.ndarray]:
        """Executes full ETL process."""
        logging.info("Starting Data Ingestion & Transformation Pipeline...")
        X_list, y_list = [], []

        for batch in self.extract_batch(batch_size=64):
            X_batch, y_batch = self.transform(batch)
            if X_batch.size > 0:
                X_list.append(X_batch)
                y_list.append(y_batch)

        X_final = np.vstack(X_list) if X_list else np.empty((0,))
        y_final = np.concatenate(y_list) if y_list else np.empty((0,))

        logging.info(f"ETL Complete. Processed shape: {X_final.shape}")
        return {"features": X_final, "labels": y_final}

if __name__ == "__main__":
    pipeline = ImageETLPipeline(raw_data_dir="./PetImages")
    data = pipeline.run_pipeline()
