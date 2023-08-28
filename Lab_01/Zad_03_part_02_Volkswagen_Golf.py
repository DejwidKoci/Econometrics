import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel("data.xlsx", sheet_name='dane_03')
y = data['Y']
X = data[['X1', 'X3', 'X4']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

# Plots
plt.figure(figsize=(12, 6))
plt.scatter(X['X1'], y, alpha=0.7)
plt.title("Scatter Plot of Y vs. X1")
plt.xlabel("Car age in years [X1]")
plt.ylabel("Car prise in PLN [Y]")
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(X['X3'], y, alpha=0.7)
plt.title("Scatter Plot of Y vs. X3")
plt.xlabel("Capacity of engine in cm3 [X3]")
plt.ylabel("Car prise in PLN [Y]")
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.scatter(X['X4'], y, alpha=0.7)
plt.title("Scatter Plot of Y vs. X4")
plt.xlabel("Mileage in thousand km [X4]")
plt.ylabel("Car prise in PLN [Y]")
plt.grid(True)
plt.show()



plt.figure(figsize=(6, 6))
plt.boxplot(y)
plt.title("Box Plot of Y")
plt.ylabel("Car prise [PLN]")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
plt.boxplot(X['X1'])
plt.title("Box Plot of X1")
plt.ylabel("Car age [years]")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
plt.boxplot(X['X3'])
plt.title("Box Plot of X3")
plt.ylabel("Power of engine [hp]")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
plt.boxplot(X['X4'])
plt.title("Box Plot of X4")
plt.ylabel("Mileage [thousand km]")
plt.grid(True)
plt.show()


# residuals, leverage, influence, DFFITS
residuals = y - y_predicted
leverage = model.get_influence().hat_matrix_diag
influence_summary = model.get_influence().summary_frame()
dffits = influence_summary['dffits']
nobs = len(data)

influence_calc = residuals * leverage / (1 - leverage)

results_df = pd.DataFrame({
    'Residuals': residuals,
    'Leverage': leverage,
    'Influence (calculated)': influence_calc,
    'DFFITS': dffits
})

print(results_df)

print()
print("Obserwacje wpływowe:")
dffits_threshold = 2 * ((model.df_model + 1) / nobs)**0.5
outliers_dffits = influence_summary[abs(dffits) > dffits_threshold]
print(outliers_dffits)


