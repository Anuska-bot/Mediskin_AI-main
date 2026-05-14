
Mediskin AI – Skin Disease Detection System

Project Overview---
Mediskin AI is a deep learning–based skin disease detection system that classifies skin images into different disease categories using Convolutional Neural Networks (CNNs).
The project aims to assist in early screening by automatically analyzing skin images and predicting the most likely skin condition.

This project is developed as part of the Infosys Internship Program.

Objectives--
1.Build an end-to-end machine learning pipeline for skin disease classification
2.Perform dataset preparation, cleaning, and preprocessing
3.Train and validate a CNN model using transfer learning
4.Evaluate model performance using standard classification metrics
5.Save and reuse the trained model for inference and deployment

Dataset Details
Source:  https://drive.google.com/drive/folders/1BADFBR8cJ_7650pICWDU30LBfb1a9h4z?usp=sharing
Classes: Multiple skin conditions such as Acne, Eczema, Melanoma, Psoriasis, Normal, etc.
Image Format: JPG / PNG
Image Size: Resized to 224 × 224
Color Mode: RGB

Dataset Split
Training: 70%
Validation: 15%
Testing: 15%
Class distribution was preserved during splitting.

Data Preprocessing & Cleaning (Milestone-1)

Removed corrupted images

Removed duplicate images

Organized images into class-wise folders

Normalized image pixel values (0–1)

Resized images to 224×224

Applied data augmentation:

Rotation

Horizontal flip

Zoom

Width & height shift

Model Architecture (Milestone-2)
Approach

Transfer Learning using MobileNetV2

Pretrained on ImageNet

Custom classification head added on top

Architecture Components

MobileNetV2 (feature extractor)

Global Average Pooling

Batch Normalization

Dense layer (ReLU)

Dropout (to reduce overfitting)

Softmax output layer

Model Training
Framework: TensorFlow / Keras
Optimizer: Adam
Loss Function: Categorical Crossentropy
Batch Size: 32
Image Size: 224×224×3
Fine-tuning: Top layers of MobileNetV2 unfrozen for better learning

Model Evaluation
Test Accuracy
Final Test Accuracy: ~65.8%
Evaluation Metrics
Accuracy
Precision
Recall
F1-Score

A confusion matrix was generated to analyze class-wise performance and identify misclassification patterns.

Performance Note

Due to class imbalance and visual similarity between certain skin diseases, the model performance is limited by dataset quality.
Further improvements can be achieved using a larger, more balanced dataset or domain-specific pretrained models.

Model Saving

The best-performing trained model was saved in reusable format:
models/skin_disease_model.keras
This model can be directly loaded for inference or deployment.

Testing with Unseen Images
The trained model was tested on unseen skin images to verify real-world inference capability.

Project Structure
Mediskin_AI/
│
├── app/
│   ├── app.py
│   ├── model_predict.py
│   ├── auth.db
│   ├── static/
│   │   ├── style.css
│   │   ├── uploads/
│   │   └── images/
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── predict.html
│       └── result.html
│
├── models/
│   └── skin_disease_model.keras
│
├── notebooks/
│   ├── model_training.ipynb
│   └── dataset_exploration.ipynb
│
├── dataset/
│   └── raw/
│
├── requirements.txt
└── README.md

Features

User Registration & Login (Session-based authentication)
Skin Image Upload (JPG / PNG)
AI-based Skin Disease Prediction
Confidence Score for Predictions
Hospital Recommendations based on Location
Clean, Professional, Healthcare-friendly UI
Medical Disclaimer for Responsible Usage

Technologies Used
Frontend
HTML
CSS
Jinja2 (Template Engine)

Backend
Python
Flask (Web Framework)
Machine Learning
TensorFlow / Keras
Convolutional Neural Network (CNN)
Database
SQLite (for user authentication)

🧩 System Workflow
User Authentication
Users register and log in securely using email and password.

Dashboard
After login, users access a dashboard explaining the system and navigation options.

Image Upload
Users upload a clear image of the affected skin area and select their location.

Image Preprocessing
The image is resized, normalized, and converted into an array suitable for the ML model.

Prediction
The trained CNN model predicts the skin disease and calculates a confidence score.

Result Display
The predicted condition, confidence score, and nearby hospital recommendations are displayed.



Author
Anuska

Mediskin AI – Skin Disease Detection System

Project Overview---
Mediskin AI is a deep learning–based skin disease detection system that classifies skin images into different disease categories using Convolutional Neural Networks (CNNs).
The project aims to assist in early screening by automatically analyzing skin images and predicting the most likely skin condition.

This project is developed as part of the Infosys Internship Program.

Objectives--
1.Build an end-to-end machine learning pipeline for skin disease classification
2.Perform dataset preparation, cleaning, and preprocessing
3.Train and validate a CNN model using transfer learning
4.Evaluate model performance using standard classification metrics
5.Save and reuse the trained model for inference and deployment

Dataset Details
Source: Kaggle (Skin Disease Image Dataset)
Classes: Multiple skin conditions such as Acne, Eczema, Melanoma, Psoriasis, Normal, etc.
Image Format: JPG / PNG
Image Size: Resized to 224 × 224
Color Mode: RGB

Dataset Split
Training: 70%
Validation: 15%
Testing: 15%
Class distribution was preserved during splitting.

Data Preprocessing & Cleaning (Milestone-1)

Removed corrupted images

Removed duplicate images

Organized images into class-wise folders

Normalized image pixel values (0–1)

Resized images to 224×224

Applied data augmentation:

Rotation

Horizontal flip

Zoom

Width & height shift

Model Architecture (Milestone-2)
Approach

Transfer Learning using MobileNetV2

Pretrained on ImageNet

Custom classification head added on top

Architecture Components

MobileNetV2 (feature extractor)

Global Average Pooling

Batch Normalization

Dense layer (ReLU)

Dropout (to reduce overfitting)

Softmax output layer

Model Training
Framework: TensorFlow / Keras
Optimizer: Adam
Loss Function: Categorical Crossentropy
Batch Size: 32
Image Size: 224×224×3
Fine-tuning: Top layers of MobileNetV2 unfrozen for better learning

Model Evaluation
Test Accuracy
Final Test Accuracy: ~65.8%
Evaluation Metrics
Accuracy
Precision
Recall
F1-Score

A confusion matrix was generated to analyze class-wise performance and identify misclassification patterns.

Performance Note

Due to class imbalance and visual similarity between certain skin diseases, the model performance is limited by dataset quality.
Further improvements can be achieved using a larger, more balanced dataset or domain-specific pretrained models.

Model Saving

The best-performing trained model was saved in reusable format:
models/skin_disease_model.keras
This model can be directly loaded for inference or deployment.

Testing with Unseen Images
The trained model was tested on unseen skin images to verify real-world inference capability.

Project Structure
Mediskin_AI/
│
├── app/
│   ├── app.py
│   ├── model_predict.py
│   ├── auth.db
│   ├── static/
│   │   ├── style.css
│   │   ├── uploads/
│   │   └── images/
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── predict.html
│       └── result.html
│
├── models/
│   └── skin_disease_model.keras
│
├── notebooks/
│   ├── model_training.ipynb
│   └── dataset_exploration.ipynb
│
├── dataset/
│   └── raw/
│
├── requirements.txt
└── README.md

Features

User Registration & Login (Session-based authentication)
Skin Image Upload (JPG / PNG)
AI-based Skin Disease Prediction
Confidence Score for Predictions
Hospital Recommendations based on Location
Clean, Professional, Healthcare-friendly UI
Medical Disclaimer for Responsible Usage

Technologies Used
Frontend
HTML
CSS
Jinja2 (Template Engine)

Backend
Python
Flask (Web Framework)
Machine Learning
TensorFlow / Keras
Convolutional Neural Network (CNN)
Database
SQLite (for user authentication)

🧩 System Workflow
User Authentication
Users register and log in securely using email and password.

Dashboard
After login, users access a dashboard explaining the system and navigation options.

Image Upload
Users upload a clear image of the affected skin area and select their location.

Image Preprocessing
The image is resized, normalized, and converted into an array suitable for the ML model.

Prediction
The trained CNN model predicts the skin disease and calculates a confidence score.

Result Display
The predicted condition, confidence score, and nearby hospital recommendations are displayed.



Author
Anuska
