import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import json
import h5py


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "skin_disease_model.keras")


def load_model_custom(model_path):
    """Load model with quantization_config stripped from config."""
    try:
        # Try standard loading first
        return tf.keras.models.load_model(model_path)
    except (ValueError, TypeError) as e:
        if "quantization_config" in str(e):
            # Fallback: load model without quantization_config
            import zipfile
            import tempfile
            import shutil
            
            with tempfile.TemporaryDirectory() as tmp_dir:
                # Extract the .keras file (it's a zip)
                with zipfile.ZipFile(model_path, 'r') as zip_ref:
                    zip_ref.extractall(tmp_dir)
                
                # Load and modify config
                config_path = os.path.join(tmp_dir, "config.json")
                with open(config_path, 'r') as f:
                    config = json.load(f)
                
                # Strip quantization_config recursively
                def strip_quantization(obj):
                    if isinstance(obj, dict):
                        if 'quantization_config' in obj:
                            del obj['quantization_config']
                        for v in obj.values():
                            strip_quantization(v)
                    elif isinstance(obj, list):
                        for item in obj:
                            strip_quantization(item)
                
                strip_quantization(config)
                
                # Save modified config
                with open(config_path, 'w') as f:
                    json.dump(config, f)
                
                # Re-create the keras file
                temp_model_path = os.path.join(tmp_dir, "model_temp.keras")
                with zipfile.ZipFile(temp_model_path, 'w') as zip_ref:
                    for root, dirs, files in os.walk(tmp_dir):
                        for file in files:
                            if file != "model_temp.keras":
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, tmp_dir)
                                zip_ref.write(file_path, arcname)
                
                # Load the modified model
                return tf.keras.models.load_model(temp_model_path)
        else:
            raise


model = load_model_custom(MODEL_PATH)

classes = [
    "Atomic Dermatitis",
    "Basal Cell Carcinoma",
    "Eczema",
    "Melanocytic Nevi",
    "Melanoma",
    "Psoriasis",
    "Tinea Ringworm",
    "Warts Molluscum"
]


def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    index = np.argmax(predictions)
    confidence = round(float(predictions[0][index]) * 100, 2)


    if confidence < 50:
        return "Low confidence – please consult a dermatologist", confidence

    return classes[index], confidence

print(model.output_shape)
