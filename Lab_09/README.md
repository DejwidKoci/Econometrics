# Unlinear models
It follows from economic theory that relationships economic relationships are often not linear.
With regard to the methods of parameter estimation of non-linear models, a distinction is made between:
1) models that are non-linear with respect to the variables, butlinear with respect to the parameters,
2) models that are non-linear with respect to the variables and parameters, but which can be reduced to
linear models by appropriate transformations (linearisable models),
3) non-linear in the strict sense (models, which cannot be linearised).  

In this python's files we build these unlinear models and create interpretations of the coefficients of this models.


# Estimation of linear models against parameters
For the model:
$$Y = \beta_0 + \beta_1 f_1(X_1, X_2, ..., X_k) + ... + \beta_p f_p(X_1, X_2, ..., X_k) + \epsilon $$    
we construct auxiliary variables:  
$$Z_1 = f_1(X_1, X_2, ..., X_k)$$    
$$...$$  
$$Z_p = f_p(X_1, X_2, ..., X_k)$$    
we obtain a linear model:  
$$Y = \beta_0 + \beta_1 Z_1 + ... + \beta_p Z_p + \epsilon $$  
whose parameters we estimate with MNK

# Linearisable models
Certain non-linear models can be reduced to linear models through appropriate transformations.
In practice, a frequently used transformation is logarithmisation.
Examples of linearisable models:
- Power model
- Exponential mmodel

# Power model
In power model $Y = \alpha X^{\beta} \cdot \xi$ we make the logarithm:
$$ln Y = ln \alpha + \beta ln X + ln \xi $$
we create "artificial" variables $U = ln Y, Z = lnX, \beta_0 = ln \alpha, \beta_1 = \beta, \epsilon = ln \xi$ and we receive:
$$U = \beta_0 + \beta_1 Z + \epsilon $$
$\beta_0, \beta_1$ estimate the same like in linear models.  
Similarly, in a model containing k explanatory variables:
$$Y = \alpha X_1^{\beta_1} \cdot X_2^{\beta_2} \cdot X_k^{\beta_k} \cdot \xi $$
substitute: $U = ln Y$, $Z_1 = ln X_1$, $Z_2 = ln X_2$, ... , $Z_k = ln X_k$, $\beta_0 = ln \alpha_0$, $\epsilon = ln \xi$, and we receive:  
$$U = \beta_0 + \beta_1 Z_1 + \beta_2 Z_2 + \beta_k Z_k + \epsilon $$
and we estimate $\beta_0, \beta_1, \beta_2, ..., \beta_k $

# Exponential model
In exponential model $Y = e^{\alpha + \beta X} \cdot \xi$ we make logarithm:
$$ln Y = \alpha + \beta \cdot X + ln \xi$$
we create "artificial" variables $U = ln Y$ and $\epsilon = ln \xi$ and we receive:
$$U = \alpha + \beta \cdot X + \epsilon$$
$\beta_0, \beta_1$ estimate the same like in linear models.
Similarly, in a model containing k explanatory variables:
$$Y = exp(\beta_0 + \beta_1 X_1 + \beta_2 X_2 + ... + \beta_k X_k + \epsilon) \cdot \xi$$
we create $U = ln Y$, and $\epsilon = ln \xi$ and we receive:
$$U = \beta_0 Z_0 + \beta_1 Z_1 + ... + \beta_k X_k + \epsilon $$
of which parameters $\beta_0, \beta_1, \beta_2, ..., \beta_k$ estimate by OLS.
