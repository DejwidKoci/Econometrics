import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('data.xlsx', sheet_name = 'dane')

y1 = data['Y1']
y2 = data[['Y2']]
z = data[['Z1']]

z = sm.add_constant(z)

model_01 = sm.OLS(y1, z).fit()
print(model_01.summary())
print(f"Zatem wzrost dochodów o 1000 zł powoduje wzrost wydatków na żywność o {round(model_01.params['Z1'] * 1000, 2)} zł")

model_02 = sm.OLS(y2, z).fit()
print(model_02.summary())
print(f"Zatem wzrost dochodów o 1000 zł powoduje wzrost wydatków na odzież o {round(model_02.params['Z1'], 2)} zł")