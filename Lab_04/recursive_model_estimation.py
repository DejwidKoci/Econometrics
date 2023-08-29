import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('data_02.xlsx', sheet_name = 'dane')

P = data['P']
M = data['M']
W = data['W']

W = sm.add_constant(W)
model_01 = sm.OLS(P, W).fit()
print(model_01.summary())

predicted_p = sm.add_constant(model_01.predict())

model_02 = sm.OLS(M, predicted_p).fit()
print(model_02.summary())

print(f"Wzrost plonów o jeden kwintal z 1 ha powoduje wzrost produkcji mięsa o {round(model_02.params['x1'], 2)} kg na 1 ha użytków rolnych")
