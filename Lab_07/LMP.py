import pandas as pd
import statsmodels.api as sm
import numpy as np

data = pd.read_excel('egzamin.xlsx', sheet_name = "Dane")

Y = data['Y_egzamin']
X = data.drop('Y_egzamin', axis = 1)
X = sm.add_constant(X)

model = sm.OLS(Y,X).fit()
#print(model.summary())

predicted_Y = model.predict()
#print(predicted_Y)

data['Y^'] = predicted_Y
data['P^'] = data['Y^'].apply(lambda x: 0.999 if x > 1 else (0.001 if x < 0 else x))
data['Waga'] = np.sqrt(1 / (data['P^'] * (1 - data['P^'])))
data['X0*'] = data['Waga']
data['X1*'] = data['X1_zaliczenie'] * data['Waga']
data['X2*'] = data['X2_absencja'] * data['Waga']
data['X3*'] = data['X3_nauczyciel'] * data['Waga']
Y_star = data['Y*'] = data['Y_egzamin'] * data['Waga']
X_star = data[['X0*','X1*','X2*','X3*']]

model_lmp = sm.OLS(Y_star, X_star).fit()
print(model_lmp.summary())

