import streamlit as st
import numpy as np
import pickle
from PIL import Image
import os

# Definisikan jalur model
model_directory = r'D:\Tugas\Sem 5\Mesin Learning\Introduction to Deep Learning (Praktek)\Introduction to Deep Learning (Praktek)'
model_path = os.path.join(model_directory, r"best_model.pkl")

if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)

        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
            
            # Fungsi untuk memproses gambar
        def preprocess_image(image):
            image = image.resize((28, 28))  # Ubah ukuran menjadi 28x28 piksel
            image = image.convert('L')  # Ubah menjadi grayscale
            image_array = np.array(image) / 255.0  # Normalisasi
            image_array = image_array.reshape(1, -1)  # Flatten ke bentuk 1D array
            return image_array

        st.title("Fashion MNIST Image Classifier - 1745")  # 4 digit npm
        st.write("Unggah beberapa gambar item fashion (misalnya sepatu, tas, baju), dan model akan memprediksi kelas masing-masing.")

        uploaded_files = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

        with st.sidebar:
            st.write("## Navigator")
            predict_button = st.button("Predict")  # Tombol di sidebar

        # Tampilkan hasil prediksi di bawah tombol "Predict"
        if uploaded_files and predict_button:
            st.write("### Hasil Prediksi")

            for uploaded_file in uploaded_files:
                # Buka dan proses setiap gambar
                image = Image.open(uploaded_file)
                processed_image = preprocess_image(image)
                predictions = model.predict_proba(processed_image)
                predicted_class = np.argmax(predictions)
                confidence = np.max(predictions) * 100

                st.write(f"**Nama File:** {uploaded_file.name}")
                st.write(f"**Kelas Prediksi:** {class_names[predicted_class]}")
                st.write(f"**Confidence:** {confidence:.2f}%")
                st.write("---") 

        if uploaded_files:
            for uploaded_file in uploaded_files:
                image = Image.open(uploaded_file)
                st.image(image, caption=f"Gambar: {uploaded_file.name}", use_column_width=True)
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.error("File model tidak ditemukan.") 


