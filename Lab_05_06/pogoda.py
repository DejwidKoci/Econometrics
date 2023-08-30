import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('pogoda.xlsx', sheet_name = 'Dane')

Y = data['Y (lody)']
V = data[['X (zatrudnienie)', 'Z1 (deszcz)', 'Z2 (słońce)']]
V = sm.add_constant(V)
print(V)

model = sm.OLS(Y, V).fit()
print(model.summary())

print()
print("INTERPRETACJE WYNIKÓW: ")
print(f"Zwiększenie zatrudnienia o 1 osobę powodowało wzrost dziennej wartości sprzedaży lodów o {round(model.params['X (zatrudnienie)'], 2)} przy zachowaniu ceteris paribus")
print(f"Przy takim samym zatrudnieniu w pogodę pochmurną sprzedaż lodów była niższa o {round(model.params['Z1 (deszcz)'], 2)} niż w pogodę słoneczną")
print(f"Przy takim samym zatrudnieniu w pogodę słoneczną sprzedaż lodów była większa o {round(model.params['Z2 (słońce)'], 2)} niż w pogodę pochmurną")