# 🤟 Sign Language Recognition System

A real-time **Sign Language Recognition System** built using **Python, OpenCV, MediaPipe, and Machine Learning**. This project detects hand gestures through a webcam, extracts 21 hand landmarks, and uses a trained **Random Forest Classifier** to recognize sign language gestures in real time. The project follows a modular, phase-wise development approach and demonstrates the practical application of Computer Vision and Machine Learning.

---

# 📌 Project Overview

This project is designed to recognize static hand gestures of the **American Sign Language (ASL)** alphabet. Instead of training directly on images, the system uses **MediaPipe** to extract **21 hand landmarks (63 features)** from each image and trains a **Random Forest** model for fast and accurate predictions.

---

# 🚀 Features

- ✅ Real-time Hand Detection
- ✅ Finger Counting
- ✅ Hand Landmark Detection (21 Landmarks)
- ✅ MediaPipe Hand Tracking
- ✅ ASL Alphabet Dataset Integration
- ✅ Automatic Landmark Extraction
- ✅ Automatic CSV Dataset Generation
- ✅ Feature Extraction (63 Features)
- ✅ Random Forest Model Training
- ✅ Model Evaluation
- ✅ Model Serialization using Joblib
- ✅ Real-Time Sign Language Prediction
- ✅ Live Webcam Recognition
- ✅ Modular Phase-wise Project Structure

---

# 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Kaggle ASL Alphabet Dataset

---

# 📂 Project Structure

```
Sign_recognition_system/
│
├── phase_1.py
├── phase_2.py
├── phase_3.py
├── phase_4.py
├── phase_5.py
├── phase_6.py
│
├── dataset.csv
├── sign_model.pkl
├── requirements.txt
├── README.md
│
├── asl_alphabet_train/
│   ├── A/
│   ├── B/
│   ├── C/
│   ├── ...
│   ├── Z/
│   ├── del/
│   ├── nothing/
│   └── space/
│
└── asl_alphabet_test/
```

---

# 📖 Development Phases

## ✅ Phase 1 – Hand Detection

Implemented real-time hand detection using **MediaPipe Hands** and OpenCV. The system captures webcam frames, detects the user's hand, and visualizes all 21 hand landmarks.

### Concepts Learned

- OpenCV Webcam
- MediaPipe Hands
- RGB Conversion
- Hand Detection
- Landmark Tracking

---

## ✅ Phase 2 – Finger Counter

Built a finger counting system using MediaPipe landmarks. The project detects open and closed fingers based on landmark positions.

### Concepts Learned

- Finger Tip IDs
- Landmark Coordinates
- Thumb Detection
- Finger Counting Logic
- Multi-Hand Support

---

## ✅ Phase 3 – Dataset Preparation

Prepared the **ASL Alphabet Dataset** from Kaggle for machine learning. The dataset contains labeled images for A–Z and additional gesture classes.

### Dataset Used

- ASL Alphabet Dataset (Kaggle)

---

## ✅ Phase 4 – Landmark Extraction & Dataset Generation

Developed an automated preprocessing pipeline that reads every image from the ASL dataset, detects the hand using MediaPipe, extracts **21 hand landmarks (63 features)**, and generates a structured **dataset.csv** file.

### Workflow

```
ASL Images
      ↓
MediaPipe
      ↓
21 Hand Landmarks
      ↓
63 Features
      ↓
dataset.csv
```

---

## ✅ Phase 5 – Machine Learning Model Training

Trained a **Random Forest Classifier** using the extracted landmark dataset.

### Workflow

```
dataset.csv
      ↓
Train/Test Split
      ↓
Random Forest
      ↓
Model Evaluation
      ↓
sign_model.pkl
```

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## ✅ Phase 6 – Real-Time Sign Recognition

Loaded the trained model and performed real-time sign prediction using a webcam. The system continuously detects hand landmarks and predicts the corresponding ASL sign.

### Workflow

```
Webcam
      ↓
MediaPipe
      ↓
21 Hand Landmarks
      ↓
63 Features
      ↓
Random Forest Model
      ↓
Predicted Sign
```

---

# 📊 Machine Learning Pipeline

```
ASL Alphabet Dataset
            │
            ▼
Image Processing
            │
            ▼
MediaPipe Hand Detection
            │
            ▼
21 Hand Landmarks
            │
            ▼
63 Features
            │
            ▼
dataset.csv
            │
            ▼
Random Forest Training
            │
            ▼
sign_model.pkl
            │
            ▼
Real-Time Prediction
```

---

# 🧠 Hand Landmark Information

MediaPipe detects **21 landmarks** for each hand.

| Landmark | Description |
|-----------|-------------|
| 0 | Wrist |
| 4 | Thumb Tip |
| 8 | Index Finger Tip |
| 12 | Middle Finger Tip |
| 16 | Ring Finger Tip |
| 20 | Pinky Finger Tip |

Each landmark consists of:

- X Coordinate
- Y Coordinate
- Z Coordinate

Total Features:

```
21 Landmarks × 3 Coordinates = 63 Features
```

---

# 🤖 Machine Learning

### Algorithm Used

- Random Forest Classifier

### Dataset

- ASL Alphabet Dataset (Kaggle)

### Input

- 63 Landmark Features

### Output

- Predicted ASL Sign

---

# 📊 Results

- ✅ Successfully detected hands in real time.
- ✅ Extracted 21 hand landmarks from ASL images.
- ✅ Generated a structured landmark dataset.
- ✅ Trained a Random Forest classifier.
- ✅ Performed real-time sign prediction using a webcam.

---

# 💻 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Sign_recognition_system.git
```

Navigate to the project directory:

```bash
cd Sign_recognition_system
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run each phase individually:

### Phase 1

```bash
python phase_1.py
```

### Phase 2

```bash
python phase_2.py
```

### Phase 3

Prepare the ASL Alphabet Dataset.

### Phase 4

```bash
python phase_4.py
```

Generates:

```
dataset.csv
```

### Phase 5

```bash
python phase_5.py
```

Generates:

```
sign_model.pkl
```

### Phase 6

```bash
python phase_6.py
```

Starts real-time sign recognition.

---

# 📈 Future Improvements

- Dynamic Sign Recognition
- Word Formation
- Sentence Formation
- Text-to-Speech
- Deep Learning (CNN/LSTM)
- Mobile Application
- Web Deployment
- Multi-language Sign Recognition

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Deepak**

🎓 B.Tech CSE (AI & ML) Student

Passionate about **Artificial Intelligence, Computer Vision, Machine Learning, and Real-World AI Applications.**

---

## ⭐ If you like this project, don't forget to Star the repository!
