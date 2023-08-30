import numpy as np
import pandas as pd
import statsmodels.api as sm

data = pd.read_excel('egzamin.xlsx', sheet_name = "Dane")

Y = data['Y_egzamin']
X = data.drop('Y_egzamin', axis = 1)
X = sm.add_constant(X)

probit_model = sm.Probit(Y, X)
probit_results = probit_model.fit()

print(probit_results.summary())


AIC = probit_results.aic

nobs = len(Y)  
HQIC = -2 * probit_results.llf + 2 * (probit_results.df_model + 1) * np.log(np.log(nobs))

BIC = probit_results.bic

print("AIC:", AIC)
print("HQIC:", HQIC)
print("BIC:", BIC)
