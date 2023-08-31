import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_excel('culture.xlsx', sheet_name = 'Dane')
Y = data['y']
X = data['x']

X = pd.DataFrame({
    'x' : 1 / X,
    'y/x' : Y / X
})

X = sm.add_constant(X)
model = sm.OLS(Y, X).fit()
print(model.summary())

a = -model.params['const']
b = -model.params['y/x']
c = -model.params['x'] / a

print()
print("MODEL TORNQVISTA II RODZAJU: y = a(x - c) / (x + b)")
print("WSPÓŁCZYNNIKI: ")
print("a: ", a)
print("b: ", b)
print("c: ", c)

print()
predicted_y = a * (data['x'] - c) / (b + data['x'])
print("PREDICTED Y: ")
print(predicted_y)

print()
flexibilities = (b + c) * data['x'] / ((data['x'] + b) * (data['x'] - c))
print("FLEXIBILITIES: ")
print(flexibilities)