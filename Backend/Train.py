import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import cv2
from joblib import dump
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

img_dir = 'Dataset/' 

img_no = os.listdir(img_dir + 'no/')
img_yes = os.listdir(img_dir + 'yes/')

dataset = []
label = []

for i, img_name in enumerate(img_no):
    if img_name.split('.')[1] == 'jpg':
        image = cv2.imread(img_dir + 'no/' + img_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (64, 64))
        dataset.append(np.array(image))
        label.append(0)

for i, img_name in enumerate(img_yes):
    if img_name.split('.')[1] == 'jpg':
        image = cv2.imread(img_dir + 'yes/' + img_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (64, 64))
        dataset.append(np.array(image))
        label.append(1)

dataset = np.array(dataset)
label = np.array(label)

dataset = dataset.reshape((dataset.shape[0], -1))

x_train, x_test, y_train, y_test = train_test_split(dataset, label, train_size=0.9, random_state=42)

model = SVC()
model.fit(x_train, y_train)

model_name = "Brain_tumor_SVM_model.joblib"
dump(model,model_name)
print("Saved Successfully")

predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:\n", report)
print("Confusion Matrix:\n", conf_matrix)
