import numpy as np
import pandas as pd
import statsmodels.api as sm
import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name = 'dane')

y = data['lw']  # Depended variable
endo = data[['educ']] # Modified by instruments - suspected of being an endogenous variable
Z = data[['expr', 'meduc']]  # Instruments
Z = sm.add_constant(Z)

endo_hat =  sm.OLS(endo, Z).fit()
#print(endo_hat.summary())

educ_hat = endo_hat.predict()
#print(educ_hat)


X_hat = pd.DataFrame({
    'expr_hat': data['expr'],
    'educ_hat': educ_hat
})

X_hat = sm.add_constant(X_hat)
final = sm.OLS(y, X_hat).fit()
print(final.summary())