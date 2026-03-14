import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("CNN_model.h5")
    return model

model = load_model()

# -----------------------------
# Get input size from model
# -----------------------------
img_height = model.input_shape[1]
img_width = model.input_shape[2]

# -----------------------------
# Define Rice Classes
# -----------------------------
labels = [
    "Arborio",
    "Basmati",
    "Ipsala",
    "Jasmine",
    "Karacadag"
]

# -----------------------------
# Image Preprocessing Function
# -----------------------------
def preprocess_image(image):

    image = image.resize((img_width, img_height))
    image = np.array(image)

    # Remove alpha channel if present
    if image.shape[-1] == 4:
        image = image[:, :, :3]

    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    return image

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Rice Grain Classification using CNN")

st.write("Upload a rice grain image to identify the rice variety.")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = preprocess_image(image)

    prediction = model.predict(img)

    predicted_class = labels[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.success(f"Predicted Rice Type: {predicted_class}")

    st.write(f"Confidence: {confidence:.2f}")