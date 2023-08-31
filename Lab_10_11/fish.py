import pandas as pd
import statsmodels.api as sm
import numpy as np


data = pd.read_excel("ryby.xlsx", sheet_name = 'Dane')
Y = np.log(data[['Y1', 'Y2']])
X = np.log(data[['X', 'P1', 'P2']])
X = sm.add_constant(X)

model_01 = sm.OLS(Y['Y1'], X).fit()
print(model_01.summary())

print()
print("INTERPRETACJE: ")
print("Przy założeniu ceteris paribus wzrost dochodów o 1% powodował wzrost spożycia drobiu o 0.3%")
print("Przy założeniu ceteris paribus wzrost ceny ryb o 1% powodował spadek spożycia drobiu o 2.4%")
print("Przy założeniu ceteris paribus wzrost ceny drobiu o 1% powodował wzrost spożycia drobiu o 0.8%")
print()


model_02 = sm.OLS(Y['Y2'], X).fit()
print(model_02.summary())

print()
print("INTERPRETACJE: ")
print("Przy założeniu ceteris paribus wzrost dochodów o 1% powodował wzrost spożycia drobiu o 0.5%")
print("Przy założeniu ceteris paribus wzrost ceny ryb o 1% powodował wzrost spożycia drobiu o 1.2%")
print("Przy założeniu ceteris paribus wzrost ceny drobiu o 1% powodował spadek spożycia drobiu o -2.9%")
print()