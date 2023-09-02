# Qualitative Variables and Segment Models

Here we create models with qualitative variables. cukier_czekolada.xlsx contains data on average monthly consumption of selected foodstuffs (in kg) per person in households by socio-economic group and average monthly disposable income ( in PLN) per person in households by socio-economic group.
In the files czekolada.py , cukier.py and owoce.py we test the significance of the model parameters, which include qualitative variables, using the F-test. The procedure is as follows:
1. We estimate the MNK parameters of the basic model and the parameters of the extended model. We denote the residuals in the basic model by $e_i$ and the residuals in the extended model by $u_i$ i = 1, 2, ... , n.
2. We calculate the empirical value of the F-statistic defined as follows:  
$$F = \frac{((Σe_i^2 - Σu_i^2) / p)}{(Σu_i^2 / (n - k - p - 1))}$$
Where:
- $Σu_i^2$ is a coefficient of determination for the base model
- $Σe_i^2$ is a coefficient of determination for the extended model
3. When the null hypothesis is true, the F statistic has an F-Snedecor distribution with m1 = p and m2 = n - k - 1 - p degrees of freedom.
4. For a given level of significance and number of degrees of freedom $m_1 = p$ and $m_2 = n - k - 1 - p$ odczytujemy z tablic wartość krytyczną F* , read off the critical value F* from the tables.

If $F>F$* then hypothesis $H_0$ is rejected. On the other hand, if $F \leq F$* then we have no grounds to reject $H_0$
