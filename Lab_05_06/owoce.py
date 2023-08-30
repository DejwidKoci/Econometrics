import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('owoce.xlsx', sheet_name = 'Dane')

data['Z1'] = data['Płeć'].apply(lambda x: 1 if x == 'kobieta' else 0)
data['Z2'] = data['Płeć'].apply(lambda x: 1 if x == 'mężczyzna' else 0)

V = data[['Dochody w tys. zł', 'Z1', 'Z2']]
V = sm.add_constant(V)

print(data)

model = sm.OLS(data['Spożycie owoców w kg'], V).fit()
print(model.summary())


V1 = data[['Dochody w tys. zł', 'Z1']]
V1 = sm.add_constant(V1)

model_01 = sm.OLS(data['Spożycie owoców w kg'], V1).fit()
print(model_01.summary())

V2 = data[['Dochody w tys. zł', 'Z2']]
V2 = sm.add_constant(V2)

model_02 = sm.OLS(data['Spożycie owoców w kg'], V2).fit()
print(model_02.summary())

print()
print("INTERPRETACJA WYNIKÓW: ")
print(f"Wzrost dochodów o tysiąc złotych spowoduje wzrost spożycia owoców o {round(model_02.params['Dochody w tys. zł'], 2)} kg bez względu na wpływ płci")
print(f"Przy takich samych dochodach mężczyźni spożywali o {-1 * round(model_02.params['Z2'], 2)} kg mniej  niż kobiety")