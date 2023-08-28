import numpy as np
import pandas as pd
import statsmodels.api as sm
import pandas as pd
import scipy.stats as stats
from UMNK_01 import final

data = pd.read_excel('data.xlsx', sheet_name = 'dane')
endo = data[['educ']] # Modified by instruments - suspected of being an endogenous variable
Z = data[['expr', 'meduc', 'iq','kww']]  # Instruments
Z = sm.add_constant(Z)
X = data[['educ', 'expr']] # Exogenous variables (initial assumption)
X = sm.add_constant(X)

first_model = sm.OLS(endo,Z).fit()
#print(first_model.summary())
residuals_first = first_model.resid
sum_squared_residuals_first = np.sum(residuals_first ** 2)

second_model = sm.OLS(endo,X.drop(endo, axis = 1)).fit()
#print(second_model.summary())
residuals_second = second_model.resid
sum_squared_residuals_second = np.sum(residuals_second ** 2)

n = data.shape[0]
confidence_level = 0.05
k = second_model.df_model # number of variables in the basic model (without suspected of being an endogenous variable)
p = 3 # amount of external instruments


numerator =  (sum_squared_residuals_second - sum_squared_residuals_first)/p
denominator = sum_squared_residuals_first/(n - k - 1 - p)

F = numerator/denominator
F_star = stats.f.ppf(1-confidence_level, p, n - k - 1 - p)

if F > F_star:
    print("Odrzucamy H0. Wszystkie instrumenty zewnętrzne są istotne.")
else:
    print("Nie ma podstaw do odrzucenia H0. Wykorzystane instrumenty zewnętrzne są nieistotne.")
