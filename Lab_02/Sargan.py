import numpy as np
import pandas as pd
import statsmodels.api as sm
import pandas as pd
import scipy.stats as stats
from UMNK_01 import final

data = pd.read_excel('data.xlsx', sheet_name = 'dane')
n = data.shape[0]
confidence_level = 0.05
m = 3 # amount of external instruments
r = 1 # amount of endogenous explanatory variables
y = data['lw']  # Depended variable
X = data[['educ', 'expr']] # Exogenous variables (initial assumption)
X = sm.add_constant(X)
endo = data[['educ']] # Modified by instruments - suspected of being an endogenous variable
Z = data[['expr', 'meduc', 'iq','kww']]  # Instruments
Z = sm.add_constant(Z)
residuals = final.resid

model = sm.OLS(residuals, Z).fit()
#print(model.summary())

r_squared = model.rsquared

S = n * r_squared
S_star = stats.chi2.ppf(1 - confidence_level, m - r)

if S < S_star:
    print("Brak podstaw do odrzucenia H0, mówiącej o tym że instrumenty są niezależne od epsilon. Wykorzystane instrumenty są egzogeniczne.")
else:
    print("Odrzucamy H0. Instrumenty są zależne od epsilon. Wykrozystane instrumenty są endogeniczne.")