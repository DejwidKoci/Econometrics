import pandas as pd
import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
data = pd.read_excel('test_chowa.xlsx', sheet_name = 'Dane')

first_sample = data[:16]
second_sample = data[16:]
# print(first_sample)
# print(second_sample)

Y = data['Y']
Y1 = first_sample['Y']
Y2 = second_sample['Y']
t = data['t']
t1 = first_sample['t']
t2 = second_sample['t']
t = sm.add_constant(t)
t1 = sm.add_constant(t1)
t2 = sm.add_constant(t2)


model = sm.OLS(Y, t).fit()
print(model.summary())

first_model = sm.OLS(Y1, t1).fit()
print(first_model.summary())

second_model = sm.OLS(Y2, t2).fit()
print(second_model.summary())

residuals_model = model.resid
sum_squared_residuals_model = np.sum(residuals_model ** 2)

residuals_first = first_model.resid
sum_squared_residuals_fisrt = np.sum(residuals_first ** 2)

residuals_second = second_model.resid
sum_squared_residuals_second = np.sum(residuals_second ** 2)

k = 1
T = data.shape[0]
confidence_level = 0.05
numerator = (sum_squared_residuals_model - sum_squared_residuals_fisrt - sum_squared_residuals_second) / (k + 1)
denominator = (sum_squared_residuals_fisrt + sum_squared_residuals_second) / (T - 2 * (k + 1))

F = numerator / denominator
F_star = stats.f.ppf(1 - confidence_level, k + 1, T - 2 * (k + 1))

if F > F_star:
    print("Odrzucamy H0, parametry modelu w z góry znanych podróbkach nie są a sobie równe. ")
else:
    print("Brak podstaw do odrzucenia H0, parametry modelu w z góry znanych podróbkach są a sobie równe. Powinniśmy stosować jeden wspólny model dla obu podpróbek")