import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel('food.xlsx', sheet_name = 'Dane')

Y = data['Y']
X = data['X']

V = 1/data['X']
model = sm.OLS(Y, sm.add_constant(V)).fit()
print(model.summary())

print()
print("INTERPRETACJA: ")
print("Gdy dochody bardzo wzrosną to wydatki na żywność wzrosną o 5,3 punktu procentowego")
print()

plt.figure(figsize = (10, 6))
plt.scatter(X, Y, label = 'Y', marker = 'o')
plt.xlabel('X [PLN]')
plt.ylabel('Y [%]')
plt.title("Wydatki na żywność w wydatkach ogółem vs. dochody na osobę")
plt.legend()
plt.grid(True)
plt.show()