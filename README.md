# 🚀 Face Recognition using KNN & OpenCV

## 📌 Overview
This project implements **real-time face recognition** using **K-Nearest Neighbors (KNN)** and **OpenCV** in Python. It captures live video, detects faces, and recognizes them with high accuracy by storing facial data along with names.

## 🎯 Features
- 🔍 **Real-time face detection**
- 🧠 **Face recognition using KNN**
- 📷 **Live webcam feed integration**
- 🗂️ **Stores face data with names for recognition**
- 📁 **Custom dataset training**
- 📊 **Optimized for accuracy and speed**

## 🛠️ Technologies Used
- 🐍 **Python**
- 👁️ **OpenCV**
- 🤖 **K-Nearest Neighbors (KNN)**
- 📊 **NumPy & Pandas**

## ⚡ Installation
1️⃣ Clone the repository:
```bash
git clone https://github.com/your-username/face-recognition-knn.git
cd face-recognition-knn
```

2️⃣ Install dependencies:
```bash
pip install opencv-python numpy pandas
```

## 🗃️ Data Storage
- The system stores each detected face along with the corresponding name.
- The dataset is saved in a structured format (e.g., `.npy` or `.csv`).
- The stored data is used for training and recognition.

## 🚀 How to Run
1️⃣ Collect training images and store them in a dataset folder.

2️⃣ Run the data collection script to store faces with names:
```bash
python collect_faces.py
```

3️⃣ Train the model:
```bash
python train.py
```

4️⃣ Start live face recognition:
```bash
python recognize.py
```

## 📸 Demo
![Demo](https://your-demo-link.com/demo.gif)


![Screenshot 2025-03-28 190002](https://github.com/user-attachments/assets/bb8e492a-135c-4af7-bfae-0b4521c3c4ed)
![Screenshot 2025-03-28 190545](https://github.com/user-attachments/assets/22421579-6db8-44a8-9c5b-4952daf6b309)
![Screenshot 2025-03-28 190158](https://github.com/user-attachments/assets/8939f163-7315-4086-b023-54c857cc3db3)
![Screenshot 2025-03-28 190417](https://github.com/user-attachments/assets/ddf3a272-1ceb-451a-bf10-ecbc53ee5c7a)
![Screenshot 2025-03-28 190311](https://github.com/user-attachments/assets/9ece9f81-6ec0-4805-92e8-5b78dbedc1d4)


## 🏆 Results
- Results achieved using KNN for face classification.
- Stores and retrieves faces efficiently for recognition.
- Works well in **real-time environments** with minimal lag.

