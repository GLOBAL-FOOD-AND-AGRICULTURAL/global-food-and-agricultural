import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load farm data
farm_data = pd.read_csv('data/farm-data.csv')

# Preprocess data
X = farm_data.drop(['yield'], axis=1)
y = farm_data['yield']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on testing set
y_pred = model.predict(X_test)

# Evaluate model performance
print("Mean squared error:", model.score(X_test, y_test))
