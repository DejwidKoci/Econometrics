import pandas as pd
import statsmodels.api as sm
import numpy as np


data = pd.read_excel("kabanosy.xlsx", sheet_name = 'Dane')
Y = np.log(data['Y'])
X = np.log(data[['X', 'P']])
X = sm.add_constant(X)

model = sm.OLS(Y, X).fit()
print(model.summary())

print()
print("INTERPRETACJE: ")
print("Przy takich samych cenach wzrost dochodów o 1% powodował wzrost sprzedaży średnio o 0.6%")
print("Przy takich samych dochodach wzrost ceny o 1% powodował spadek sprzedaży kabanosów średnio o 0.9%")
print()