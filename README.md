# 🌾 Rice Grain Classification Using Convolutional Neural Networks (CNN)

An AI-powered computer vision application that automatically classifies rice grain images into five different varieties using a Convolutional Neural Network (CNN) built with TensorFlow and Keras.

## 🚀 Project Overview

Rice grain identification is important in agricultural quality assessment, food processing, and grain quality control.

Traditional manual classification can be time-consuming and subjective.

This project uses deep learning and computer vision to automate rice variety identification by learning visual patterns from rice grain images.

A trained CNN model analyzes uploaded images and predicts the corresponding rice variety through an interactive Streamlit application.

## ✨ Key Features

* CNN-based image classification using TensorFlow/Keras.
* Classification of five rice varieties.
* Image preprocessing and normalization using NumPy and Pillow.
* Interactive image upload interface using Streamlit.
* Real-time prediction with confidence scores.
* Trained models available in HDF5 and Keras formats.
* Jupyter Notebook documenting model development and evaluation.

## 🌾 Rice Varieties

The model classifies images into the following five categories:

1. Arborio
2. Basmati
3. Ipsala
4. Jasmine
5. Karacadag

## 🛠️ Technology Stack

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Core programming language             |
| TensorFlow       | Deep learning framework               |
| Keras            | CNN model implementation              |
| CNN              | Image classification                  |
| NumPy            | Numerical operations                  |
| Pillow           | Image processing                      |
| Streamlit        | Interactive web application           |
| Jupyter Notebook | Model development and experimentation |

## 📂 Project Structure

```text
rice-grain-classification/
│
├── app.py
├── CNN_model.h5
├── cnn_model.keras
├── rice-classification-by-cnn.ipynb
├── requirements.txt
├── Rice_Citation_Request.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/gayathri031024-cmyk/-Computer-Vision-Approach-for-Accurate-Rice-Grain-Classification-using-CNN-.git
```

### 2. Navigate to the project directory

```bash
cd -Computer-Vision-Approach-for-Accurate-Rice-Grain-Classification-using-CNN-
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 🔍 How It Works

1. **Image Upload:** The user uploads a rice grain image through the Streamlit interface.
2. **Preprocessing:** The image is resized to the dimensions expected by the trained CNN model.
3. **Normalization:** Pixel values are normalized before model inference.
4. **Feature Extraction:** The CNN processes the image and learns visual patterns.
5. **Classification:** The model generates prediction probabilities for the five rice varieties.
6. **Result Display:** The application displays the predicted rice variety and confidence score.

## 📊 Model Performance

Model performance should be reported using actual evaluation results.

| Evaluation Metric   | Result         |
| ------------------- | -------------- |
| Training Accuracy   | To be measured |
| Validation Accuracy | To be measured |
| Test Accuracy       | To be measured |
| Precision           | To be measured |
| Recall              | To be measured |
| F1-Score            | To be measured |

*Note: Actual evaluation metrics will be added after verifying the model evaluation results from the training notebook.*

## 📓 Model Development

The Jupyter Notebook `rice-classification-by-cnn.ipynb` contains the model development and experimentation workflow.

It can be used to explore:

* Dataset preparation
* Image preprocessing
* CNN model development
* Model training
* Model evaluation

## 📸 Application Screenshots

Add screenshots of:

* Streamlit application homepage
* Uploaded rice grain image
* Classification prediction
* Prediction confidence

## 🔮 Future Improvements

* Improve classification performance through hyperparameter tuning.
* Add prediction probability visualizations.
* Introduce prediction history.
* Evaluate model performance using a confusion matrix.
* Deploy the application for public access.

## 📚 Dataset Attribution

Dataset source and citation information are provided in `Rice_Citation_Request.txt`.

Please refer to the citation instructions when using or redistributing the dataset.

## 👩‍💻 Author

**Gayathri Virabhathini**

* GitHub: https://github.com/gayathri031024-cmyk
* LinkedIn: https://www.linkedin.com/in/gayathri-virabhathini
* Portfolio: https://portfolio-peach-zeta-32.vercel.app/

---

⭐ If you find this project interesting, consider giving the repository a star.

