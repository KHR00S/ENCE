import streamlit as st
import numpy as np
from PIL import Image
import onnxruntime as ort


# Load the ONNX model
onnx_model_path = 'best1.onnx'
onnx_session = ort.InferenceSession(onnx_model_path)

# Define class labels
class_labels = ['Fire', 'None', 'Smoke', 'Smoke and Fire']

# Function to preprocess image
def preprocess_image(image):
    # Resize image to (416, 416)
    image = image.resize((512, 512))
    # Convert image to numpy array
    img_array = np.array(image)
    # Transpose array to (channels, height, width)
    img_array = np.transpose(img_array, (2, 0, 1))
    # Normalize pixel values
    img_array = img_array.astype(np.float32) / 255.0
    return img_array

# Function to classify image
def classify_image(image):
    # Preprocess image
    img_array = preprocess_image(image)
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Perform inference
    input_name = onnx_session.get_inputs()[0].name
    output_name = onnx_session.get_outputs()[0].name
    classes = onnx_session.run([output_name], {input_name: img_array})[0]
    predicted_class_index = np.argmax(classes)
    # Get the predicted label and confidence
    predicted_label = class_labels[predicted_class_index]
    confidence = classes[0][predicted_class_index]
    return predicted_label, confidence

# Main Streamlit app
def app():
    #title
    st.title("Pemanfaatan Big Data untuk Aksi Iklim: Klasifikasi Gambar Kebakaran Hutan dalam Kompetisi Big Data Competition Statistics Explore 2024")
    st.write("")

    # Upload image
    uploaded_image = st.file_uploader("Silakan upload gambar untuk dianalisis:", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Gambar yang Diunggah', use_column_width=True)

        # Button to classify image
        classify_button = st.button("Klasifikasi Gambar")

        if classify_button:
            try:
                # Classify the uploaded image
                predicted_label, confidence = classify_image(image)
                # Display the prediction
                st.write(f"Prediksi: {predicted_label} (Kepercayaan: {confidence:.2f})")
            except Exception as e:
                st.write(f"An error occurred: {e}")

# Ensure the script can be run directly or imported as a module
if __name__ == "__main__":
    app()
