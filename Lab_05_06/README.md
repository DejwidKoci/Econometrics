# Qualitative Variables and Segment Models

Here we create models with qualitative variables. cukier_czekolada.xlsx contains data on average monthly consumption of selected foodstuffs (in kg) per person in households by socio-economic group and average monthly disposable income ( in PLN) per person in households by socio-economic group.
In the files czekolada.py , cukier.py , wyroby_cukiernicze.py and owoce.py we test the significance of the model parameters, which include qualitative variables, using the F-test. The procedure is as follows:
1. We estimate the MNK parameters of the basic model and the parameters of the extended model. We denote the residuals in the basic model by $e_i$ and the residuals in the extended model by $u_i$ i = 1, 2, ... , n.
2. We calculate the empirical value of the F-statistic defined as follows:  
$$F = \frac{((Σe_i^2 - Σu_i^2) / p)}{(Σu_i^2 / (n - k - p - 1))}$$
Where:
- $Σu_i^2$ is a coefficient of determination for the base model
- $Σe_i^2$ is a coefficient of determination for the extended model
3. When the null hypothesis is true, the F statistic has an F-Snedecor distribution with m1 = p and m2 = n - k - 1 - p degrees of freedom.
4. For a given level of significance and number of degrees of freedom $m_1 = p$ and $m_2 = n - k - 1 - p$ odczytujemy z tablic wartość krytyczną F* , read off the critical value F* from the tables.

If $F>F$* then hypothesis $H_0$ is rejected. On the other hand, if $F \leq F$* then we have no grounds to reject $H_0$


## Chow Test
$H_0$: The parameters of the model in the predetermined subsamples are equal to each other.  
$H_1$: The parameters of the model in the predetermined subsamples are not a equal.  
The procedure takes place in several stages
1. The model parameters are estimated:
$y_t = \beta_0 + \beta_1 x_{t1} + \beta_2 x_{t2} + \ldots + \beta_k x_{tk} + \epsilon_t \$
and the sum of squares of the residuals is calculated for this model
$$SKR_0 = \sum^T_{t=1} e^2_t$$

2. Model parameters are estimated for each subsample separately:
- model 1 for $t= 1,2,...,t_1 - 1$ obtaining the sum of squares of the residuals $SKR_1$
- model 2 for $t= t_1 + t_1 + 1,...,T obtaining the sum of squares of the residuals $SKR_2$

3. The calculation:
$$F = \frac{(SKR_0 - SKR_1 - SKR_2) / (k+1)}{(SKR_1 + SKR_2) / [T - 2(k+1)]}$$

If $H_0$ is true, then the F statistic has a Fisher Snedecor distribution with $m_1 = k + 1$ and $m_2 = T - 2(k + 1)$ degrees of freedom. We reject the null hypothesis for $F > F$*

test_chowa.py contains this test, in which we check whether our sample needs to be split into smaller sub-samples.
