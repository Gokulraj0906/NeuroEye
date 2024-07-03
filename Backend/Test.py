from joblib import load
import cv2
import numpy as np

# Load the pre-trained SVM model
model = load('G:\\Projects\\NeroBird\\types_of_Brain_tumor_SVM.joblib')

# Path to the input image
input_img_path = 'G:\\Projects\\NeroBird\\Dataset\\pituitary\\Tr-pi_0010.jpg'

# Read, preprocess, and flatten the input image
input_img = cv2.imread(input_img_path)
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
input_img = cv2.resize(input_img, (64, 64))

# Flatten and reshape the image for prediction
input_img = input_img.flatten().reshape(1, -1)

# Predict the label for the input image
prediction = model.predict(input_img)

# Define the correct label mapping
label_map = {0: 'No Tumor', 1: 'Glioma', 2: 'Meningioma', 3: 'Pituitary'}

# Get the predicted label
predicted_label = label_map[prediction[0]]

# Print the prediction result
print(f"Prediction for the input image: {predicted_label}")
