import tensorflow as tf
import numpy as np

def load_trained_model(model_path: str):
    model = tf.keras.models.load_model(model_path)
    return model

def predict_image(model, img_array: np.ndarray):
    preds = model.predict(img_array)
    class_idx = np.argmax(preds, axis=1)[0]
    confidence = float(np.max(preds))
    # you must define this list according to your dataset classes
    classes = ["organic", "plastic", "glass", "metal", "battery", "cloth"]
    predicted_class = classes[class_idx]
    return predicted_class, confidence