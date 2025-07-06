# 🔥 Image Classifier GUI using CNN (ResNet50)

A modern **desktop image classification app** built with **Tkinter GUI** and powered by **ResNet50 (TensorFlow CNN)**. Classify **single images or folders** via upload or drag & drop. Perfect for learners, demos, or fast dataset previews.

---

## 🧠 What Is This?

A deep learning + desktop GUI hybrid that allows anyone to:

- Classify images using **pretrained ResNet50**
- Use drag & drop or upload method
- View predictions with top-3 labels + confidence
- Save and log results in `.txt`
- Batch-classify entire folders

Ideal for:
- Beginners exploring DL with GUIs
- Small desktop tools for dataset inspection
- Quick offline inference testing

---
🧠 How It Works (Internals)
Uses ResNet50 pretrained on ImageNet (1000+ categories)

Image resized to 224x224, preprocessed with Keras utilities

Model returns top 3 predictions + confidence

GUI renders image + prediction results

Classification history maintained in the session and optionally saved

---

## 🏗️ Tech Stack & Libraries

| Layer         | Tech / Library                      |
|--------------|--------------------------------------|
| GUI          | `Tkinter`, `tkinterDnD2`             |
| Image Engine | `PIL (Pillow)`                       |
| Backend      | `TensorFlow`, `Keras`, `ResNet50`    |
| Others       | `os`, `datetime`, `numpy`            |

---

## 🚀 Features

- ✅ Drag & Drop Support
- ✅ Upload Single Image or Entire Folder
- ✅ Top-3 Predictions with Accuracy %
- ✅ Batch Classification with Scrollable Display
- ✅ Save Classification History to `.txt`
- ✅ Timestamped History Log
- ✅ Keyboard Shortcuts
- ✅ Reset / Clear Display Options
- ✅ Fully Offline Desktop Inference

---

## 📐 Architecture Diagram

           +-----------------------------+
           |        User Interface       |
           |  (Tkinter GUI + Drag/Drop)  |
           +-------------+---------------+
                         |
                         v
          +--------------+---------------+
          |        Image Classifier       |
          |  (Preprocess + ResNet50 CNN)  |
          +--------------+---------------+
                         |
        +----------------+----------------+
        |                                 |
 +------+-------+              +----------+---------+
 | Image Display |             | Classification Log |
 +--------------+              +---------------------+







