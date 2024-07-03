from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)  # Add CORS support for cross-origin requests

# Load the pre-trained SVM model (assuming it's in the same directory)
model = load('Brain_tumor_SVM_model.joblib')

# Define the label mapping
label_map = {0: 'No Tumor', 1: 'Glioma', 2: 'Meningioma', 3: 'Pituitary'}


@app.route('/', methods=['POST'])
def predict_tumor():
    """Predicts the tumor class from an uploaded image."""
    if 'file' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    try:
        # Read the image from the request
        file = request.files['file']
        input_img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Error handling: Check if image is valid
        if input_img is None:
            return jsonify({'error': 'Invalid image format'}), 400

        # Preprocess the image
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
        input_img = cv2.resize(input_img, (64, 64))  # Maintain aspect ratio for better accuracy

        # Flatten and reshape the image for prediction
        input_img = input_img.flatten().reshape(1, -1)

        # Predict the tumor class
        prediction = model.predict(input_img)
        predicted_label = label_map[prediction[0]]

        # Return the prediction result in JSON format
        return jsonify({'prediction': predicted_label})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
