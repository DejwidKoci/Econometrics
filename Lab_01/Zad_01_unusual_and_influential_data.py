import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_excel("data.xlsx", sheet_name='dane_01')
y = data['Y']
X = data[['X']]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
y_predicted = model.predict(X)

# Plots
plt.figure(figsize=(12, 6))
plt.scatter(y, X['X'], alpha=0.7)
plt.title("Scatter Plot of Y vs.X")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()


plt.figure(figsize=(6, 6))
plt.boxplot(y)
plt.title("Box Plot of Y")
plt.ylabel("Y")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
plt.boxplot(X['X'])
plt.title("Box Plot of X")
plt.ylabel("X")
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


