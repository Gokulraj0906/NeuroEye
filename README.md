# NeuroEye - Brain Tumor Detection using SVM

## Overview
NeuroEye is a powerful machine learning application designed to detect brain tumors using Support Vector Machines (SVM). With an accuracy of 95.68%, NeuroEye offers a reliable and efficient solution for early detection and diagnosis, leveraging cutting-edge technologies like React, JavaScript, Python, and Flask.

## Features
- **Accurate Detection**: Achieves 95.68% accuracy in detecting brain tumors.
- **User-Friendly Interface**: Built with React and JavaScript for an intuitive user experience.
- **Robust Backend**: Utilizes Python and Flask for data processing and server-side operations.
- **Data Preprocessing**: Ensures high-quality data for model training and prediction.

## Technologies Used
- **Frontend**: React, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: Support Vector Machines (SVM)
- **Data Processing**: Pandas, NumPy

## Installation

### Prerequisites
- Node.js and npm
- Python 3.6+
- Flask
- Virtualenv (optional but recommended)

### Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/Gokulraj0906/NeuroEye.git
    cd NeuroEye
    ```

2. **Set up the backend**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    python app.py
    ```

3. **Set up the frontend**
    ```bash
    cd frontend
    npm install
    npm start
    ```

## Usage
- Navigate to the frontend application in your browser (typically `http://localhost:3000`).
- Upload the MRI scan image you want to analyze.
- The application will process the image and display the detection result.

## Contributing
We welcome contributions to NeuroEye! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
For any inquiries or feedback, please contact Gokulraj.S at [gokulraj.ds.ai@gmail.com](mailto:gokulraj.ds.ai@gmail.com).
