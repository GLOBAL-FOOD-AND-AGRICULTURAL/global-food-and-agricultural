# crop_disease_detection.py
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
images = []
labels = []
for file in os.listdir('crop_images'):
  img = cv2.imread(os.path.join('crop_images', file))
  images.append(img)
  labels.append(int(file.split('_')[1].split('.')[0]))

# Preprocess data
X = np.array(images)
y = np.array(labels)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
