# 🥚 EggLift: AI-Powered Egg Color Sorter

EggLift is a robotics and artificial intelligence project designed to **automatically classify and sort eggs** by their shell color—white or brown—using **computer vision**, a **convolutional neural network (CNN)** model, and a **servo-powered robotic arm**.

This solution is designed to enhance productivity and reduce errors in egg sorting, a critical step in poultry farming operations.

---

## 📽 Project Overview

The project integrates:
- **AI & Machine Learning** – for real-time color classification of eggs via a trained CNN model using TensorFlow.
- **OpenCV** – for capturing and processing images through a webcam.
- **Robotics (Servo motors + Arduino)** – for mechanical sorting using a robotic arm and grippers.

---

## 🔍 How It Works

### 🧠 1. AI Egg Detection (Image Classification)
- A webcam captures images of incoming eggs.
- A pretrained **Keras CNN model** (`keras_model.h5`) classifies the egg as either white or brown.
- Prediction is visualized via a live feed and sent for actuation.

> See: [`eggdetectionaicode.py`](./eggdetectionaicode.py)

### 🤖 2. Robotic Sorting with Servo Motors
- Based on the classification, the robotic arm (powered by MG996R servo motors and controlled via Raspberry Pi Pico W) positions the gripper to pick and place the egg into the appropriate tray.
- Servo movements include: base rotation, elbow joint, wrist, and gripper control.

> See: [`SERVO-1.py`](./SERVO-1.py)

---

## 🛠 Hardware Components

| Component                       | Quantity | Notes                          |
|-------------------------------|----------|--------------------------------|
| Arduino Uno / Raspberry Pi Pico W | 1      | Microcontroller                |
| MG996R Servo Motors           | 6        | Robotic arm and gripper joints |
| PCA9685 Servo Driver          | 1        | PWM control                    |
| Webcam                        | 1        | For image input                |
| Plywood + Egg Trays           | -        | Structural base                |

---

## 🧪 Model Performance

| Class       | Precision | Recall | F1-Score |
|-------------|-----------|--------|----------|
| White Egg   | 93.33%    | 96.55% | 94.92%   |
| Brown Egg   | 96.67%    | 93.55% | 95.08%   |
| **Overall Accuracy** | – | – | **95%** |

> Confusion matrix and performance metrics available in the full documentation.

---

## 📄 Full Documentation

Detailed design, testing, methodology, results, and team reflections are available in the official documentation:  
📄 [`G1_Robotics_Capstone-Project_Final.docx`](./G1_Robotics_Capstone-Project_Final.docx)

---

## 🚀 Features

- Real-time color detection using webcam + TensorFlow.
- Automated sorting using microcontroller and servo motors.
- High accuracy (95%) with minimal dataset.
- Cost-effective design using readily available components.
- Sponge-padded gripper to avoid egg breakage.

---

## 📌 Future Improvements

- Expand the image dataset to improve model robustness.
- Replace metal gripper with vacuum or soft gripper.
- Integrate a user-friendly GUI for interaction.
- Upgrade servo motors for better stability and durability.

---

## 👨‍💻 Contributors

- Ian Azaña  
- Jeff Alfred Capa  
- Alliah Marie Cardenas  
- Gabryel Clain Golpeo  
- Rizzel Elyssa Ygan  
- Shemuel Josh Verana

---

## 📜 License

This project is part of a capstone course in Robotics Technology under the Electronics Engineering Department at **Polytechnic University of the Philippines**.

---

