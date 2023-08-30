import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

data_01 = pd.read_excel('data.xlsx', sheet_name = 'Dane_01')
data_02 = pd.read_excel('data.xlsx', sheet_name = 'Dane_02')
data_03 = pd.read_excel('data.xlsx', sheet_name = 'Dane_03')
data_04 = pd.read_excel('data.xlsx', sheet_name = 'Dane_04')

Y1 = np.log(data_01['y'])
X1 = np.log(data_01['x'])

Y2 = np.log(data_02['y'])
X2 = data_02['x']

Y3 = data_03['y']
X3 = np.log(data_03['x'])

Y4 = data_04['y']
data_04['x^2'] = data_04['x'] ** 2
X4 = data_04[['x', 'x^2']]

model_01 = sm.OLS(Y1, sm.add_constant(X1)).fit()
print(model_01.summary())
print()
print("INTERPRETACJA: ")
print("Wzrost x o 1% powodował wzorst y o ok 4%")
print()

plt.figure(figsize = (10, 6))
plt.scatter(data_01['x'], data_01['y'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Model potęgowy")
plt.legend()
plt.grid(True)
plt.show()

model_02 = sm.OLS(Y2, sm.add_constant(X2)).fit()
print(model_02.summary())
print()
print("INTERETACJA: ")
print("Wzrost X o jednostkę powodował wzrost Y o 10%")
print()

plt.figure(figsize = (10, 6))
plt.scatter(data_02['x'], data_02['y'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Model wykładniczy")
plt.legend()
plt.grid(True)
plt.show()

model_03 = sm.OLS(Y3, sm.add_constant(X3)).fit()
print(model_03.summary())
print()
print("INTERPRETACJA: ")
print("Wzrost x o 1% powodował wzrost y o 0,0052 jednostek")
print()

plt.figure(figsize = (10, 6))
plt.scatter(data_03['x'], data_03['y'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Model logarytmiczny")
plt.legend()
plt.grid(True)
plt.show()

model_04 = sm.OLS(Y4, sm.add_constant(X4)).fit()
print(model_04.summary())
print()
print("INTERPETACJA: ")
print("Na początku wraz ze wzrostem X maleje Y, po czym po przekroczeniu poziomu X=5,24 wzrost X powoduje zwiększenie się poziomu Y")
print()

plt.figure(figsize = (10, 6))
plt.scatter(data_04['x'], data_04['y'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Model kwadratowy")
plt.legend()
plt.grid(True)
plt.show()