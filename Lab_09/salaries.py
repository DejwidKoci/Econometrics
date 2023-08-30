import pandas as pd
import statsmodels.api as sm
import numpy as np
data = pd.read_excel('wynagrodzenia.xlsx', sheet_name = 'Dane')
Y = data['Y_wage']
X = data.drop('Y_wage', axis = 1)
ln_Y = np.log(Y)

model_01 = sm.OLS(ln_Y, sm.add_constant(data[['exper', 'exper2']])).fit()
print(model_01.summary())

model_02 = sm.OLS(ln_Y, sm.add_constant(data['educ'])).fit()
print(model_02.summary())
print()
print("INTERPRETACJA: ")
print("Wzrost educ o jeden rok powduje wzrost wage o 5.5%")

model_03 = sm.OLS(ln_Y, sm.add_constant(data['fem'])).fit()
print(model_03.summary())
print()
print("INTERPRETACJA: ")
print("Jeżeli osoba jest kobietą, to jej wynagrodzenie spada o 43%")

model = sm.OLS(ln_Y, sm.add_constant(X)).fit()
print(model.summary())
