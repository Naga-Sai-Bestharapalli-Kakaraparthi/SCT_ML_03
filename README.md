# SCT_ML_03
SCT_TrackCode_3
🐶🐱 Dog vs. Cat Image Classification Using Support Vector Machine (SVM) 📌 Project Overview This project implements a binary image classification model that accurately distinguishes between grayscale images of cats and dogs using a Support Vector Machine (SVM) with a linear kernel. Through efficient image preprocessing and classical machine learning, the project showcases a foundational approach to image recognition tasks.

🎯 Objective The primary goal is to build a robust classifier that can effectively differentiate between cat and dog images based on pixel-level features. The model is developed using:

Image preprocessing: grayscale conversion, resizing, and flattening.

SVM model training for high-accuracy classification.

Performance evaluation using metrics such as accuracy, confusion matrix, and F1-score.

🧠 Core Concepts Supervised Learning: Leveraging labeled data to train a predictive model.

Support Vector Machine (SVM): A powerful linear classifier that identifies the optimal decision boundary.

Image Preprocessing: Standardizing image input via grayscale conversion, resizing, and feature vector generation.

Model Evaluation: Using accuracy, precision, recall, and F1-score to measure model effectiveness.

🛠️ Tools & Technologies Tool Purpose Python Core programming language Scikit-learn SVM modeling and evaluation metrics OpenCV (cv2) Image loading, grayscale conversion, resizing NumPy Numerical operations and array manipulation Matplotlib Visualization of images and results

📂 Dataset Overview Dataset Name: Microsoft Cats vs. Dogs

Source: [Microsoft Research] or [Kaggle Mirror]

Description: A labeled dataset of thousands of cat and dog images used for binary classification.

Structure:

📁 PetImages/Cat/ – Images labeled as Cat (0)

📁 PetImages/Dog/ – Images labeled as Dog (1)

Format: JPEG images with varying resolutions

🔄 Project Workflow

Data Loading Load images from respective folders using OpenCV.
Assign labels based on directory names.

Image Preprocessing Convert images to grayscale to reduce color complexity.
Resize all images to a fixed dimension (e.g., 64x64 pixels) for uniformity.

Flatten each image into a 1D array to form feature vectors.

Feature Extraction Use pixel intensity values as features.
Normalize the pixel values (e.g., scale to [0, 1]) to stabilize learning.

Model Training Split dataset into training and testing sets (e.g., 80/20 split).
Train an SVM classifier with a linear kernel.

Tune hyperparameters (e.g., C value) using grid search if necessary.

Model Evaluation Evaluate using:
✅ Accuracy

✅ Precision

✅ Recall

✅ F1-Score

✅ Confusion Matrix

Analyze performance on unseen data.

Visualization Display:
Sample input images with predicted labels

Confusion matrix heatmap for model performance insight

📈 Outcome The final model effectively classifies grayscale images of dogs and cats with competitive accuracy, showcasing the power of classical machine learning methods in image-based classification tasks.
