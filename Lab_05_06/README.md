# Qualitative Variables and Segment Models

Here we create models with qualitative variables. cukier_czekolada.xlsx contains data on average monthly consumption of selected foodstuffs (in kg) per person in households by socio-economic group and average monthly disposable income ( in PLN) per person in households by socio-economic group.
In the files czekolada.py , cukier.py and owoce.py we test the significance of the model parameters, which include qualitative variables, using the F-test. The procedure is as follows:
1. We estimate the MNK parameters of the basic model and the parameters of the extended model. We denote the residuals in the basic model by $e_i$ and the residuals in the extended model by $u_i$ i = 1, 2, ... , n.
2. We calculate the empirical value of the F-statistic defined as follows:  
$$F = \frac{((Σe_i^2 - Σu_i^2) / p)}{(Σu_i^2 / (n - k - p - 1))}$$

