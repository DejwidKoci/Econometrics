import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel("data_02.xlsx", sheet_name='dane')
y = data['lnbwt']
X = data[['cigspreg', 'parity', 'male']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

