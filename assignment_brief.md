# Assignment Context (from course brief)

This project is for the course **Machine Learning and Deep Learning** (Artificial Intelligence) and corresponds to the summative assessment (60 marks). The assignment asks students to pick one of two scenarios. This repository implements **Scenario 1: Computer Vision-based Waste Segregation System for Smart Cities**.

## Scenario 1 Summary
- Organisation: EcoLogic / EcoCity Solutions (smart city tech startup)
- Problem: incorrect waste segregation at collection centers reduces recycling and increases landfill usage.
- Goal: build an intelligent image-based waste classification system that identifies waste type and recommends the correct color-coded bin.
- Target bin colors (typical):
  - Green – Biodegradable
  - Blue – Recyclable
  - Red – Hazardous

## Steps from the brief

1. **Understand the Problem and Define Requirements**
   - Learn waste types: biodegradable, recyclable, hazardous.
   - Map waste → bin color.
   - Define input (image) and output (waste type + bin + confidence).
   - Explain smart city relevance.

2. **Data Collection and Preprocessing**
   - Use the dataset shared in the drive (garbage items, ~10 classes: plastic, glass, metal, clothes, shoes…).
   - Use ~100 images per class.
   - Resize to 224x224.
   - Apply augmentation (rotation, flip, zoom, brightness).
   - Split into 70% train, 15% validation, 15% test.
   - Organize folders per class.

3. **Model Development**
   - Use YOLOv5/YOLOv8 for detection OR MobileNet/EfficientNet for classification.
   - Evaluate using accuracy and confusion matrix.

4. **Integration and Bin Recommendation Logic**
   - After classification, recommend bin based on category.
   - Show prediction label + confidence.

5. **Web App Development using Streamlit**
   - Show uploaded image.
   - Show detected/predicted waste item.
   - Show bin recommendation.
   - Keep UI clean and responsive.

6. **Testing and Feedback**
   - Test on unseen images, different lighting/backgrounds.
   - Collect feedback from users.

7. **Deployment on Streamlit Cloud**
   - Push repo to GitHub.
   - Deploy on Streamlit Cloud.
   - Share public link.

## Evidence Checklist (to put in your PDF submission)
- GitHub link (with access for `ai.assignments@wacpinternational.org`)
- Student full name
- Candidate registration number
- CRS name: Artificial Intelligence
- Course name: Machine Learning and Deep Learning
- School name
- Live Streamlit app link

## Rubric Mapping (60 marks)
- Understanding the problem & requirements – 5
- Data collection & preprocessing – 10
- Model development – 10
- System logic & integration (bin logic) – 10
- Testing, deployment & accessibility – 10
- GitHub repo & documentation – 5