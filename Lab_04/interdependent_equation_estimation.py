import pandas as pd
import statsmodels.api as sm

data = pd.read_excel('data_03.xlsx', sheet_name = 'dane')

Y1 = data['y1t']
Y2 = data['y2t']
Z = data[['z1t', 'z2t', 'z3t']]


model_01 = sm.OLS(Y1, Z).fit()
print(model_01.summary())

model_02 = sm.OLS(Y2, Z).fit()
print(model_02.summary())

data['predicted_y1'] = model_01.predict()
data['predicted_y2'] = model_02.predict()


X1 = data[['predicted_y2', 'z1t']]
model_03 = sm.OLS(Y1, X1).fit()
print(model_03.summary())

X2 = data[['predicted_y1', 'z2t', 'z3t']]
model_04 = sm.OLS(Y2, X2).fit()
print(model_04.summary())

