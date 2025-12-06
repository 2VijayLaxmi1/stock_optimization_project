import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('/home/vijaylaxmi/stock_optimization_project/sales_data/sales_data.csv')

# Select Features (input columns)
X = df[['Price', 'Opening_Stock']]

# Select Target (output column)
y = df['Units_Sold']

# Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the test set
y_pred = model.predict(X_test)

# ---- Make a new prediction ----
new_data = pd.DataFrame({
    'Price': [120],
    'Opening_Stock': [100]
})

predicted_units = model.predict(new_data)[0]

print("\n Prediction Example")
print(f"For Price = 120 and Opening Stock = 100 → Expected Units Sold = {np.round(predicted_units, 0)}")

