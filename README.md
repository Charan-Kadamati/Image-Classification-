
# 🔥 Image Classifier GUI using CNN (ResNet50)

A modern **desktop image classification app** built with **Tkinter GUI** and powered by **ResNet50 (TensorFlow CNN)**. Classify **single images or folders** via upload or drag & drop. Perfect for learners, demos, or fast dataset previews.

---

## 🧠 What Is This?

A deep learning + desktop GUI hybrid that allows anyone to:

- 🖼️ Classify images using **pretrained ResNet50**
- 📂 Use drag & drop or upload method
- 📊 View predictions with top-3 labels + confidence
- 💾 Save and log results in `.txt`
- 🗃️ Batch-classify entire folders

Ideal for:

- 👶 Beginners exploring DL with GUIs  
- 🔍 Small desktop tools for dataset inspection  
- ⚡ Quick offline inference testing

---

## 🧠 How It Works (Internals)

- 🤖 Uses **ResNet50** pretrained on **ImageNet** (1000+ categories)
- 📐 Input images are resized to `224x224`, then preprocessed via Keras
- 🧠 Predictions are decoded into **Top-3 labels + probabilities**
- 🖼 GUI displays images with prediction results and history
- 📝 All classified results are timestamped and optionally saved

---

## 📚 Dataset Used

> This project uses the **ImageNet** dataset *indirectly* via Keras' **ResNet50**:

- 🗂 1.2M training images  
- 🏷️ 1,000 object categories  
- 🧠 Used as a **pre-trained classifier** (no retraining needed)

---

## 🏗️ Tech Stack & Libraries

| 🧩 Layer         | 🛠️ Tech / Library                      |
|------------------|----------------------------------------|
| 🖥 GUI           | `Tkinter`, `tkinterDnD2`               |
| 🖼 Image Engine  | `PIL (Pillow)`                         |
| 🧠 Backend       | `TensorFlow`, `Keras`, `ResNet50`      |
| ⚙️ Others        | `os`, `datetime`, `numpy`              |

---

## 🚀 Features

- 🖼 Drag & Drop Support  
- 📁 Upload Single Image or Entire Folder  
- 📊 Top-3 Predictions with Confidence Scores  
- 🧾 Batch Classification with Scrollable Results  
- 💾 Save Results to `.txt` File  
- 🕒 Timestamped Classification Log  
- ⌨️ Keyboard Shortcuts (`Ctrl+O`, `Ctrl+S`, `Ctrl+Shift+F`)  
- ♻️ Clear & Reset Display Options  
- 📴 Fully Offline – No Internet Required

---

## 📐 Architecture Diagram

> 🧠 ResNet50-based Pretrained CNN Pipeline

![Architecture Diagram](https://github.com/user-attachments/assets/209330ff-4bb5-4de3-b860-4a18f233cc7b)

---
## 🌐 Screenshots
![Screenshot 2025-07-06 230459](https://github.com/user-attachments/assets/edac7c5e-8aeb-42a7-b0f5-1eed56df7368)

---

## 🏁 How to Run

### 📦 Install Dependencies

```bash
pip install tensorflow pillow tkinterdnd2
```

For tkinterDnD2 issues on Windows:

```bash
pip install git+https://github.com/pmgagne/tkinterdnd2.git
```

---

### ▶️ Run the App

```bash
python gui_app.py
```

---

## 👨‍💻 Author

**K.V.M Sri Charan**  
📍 India | ✨ ML Explorer | 🧠 AI Enthusiast
🔗 https://www.linkedin.com/in/sri-charan-702885340/

---

## 📄 License

MIT License'

#tags: tkinter cnn keras resnet50 gui image-classification deep-learning desktop-app python
