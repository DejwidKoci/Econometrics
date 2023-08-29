import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
data = pd.read_excel('żywność.xlsx', sheet_name = 'Dane')

food = data['Y']
V = data[['X', 'Z1', 'Z2', 'Z3']]
V = sm.add_constant(V)
model_01 = sm.OLS(food, V).fit()
print(model_01.summary())

print()
print("Wzrost dochodów o tysiąc zł powodował procentowy spadek udziałów wydatków na żywność w łącznych wydatkach o 0.0002%")
print("W badanym okresie procentowy udział wydatków na żywność w łącznych wydatkach w pierwszym kwartale była średnio niższa o 1.17% niż w czwartym kwartale.")
print("W badanym okresie procentowy udział wydatków na żywność w łącznych wydatkach w drugim kwartale była średnio niższa o 0.46% niż w czwartym kwartale.")
print("W badanym okresie procentowy udział wydatków na żywność w łącznych wydatkach w trzecim kwartale była średnio wyższa o 0.06% niż w czwartym kwartale.")

X = data['X']
X = sm.add_constant(X)
model_02 = sm.OLS(food, X).fit()
print(model_02.summary())




residuals_first = model_01.resid
sum_squared_residuals_first = np.sum(residuals_first ** 2)

residuals_second = model_02.resid
sum_squared_residuals_second = np.sum(residuals_second ** 2)


k = model_02.df_model # number of variables in the basic model (without suspected of being an endogenous variable)
p = 3 # amount of external instruments
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