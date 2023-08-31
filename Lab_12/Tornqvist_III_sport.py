import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_excel('sport.xlsx', sheet_name = 'Dane')
Y = data['y']
X = data['x']

X = pd.DataFrame({
    'x' : X,
    'y/x' : Y / X
})

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())

a = model.params['x']
b = -model.params['y/x']
c =  -model.params['const'] / model.params['x']

print()
print("MODEL TORNQVISTA III RODZAJU: y = ax(x - c) / (x + b)")
print("WSPÓŁCZYNNIKI: ")
print("a: ", a)
print("b: ", b)
print("c: ", c)

print()
predicted_y = a * X['x'] * (X['x'] - c) / (b + X['x'])
print("PREDICTED Y: ")
print(predicted_y)

print()
flexibilities = (X['x'] ** 2 + 2 * b * X['x'] - c * b)/((X['x'] + b) * (X['x'] - c))
print("FLEXIBILITIES: ")
print(flexibilities)