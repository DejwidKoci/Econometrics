import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel("data.xlsx", sheet_name='dane')
y = data['lw']
X = data[['educ','expr']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())