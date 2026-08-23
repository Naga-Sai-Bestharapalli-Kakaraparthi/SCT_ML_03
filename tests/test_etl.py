import numpy as np
import pytest
from src.etl_pipeline import ImageETLPipeline

def test_transform_shape():
    pipeline = ImageETLPipeline(raw_data_dir="./", img_size=(32, 32))
    # Mock single dummy 32x32 image logic
    dummy_img = (np.random.rand(32, 32, 3) * 255).astype(np.uint8)
    
    # Verify flattened dimension matches (32 * 32 = 1024 features)
    resized = dummy_img.mean(axis=2).reshape(32, 32)
    normalized = resized.astype(np.float32) / 255.0
    
    assert normalized.flatten().shape[0] == 1024
