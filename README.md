# 🌾 Computer Vision Approach for Accurate Rice Grain Classification using CNN

A deep learning-based image classification system that leverages **Computer Vision** and a **Convolutional Neural Network (CNN)** to automatically identify and classify rice grains into their respective varieties based on visual features such as shape, size, and texture.

## 📌 Overview

Manual classification of rice grains is time-consuming, labor-intensive, and prone to human error. This project automates the process using a CNN model trained on rice grain images, enabling fast, consistent, and accurate variety classification — useful for agricultural quality control, food industry sorting, and research applications.

## ✨ Features

- 🧠 CNN-based image classification model (`CNN_model.h5` / `cnn_model.keras`)
- 📊 Trained and evaluated using a labeled rice grain image dataset
- 🌐 Interactive **Streamlit web app** (`app.py`) for real-time predictions
- 📓 Jupyter notebook (`rice-classification-by-cnn.ipynb`) detailing the full model development pipeline

## 🗂️ Project Structure

```
├── CNN_model.h5                      # Trained CNN model (HDF5 format)
├── cnn_model.keras                   # Trained CNN model (Keras format)
├── app.py                            # Streamlit application for inference
├── rice-classification-by-cnn.ipynb  # Model training & evaluation notebook
├── Rice_Citation_Request.txt         # Dataset citation/reference
├── requirements.txt                  # Python dependencies
└── README.md
```

## ⚙️ Tech Stack

- **Python**
- **TensorFlow / Keras** – model building and training
- **Streamlit** – web app deployment
- **NumPy, Pandas, Matplotlib** – data handling and visualization

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## 🎯 How It Works

1. Upload a rice grain image via the Streamlit interface.
2. The trained CNN model processes the image and extracts key visual features.
3. The model predicts the rice variety and displays the result with a confidence score.

## 📈 Model Performance

| Metric | Score |
|--------|-------|
| Training Accuracy | _add value_ |
| Validation Accuracy | _add value_ |
| Test Accuracy | _add value_ |
| Precision | _add value_ |
| Recall | _add value_ |
| F1-Score | _add value_ |

> Add a confusion matrix or accuracy/loss curve image here for a stronger visual summary, e.g.:
> `![Accuracy Curve](assets/accuracy_curve.png)`

## 📚 Dataset

Refer to `Rice_Citation_Request.txt` for dataset source and citation details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues).

## 📄 License

This project is open-source. Add your preferred license (MIT, Apache 2.0, etc.).

## 🙌 Acknowledgements

Thanks to the creators of the rice grain image dataset referenced in `Rice_Citation_Request.txt`.
