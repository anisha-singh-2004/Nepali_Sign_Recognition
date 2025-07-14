# 🧠 Nepali Sign Recognition

A computer vision system for recognizing Nepali Sign Language (NSL) gestures using machine learning. This project is designed to support real-time gesture recognition using webcam input and is trained on the NSL23 dataset.

---

## 🎯 Overview

This project aims to facilitate the recognition of Nepali Sign Language by:

- Using keypoint extraction (e.g., via MediaPipe) or CNN-based image classification.
- Training custom models on the NSL23 dataset.
- Providing real-time inference via webcam or static images.

---

## 🧩 Project Structure

```

Nepali\_Sign\_Recognition/
├── data/                    # Contains NSL23 and processed data
│   └── NSL23/               # Raw dataset
│   └── processed/           # Preprocessed dataset
├── notebooks/               # Jupyter notebooks for analysis & experiments
├── src/
│   ├── data\_loader.py       # Data preprocessing and loading utilities
│   ├── model.py             # Model architecture
│   ├── train.py             # Training pipeline
│   ├── evaluate.py          # Evaluation script
│   └── infer.py             # Inference and demo interface
├── models/                  # Saved model checkpoints
├── requirements.txt         # Required Python packages
├── README.md                # Project description and usage
└── LICENSE

````

---

## 📦 Dataset: NSL23

We use the **NSL23 Dataset**, a publicly available dataset of Nepali sign language gestures.

📂 **Download/Clone Dataset**  
```bash
git clone https://github.com/anisha-singh-2004/NSL23.git data/NSL23
````

📘 Dataset Repository: [NSL23 Dataset on GitHub](https://github.com/anisha-singh-2004/NSL23)

---

## 🛠️ Setup & Installation

### Requirements

* Python 3.8 or above
* pip (Python package installer)

### Installation

```bash
git clone https://github.com/anisha-singh-2004/Nepali_Sign_Recognition.git
cd Nepali_Sign_Recognition
pip install -r requirements.txt
```

---

## 🧼 Data Preprocessing

Before training, convert the raw images into a structured format or extract keypoints.

```bash
python src/data_loader.py \
  --input_dir data/NSL23 \
  --output_dir data/processed
```

---

## 🧠 Training the Model

Train the sign recognition model on the processed dataset:

```bash
python src/train.py \
  --data_dir data/processed \
  --epochs 20 \
  --batch_size 32 \
  --learning_rate 0.001 \
  --model_out models/sign_model.pth
```

---

## 📊 Evaluation

Evaluate model performance using accuracy and confusion matrix:

```bash
python src/evaluate.py \
  --model_path models/sign_model.pth \
  --data_dir data/processed
```

---

## 🎥 Real-time Inference

### Inference on Image:

```bash
python src/infer.py \
  --model_path models/sign_model.pth \
  --input example.jpg
```

### Webcam Inference:

```bash
python src/infer.py \
  --model_path models/sign_model.pth \
  --webcam
```

---

## 📈 Results

| Metric                | Value (example) |
| --------------------- | --------------- |
| Accuracy              | 91.5%           |
| Inference Speed (CPU) | \~12 FPS        |
| Inference Speed (GPU) | \~38 FPS        |

---

## 🔭 Future Work

* Expand to dynamic signs and full sentence prediction.
* Build a translation system from signs to text or speech.
* Deploy to mobile (Android/iOS) using TensorFlow Lite or ONNX.

---

## 📚 References

* [NSL23: Nepali Sign Language Dataset](https://github.com/anisha-singh-2004/NSL23)
* [MediaPipe](https://mediapipe.dev/)
* [OpenHands: Sign Language Recognition for Low-Resource Languages](https://arxiv.org/abs/2110.05877)


---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


