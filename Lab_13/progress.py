import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_excel('progress.xlsx', sheet_name = 'Dane')
Y = data['Produkcja']
X = data[['Zatrudnienie', 'Majątek']]

U = np.log(Y)
Z = np.log(X)
t = data['Miesiąc']
Z['t'] = t
Z = sm.add_constant(Z)

model = sm.OLS(U, Z).fit()
print(model.summary())
const = np.exp(model.params['const'])

print()
print("FUNKCJA PRODUKCJI: ")
print(f" {round(const, 2)} * L ** {round(model.params['Zatrudnienie'], 2)} * K ** {round(model.params['Majątek'], 2)} * exp({round(model.params['t'], 2)} * t)")
print("Ponieważ parametr delta(stojący przy zmiennej t) jest statystycznie istotny, to występuje efekt postępu techniczno-organizacyjnego ")
print("Przy takim samym wykorzystaniu nakładów kapitąłowych i pracy z miesiąca na miesiąc produkcja rosła o 1%")