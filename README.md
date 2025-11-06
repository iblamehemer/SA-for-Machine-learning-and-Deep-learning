# SA-for-Machine-learning-and-Deep-learning

# ♻️ SmartWasteAI – Intelligent Waste Segregation Assistant

## 📘 Overview
**SmartWasteAI** is a deep learning–based image classification project designed to assist smart cities with **automated waste segregation**.  
It uses a **MobileNetV2 CNN model** to identify the type of waste (plastic, glass, metal, cloth, battery, etc.) and recommends the **correct color-coded disposal bin** through a simple **Streamlit web app**.

This project was built as part of the **Machine Learning & Deep Learning (AI) Summative Assessment (2025)** at **UGdam School**, authored by **Hemer Pandya**.

---

## 🧠 Project Objective
Inaccurate waste segregation leads to environmental and recycling inefficiencies.  
This project demonstrates how **computer vision** can classify waste materials from images and suggest the correct bin using a **trained neural network model**.

| Waste Type | Recommended Bin | Color |
|-------------|-----------------|--------|
| Biodegradable | Organic Waste | 🟩 Green |
| Recyclable | Plastic, Glass, Metal | 🟦 Blue |
| Hazardous | Batteries, E-waste | 🟥 Red |

---

## ⚙️ Model Development

### 1. Data Preparation
- Dataset: ~1500 labeled images from five categories  
- Structure:
