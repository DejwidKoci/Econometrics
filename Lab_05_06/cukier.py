import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
data = pd.read_excel('cukier_czekolada.xlsx', sheet_name = 'dane')

cukier = data['cukier']
Z = data[['z2', 'z3', 'z4', 'z5', 'z6', 'x']]
Z = sm.add_constant(Z)
model_01 = sm.OLS(cukier, Z).fit()
print(model_01.summary())


X = data['x']
X = sm.add_constant(X)
model_02 = sm.OLS(cukier, X).fit()
print(model_02.summary())



residuals_first = model_01.resid
sum_squared_residuals_first = np.sum(residuals_first ** 2)

residuals_second = model_02.resid
sum_squared_residuals_second = np.sum(residuals_second ** 2)


k = model_02.df_model # number of variables in the basic model (without suspected of being an endogenous variable)
p = 5 # amount of external instruments
n = data.shape[0]
confidence_level = 0.05

numerator =  (sum_squared_residuals_second - sum_squared_residuals_first)/p
denominator = sum_squared_residuals_first/(n - k - 1 - p)

F = numerator/denominator
F_star = stats.f.ppf(1-confidence_level, p, n - k - 1 - p)

if F > F_star:
    print("Odrzucamy H0. Wszystkie instrumenty zewnętrzne są istotne.")
else:
    print("Nie ma podstaw do odrzucenia H0. Wykorzystane instrumenty zewnętrzne są nieistotne.")

print()
print("INTERPRETACJE WYNIKÓW")
print("Wzrost dochodów o tysiąc złotych powodował spadek średniego miesięcznego spożycia cukru o 0.67 kg (ceteris paribus)")
print("Pracownicy nierobotniczy spożywali miesięcznie średnio o 0.2 kg mniej cukru niż pracownicy robotniczy")
print("Rolnicy spożywali miesięcznie średnio o 0.65 kg więcej cukru niż pracownicy robotniczy")
print("Osoby zaliczający się do 'własny_rach' spożywali miesięcznie średnio o 0.17 kg więcej cukru niż pracownicy robotniczy")
print("Emeryci spożywali miesięcznie średnio o 0.69 kg więcej cukru niż pracownicy robotniczy")
print("Renciści spożywali miesięcznie średnio o 0.38 kg więcej cukru niż pracownicy robotniczy")
print()