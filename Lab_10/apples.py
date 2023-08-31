import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('owoce.xlsx', sheet_name = 'Dane')

# power model
Y1 = np.log(data['jabłka'])
X1 = np.log(data['X_real'])
X1 = sm.add_constant(X1)

model_01 = sm.OLS(Y1, X1).fit()
print(model_01.summary())
print()
print("Współczynniki funkcji potęgowej  y = a * x ** b")
print("a: ", np.exp(model_01.params['const']))
print("b: ", model_01.params['X_real'])
print()
print("INTERPRETACJE: ")
print(f"Wzrost miesięcznych dochodów o 1% powoduje wzrost miesięcznego spożycia jabłek o {round(model_01.params['X_real'], 2)}% ")

flexibility = pd.DataFrame({
    "x": data['X_real'],
    "Elastyczność": model_01.params['X_real']
})
print()
print("ELASTYCZNOŚCI: ")
print(flexibility)

y_predicted = np.exp(model_01.params['const']) * data['X_real'] ** model_01.params['X_real']
plt.figure(figsize = (10, 6))
plt.scatter(data['X_real'], data['cytrusowe'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linearyzacja modelu potęgowego")
plt.legend()
plt.grid(True)
plt.show()


# exponential with reverse
Y2 = Y1
X2 = 1 / data['X_real']
X2 = sm.add_constant(X2)

model_02 = sm.OLS(Y2, X2).fit()
print(model_02.summary())
saturation = np.exp(model_02.params['const'])
vertex = -model_02.params['X_real'] / 2

print()
print("Współczynniki funkcji wykładniczej z odwrotnością  y = exp(a - b/x)")
print("a: ", model_02.params['const'])
print("b: ", model_02.params['X_real'])
print("Poziom nasycenia: ", saturation)
print()
print("INTERPRETACJE: ")
print(f"Wraz ze wzrostem dochodów zwiększało się spożycie jabłek ale nie przekraczały one {round(saturation, 2)}%")
print(f"Na początku wraz ze wzrostem dochodów zwiększało się spożycie jabłek w przyspieszonym tempie po czym po przekroczeniu dochodów na poziomie {round(vertex, 2)} spożycie jabłek zaczeły wzrastać wolniej")

flexibility = pd.DataFrame({
    "x": data['X_real'],
    "Elastyczność": -model_02.params['X_real'] / data['X_real']
})
print()
print("ELASTYCZNOŚCI: ")
print(flexibility)



y_predicted = np.exp(model_02.params['const'] + model_02.params['X_real'] / data['X_real'])
plt.figure(figsize = (10, 6))
plt.scatter(data['X_real'], data['cytrusowe'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linearyzacja modelu wykładniczego z odwrotnością")
plt.legend()
plt.grid(True)
plt.show()

# Tornqvist
# y = ax / (b + x)
Y3 = 1 / data['cytrusowe']
X3 = 1 / data['X_real']
X3 = sm.add_constant(X3)

model_03 = sm.OLS(Y3, X3).fit()
print(model_03.summary())

a = 1 / model_03.params['const']
b = a * model_03.params['X_real']
print()
print("Współczynniki funkcji Tornqvista y = ax / (b + x)")
print("a (poziom nasycenia): ", a)
print("b: ", b)
print()
print("INTERPRETACJE: ")
print(f"Wraz ze wzrostem dochodów zwiększało się spożycie jabłek ale nie przekraczały {round(a, 2)}%")

flexibility = pd.DataFrame({
    "x": data['X_real'],
    "Elastyczność": model_03.params['X_real'] / (model_03.params['X_real'] + data['X_real'])
})
print()
print("ELASTYCZNOŚCI: ")
print(flexibility)

y_predicted = a * data['X_real']/(b + data['X_real'])
plt.figure(figsize = (10, 6))
plt.scatter(data['X_real'], data['cytrusowe'], label = 'Y', marker = 'o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linearyzacja modelu Tornqvista")
plt.legend()
plt.grid(True)
plt.show()
