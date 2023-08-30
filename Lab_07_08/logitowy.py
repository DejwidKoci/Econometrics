import numpy as np
import pandas as pd
import statsmodels.api as sm

data = pd.read_excel('egzamin.xlsx', sheet_name = "Dane")

Y = data['Y_egzamin']
X = data.drop('Y_egzamin', axis = 1)
X = sm.add_constant(X)

logit_model = sm.Logit(Y, X)
logit_results = logit_model.fit()

print(logit_results.summary())


AIC = logit_results.aic

nobs = len(Y)  
HQIC = -2 * logit_results.llf + 2 * (logit_results.df_model + 1) * np.log(np.log(nobs))

BIC = logit_results.bic

print("AIC:", AIC)
print("HQIC:", HQIC)
print("BIC:", BIC)
