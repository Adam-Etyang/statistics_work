from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


#load data from the xlsx file
df = pd.read_excel("../data/DATA.xlsx", sheet_name="Sheet1")

# Prepare data
X = df['Hours_Coding'].values.reshape(-1, 1)  # Reshape for sklearn
y = df['Num_Bugs'].values

# Fit model
model = LinearRegression()
model.fit(X, y)

# Get coefficients
a, b = model.intercept_, model.coef_[0]
print(f"Regression equation: y = {a:.2f} + {b:.2f}x")

# Predict for 20 hours
prediction = model.predict([[20]])
print(f"Predicted bugs for 20 hours: {prediction[0]:.2f}")