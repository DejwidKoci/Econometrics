import pandas as pd
import statsmodels.api as sm
import numpy as np
data = pd.read_excel('production.xlsx', sheet_name = 'Dane')
Y = data['Y=produkcja']
X = data[['X1=praca', 'X2=nak_mat']]

U = np.log(Y)
Z = pd.DataFrame({
    'Z1': np.log(X['X1=praca']),
    'Z2': np.log(X['X2=nak_mat'])
})
Z = sm.add_constant(Z)

model = sm.OLS(U, Z).fit()
print(model.summary())
b0 = np.exp(model.params['const'])
b1 = model.params['Z1']
b2 = model.params['Z2']
print()
print("FUNKCJA PRODUCKJI: ")
print(f"y = {round(b0, 2)} * L ** {round(b1, 2)} * K ** {round(b2, 2)}")

L0 = 25
K0 = 5000
Y0 = b0 * L0 ** b1 * K0 ** b2
print()
print(f"Przewidywana wartość produkcji przy z góry ustalonych L0 i K0:  {round(Y0, 2)} jednostek")

PPL = Y0 / L0
PPK = Y0 / K0
print(f"Produkt przeciętny dla L:  {round(PPL, 2)} jednostek")
print(f"Produkt przeciętny dla K: {round(PPK, 2)} jednostek")

PKL = b0 * b1 * L0 ** (b1 - 1) * K0 ** b2 
PKK = b0 * b2 * L0 ** b1 * K0 ** (b2 - 1)
print(f"Krańcowa wydajność pracy wynosi: {round(PKL, 2)}, czyli o {round(PKL, 2)} jednostek przeciętnie wzrośnie wielkość produkcji jeśli nakład pracy zwiększy się o jednostkę przy nizemienionych nakładach pozostałych czynników produkcji ")
print(f"Krańcowa wydajność kapitału wynosi: {round(PKK, 2)}, czyli o {round(PKK, 2)} jednostekprzeciętnie wzrośnie wielkość produkcji jeśli nakład kapitału zwiększy się o jednostkę przy nizemienionych nakładach pozostałych czynników produkcji ")

EL = b1
EK = b2
k = b1 + b2
print(f"Gdy nakłady pracy wzrosną o 1%, a kapitał pozostanie bez zmian to wielkość produkcji wzrośnie o {round(EL, 2)}%")
print(f"Gdy kapitał wzrośnie o 1%, a nakłady pracy pozostanie bez zmian to wielkość produkcji wzrośnie o {round(EK, 2)}%")

KSSLK = -b1 / b2 * K0 / L0
KSSKL = -b2 / b1 * L0 / K0 

print(f"W przypadku wycofania jednostki nakładu pracy L, należy wprowadzić {round(KSSLK, 2)} jednostek kapitału, by produkcja została utrzymana na tym samym poziomie")
print(f"W przypadku wycofania jednostki kapitału K, należy wprowadzić {round(KSSKL, 2)} jednostek nakładu pracy, by produkcja została utrzymana na tym samym poziomie")

if k > 1:
    print(f'k = {round(k, 2)}, zatem produkcja wzrasta szybciej niż czynniki produkcji, mamy do czynienia z tzw. rosnącymi efektami skali produkcji')
elif k < 1:
    print(f'k = {round(k, 2)}, zatem produkcja wzrasta wolniej niż czynników produkcji, mamy do czynienia z tzw. malejącymi efektami skali produkcji')
else:
    print(f"k = {round(k, 2)}, zatem występują stałe efekty skali produkcji")

