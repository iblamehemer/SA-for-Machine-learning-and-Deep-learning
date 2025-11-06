import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from bin_logic import map_class_to_bin  # this is from the project I gave you

st.set_page_config(page_title="SmartWasteAI", page_icon="🗑️", layout="centered")
st.title("SmartWasteAI – Waste Segregation Assistant")
st.write("Upload a waste image and I'll tell you which bin to use.")

# 1) load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("models/waste_classifier.h5")
    return model

model = load_model()

# 2) this MUST match your training print:
# Class indices: {'battery': 0, 'cloth': 1, 'glass': 2, 'metal': 3, 'plastic': 4}
CLASS_NAMES = ["battery", "cloth", "glass", "metal", "plastic"]

uploaded_file = st.file_uploader("Upload a waste image", type=["jpg", "jpeg", "png"])

def predict_image(img_array):
    preds = model.predict(img_array)
    idx = np.argmax(preds, axis=1)[0]
    conf = float(np.max(preds))
    return CLASS_NAMES[idx], conf

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # preprocess like training
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predicted_class, confidence = predict_image(img_array)

    st.subheader("Prediction")
    st.write(f"**Waste Type:** {predicted_class}")
    st.write(f"**Confidence:** {confidence*100:.2f}%")

    # map to bin
    bin_rec = map_class_to_bin(predicted_class)
    st.success(f"Recommended Bin: {bin_rec}")
else:
    st.warning("Please upload an image to proceed.")