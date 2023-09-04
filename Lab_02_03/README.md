# Endogeneity and Exogeneity of the Linear Model Variables.

In a situation where we suspect that there are variables in our model that are to some extent dependent on the random component, we can apply the General Instrumental Variables Method. It has the form:
$$b_{GIV} =  (\hat{X}^T \hat{X})^{-1} \cdot (\hat{X}^T Y)$$

The use of the above formula corresponds to using ordinary MNK twice:
1) In the first step, $\hat{X} = Z(Z^TZ)^{-1} Z^TX$ is estimated, i.e. here models are estimated in which the explanatory variables are the instrumental variables Z and the explanatory variables are X (as many models as there are X variables).
2) In the second step, a model is estimated in which Y is the explanatory variable and the explanatory variables are $\hat{X}$

# Hausman Test
Consider the following model: $Y = X$ $\beta$ + $\epsilon$ 

We verify the following hypothesis:  
$H_0$: the random component of the model $\epsilon$ is independent of X   
$H_1$: the random component of the model $\epsilon$ is dependent on X

In our case, is suspected that `educ` is an endogenous variable. We stimate a model in which `educ` is the explanatory and all Z instruments (internal and external) the explanatory: $$educ = \delta Z + \xi$$  
`educ` is endogenous if and only if $\xi$ is correlated with $\epsilon$, meaning that in the model $\epsilon$ = $\rho$ $\xi$ + $\eta$ the parameter $\rho$ is significantly different from zero.
Summary we get: $$Y = \beta_0 + \beta_1 educ + \beta_2 staz + \rho \xi + \eta $$

If $\rho$ is significantly different from zero, the `educ` variable is endogenous and reject the null hypothesis.

# Sargan Test
The hypothesis is being verified:  
$H_0$: the instruments are independent of $\epsilon$  
$H_1$: the instruments are depended on $\epsilon$  

An auxiliary model is created in which the explanatory variable is the residuals from the output model (i.e. Y from X, but $b_{2MNK}$ is used) and the explanatory variables are all exogenous variables.  

The test statistic is of the form: $S = nR^2$  
Where:
- $n$ - the number of observations
- $R^2$ - coefficient of determination of the auxiliary model

Under the assumption of the null hypothesis, $S$ has a chi-square distribution with $m-r$ degrees of freedom degrees of freedom, where $m-r$ is the number of external instruments minus the number of instrumentalised variables.  
If $S > chi^2_{m-r; 0.05}$ we reject $H_0$.

# Weak Instruments Test
$H_1$: the instruments are weakly correlated with the instrumented variable.  
$H_2$: the instruments are strongly correlated with the instrumented variable.  

An auxiliary model is used to verify the hypothesis:
- the explanatory variable is the instrumentalised variable (in our case: educ),
- The explanatory variables are all instruments (internal and external).

The testing procedure in this case is as follows:
1. We estimate MNK the parameters of the basic model and the parameters of the extended model. Let us denote the residuals in the basic model by $e_i$ and the residuals in the extended model by $u_i$.
2. We calculate the empirical value of the F-statistic defined as follows:
3. With the null hypothesis being true, the F statistic has an F - Snedecor distribution with $m_1 = p$ and $m_2 = n - k - 1 - p$ degrees of freedom.
4. For a given level of significance and for the number of degrees of freedom $m1 = p$ and $m2 = n - k - 1 - p$, we read the critical value of $F$ from the tables. If $F$ $>$ $F*$ then hypothesis $H_0$ is rejected. On the other hand, if $F$ $≤$ $F^*$ then we have no grounds to reject hypothesis $H_0$.


The combined significance of all external instruments is verified. The F-statistic is used for this purpose. Rejecting the hypothesis of no the joint significance of all external instruments means rejection of the hypothesis that the instruments are weakly correlated with the variable instrumentalised variable.
