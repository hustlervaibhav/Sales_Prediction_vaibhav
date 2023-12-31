# -*- coding: utf-8 -*-
"""Sales_Prediction _vaibhav.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WEQB82bYAJY_n2VE9DggtoqRP29wRljK

Importing Libraries
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

advert=pd.read_csv("/content/advertising.csv")

advert

advert.info()

print(advert.columns)

column_names = ['TV', 'Radio', 'Newspaper', 'Sales']
for column in column_names:
    column_data = advert[column]
    print(f"Column: {column}")
    print(column_data)
    print()

advert.isnull().sum()

advert.count()

print(advert.dtypes)

print(advert.shape)

print(advert.describe())

print(advert.shape)

print(advert.describe)

filtered_data = advert[(advert['TV'] >= 180) & (advert['TV'] <= 230)]

print(filtered_data)

filtered_data = advert[(advert['Radio'] >= 3.7) & (advert['Radio'] <= 10.8)]

print(filtered_data)

filtered_data = advert[(advert['Sales'] >= 12) & (advert['Sales'] <= 15)]

print(filtered_data)

filtered_data = advert[(advert['Newspaper'] >= 40) & (advert['Newspaper'] <= 60)]

print(filtered_data)

""" Now comes the part of DATA VISUALIZATION"""

advert.hist(bins=10, figsize=(10, 8))
plt.tight_layout()
plt.show()

#Color composition
colors = ['green' if length >= 120 else 'yellow' for length in advert['TV']]

#Scatter Plot
plt.scatter(advert['TV'], advert['Radio'], c=colors)
plt.ylabel('TV')
plt.xlabel('Radio')
plt.title('TV vs Radio')

colors = ['green' if length >= 45 else 'yellow' for length in advert['Newspaper']]

#Next Scatter Plot
plt.scatter(advert['Newspaper'], advert['Radio'], c=colors)
plt.ylabel('Newspaper')
plt.xlabel('Radio')
plt.title('Newspaper vs Radio')

#Columns for CORRELATION
columns = ['Radio', 'TV', 'Sales', 'Newspaper',]

#Calculation of coefficient matrix
correlation_matrix = advert[columns].corr()

print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.countplot(x='TV', data=advert, )
plt.show()

#Finding Outliners in data
sns.heatmap(advert.isnull(), yticklabels=False, annot=True)

sns.scatterplot(x='TV', y='Sales',
                hue='TV', data=advert, )

sns.pairplot(advert, hue='TV', height=2)

sns.scatterplot(x='Newspaper', y='Sales',
                hue='Newspaper', data=advert, )

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
sns.boxplot(x='Radio', y='Sales', data=advert)

plt.subplot(2, 2, 2)
sns.boxplot(x='Newspaper', y='Sales', data=advert)

plt.subplot(2, 2, 3)
sns.boxplot(x='TV', y='Sales', data=advert)

plt.tight_layout()
plt.show()

sns.histplot(advert['Sales'], kde=True)
plt.title('Distribution of Sales')
plt.show()

"""Linear Regressiion Model"""

# Division of Data into Features (X) and Target Variable (Y)
X = advert[['TV', 'Radio', 'Newspaper']]
Y = advert['Sales']

#Training And Testing Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

#Model training
lr = LinearRegression()
lr.fit(X_train, Y_train)

Y_pred = lr.predict(X_test)

#Model Evaluation
mse = mean_squared_error(Y_test, Y_pred)
rmse = mean_squared_error(Y_test, Y_pred, squared=False)
r2 = r2_score(Y_test, Y_pred)

#Accuracy calculation
threshold = 0.1  # Define your threshold value here
accurate_predictions = (abs(Y_test - Y_pred) <= threshold).sum()
total_predictions = len(Y_test)
accuracy = accurate_predictions / total_predictions

print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Accuracy:", accuracy)
print("R-squared (R2) Score:", r2)

"""RANDOM FOREST REGRESSION"""

X = advert[['TV', 'Radio', 'Newspaper']]
Y = advert['Sales']

#Data splitting into traing and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

#Training Random Forest Model
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, Y_train)

Y_pred = rf.predict(X_test)

mse = mean_squared_error(Y_test, Y_pred)
rmse = mean_squared_error(Y_test, Y_pred, squared=False)
r2 = r2_score(Y_test, Y_pred)

print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2) Score:", r2)