import numpy as np
import pandas as pd
import statsmodels.api as sm
import pandas as pd

data = pd.read_excel('data.xlsx', sheet_name = 'dane')

y = data['lw']  # Depended variable
X = data[['educ', 'expr']] # Exogenous variables (initial assumption)
X = sm.add_constant(X)
endo = data[['educ']] # Modified by instruments - suspected of being an endogenous variable
Z = data[['expr', 'meduc', 'iq','kww']]  # Instruments
Z = sm.add_constant(Z)

first_model = sm.OLS(endo,Z).fit()
#print(first_model.summary())

residuals = first_model.resid
X['residuals'] = residuals

supporting_model = sm.OLS(y,X).fit()
#print(supporting_model.summary())

coef_res = supporting_model.params['residuals']

if coef_res != 0:
    print("Odrzucamy H0. Zatem składnik losowy modelu jest zależny od X.")
    print("Czyli nie powinniśmy stosować KMNK, ale powinniśmy wykorzystać UMZI (2MNK)")
else:
    print("Brak podstaw do odrzucenia H0. Składnik losowy modelu jest niezależny od X")

