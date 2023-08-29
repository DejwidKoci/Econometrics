import numpy as np
import pandas as pd
import statsmodels.api as sm
import pandas as pd

data = pd.read_excel('data_02.xlsx', sheet_name = 'dane')

y = data['lnbwt']  # Depended variable
endo = data[['cigspreg']] # Modified by instruments - suspected of being an endogenous variable
Z = data[['parity', 'male', 'famincom']]  # Instruments
Z = sm.add_constant(Z)

endo_hat =  sm.OLS(endo, Z).fit()
#print(endo_hat.summary())

cigspreg_hat = endo_hat.predict()
#print(educ_hat)


X_hat = pd.DataFrame({
    'parity_hat': data['parity'],
    'male_hat': data['male'],
    'cigspreg_hat': cigspreg_hat
})

X_hat = sm.add_constant(X_hat)
final = sm.OLS(y, X_hat).fit()
print(final.summary())
