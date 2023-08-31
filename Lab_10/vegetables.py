import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("warzywa.xlsx", sheet_name = 'Dane')

# power model
Y1 = np.log(data['y'])
X1 = np.log(data['x'])
X1 = sm.add_constant(X1)

model_01 = sm.OLS(Y1, X1).fit()
print(model_01.summary())
print()
print("Współczynniki funkcji potęgowej  y = a * x ** b")
print("a (poziom nasycenia): ", np.exp(model_01.params['const']))
print("b: ", model_01.params['x'])
print()
print("INTERPRETACJE: ")
print("Wzrost miesięcznych dochodów o 1% powoduje wzrost miesięcznych wydatków na warzywa i ich przetwory o 0.58%")

flexibility = pd.DataFrame({
    "x": data['x'],
    "Elastyczność": model_01.params['x']
})
print()
print("ELASTYCZNOŚCI: ")
print(flexibility)

y_predicted = np.exp(model_01.params['const']) * data['x'] ** model_01.params['x']
plt.figure(figsize = (10, 6))
plt.scatter(data['x'], data['y'], label = 'Y', marker = 'o')
plt.plot(data['x'], y_predicted)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linearyzacja modelu potęgowego")
plt.legend()
plt.grid(True)
plt.show()

# exponential with reverse
Y2 = Y1
X2 = 1 / data['x']
X2 = sm.add_constant(X2)

model_02 = sm.OLS(Y2, X2).fit()
print(model_02.summary())
saturation = np.exp(model_02.params['const'])
vertex = -model_02.params['x'] / 2

print()
print("Współczynniki funkcji wykładniczej z odwrotnością  y = exp(a - b/x)")
print("a (poziom nasycenia): ", saturation)
print("b: ", vertex)
print()
print("INTERPRETACJE: ")
print(f"Wraz ze wzrostem dochodów zwiększały się wydatki na warzywa ale nie przekraczały {round(saturation, 2)}%")
print(f"Na początku wraz ze wzrostem dochodów zwiększały się wydatki na warzywa w przyspieszonym tempie po czym po przekroczeniu dochodów na poziomie {round(vertex, 2)} dochody zaczeły wzrastać wolniej")

flexibility = pd.DataFrame({
    "x": data['x'],
    "Elastyczność": -model_02.params['x'] / data['x']
})
print()
print("ELASTYCZNOŚCI: ")
print(flexibility)



y_predicted = np.exp(model_02.params['const'] + model_02.params['x'] / data['x'])
plt.figure(figsize = (10, 6))
plt.scatter(data['x'], data['y'], label = 'Y', marker = 'o')
plt.plot(data['x'], y_predicted)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linearyzacja modelu wykładniczego z odwrotnością")
plt.legend()
plt.grid(True)
plt.show()

# Tornqvist
# y = ax / (b + x)
Y3 = 1 / data['y']
X3 = 1 / data['x']
X3 = sm.add_constant(X3)

model_03 = sm.OLS(Y3, X3).fit()
print(model_03.summary())

a = 1 / model_03.params['const']
b = a * model_03.params['x']
print()
print("Współczynniki funkcji Tornqvista y = ax / (b + x)")
print("a (poziom nasycenia): ", a)
print("b: ", b)

flexibility = pd.DataFrame({
    "x": data['x'],
    "Elastyczność": model_03.params['x'] / (model_03.params['x'] + data['x'])
})
print()
print("ELASTYCZNOŚCI: ")
print(flexibility)

y_predicted = a * data['x']/(b + data['x'])
plt.figure(figsize = (10, 6))
plt.scatter(data['x'], data['y'], label = 'Y', marker = 'o')
plt.plot(data['x'], y_predicted)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linearyzacja modelu Tornqvista")
plt.legend()
plt.grid(True)
plt.show()
