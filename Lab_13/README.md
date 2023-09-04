# Cobb-Duglas Function
Here we build models using the Cobb-Duglas function. We interpret the elasticity indices, the parameters of the function and examine the degree of homogeneity of the function.  

This is one of the typical functions used in econometric production analysis.  
It has the form:
$$f(x_1, x_2) = b_0 \cdot x_1^{b_1} \cdot x_2^{b_2} \cdot exp(\epsilon) $$
In order to estimate the above model, it is necessary to linearise it:
$$lny = ln\beta_0 + \beta_1ln(x_1) + \beta_2 ln(x_2) + \epsilon$$
All parameters of the C-D function are assumed to be positive
The Cobb-Douglas function satisfies the basic demands placed on production functions, i.e.
1. Marginal productivities are positive (the first derivatives of the C-D function are positive)
2. Marginal productivities are decreasing (second derivatives of the C-D function are less than 1)
3. Productivity of one factor increases as the other factor increases (mixed derivatives are greater than zero)

Furthermore, the Cobb-Douglas function is a homogeneous function.  

A function is homogeneous of degree k if an increase in factors of of production in a given proportion t, results in an increase in output in a proportion
$t^k$ that is $$f(tx_1, tx_2) = t^k f(x_1, x_2)$$

For Cobb - Duglas function $f(x_1, x_2) = b_0 \cdot x_1^{b_1} \cdot x_2^{b_2}$, we have
$$f(tx_1, tx_2) = b_0 \cdot (tx_1)^{b_1} \cdot (tx_2)^{b2} = t^{b_1 + b_2} \cdot b_0 x_1^{b_1} \cdot x_2^{b_2} = t^{b_1 + b_2} \cdot f(x_1, x_2)$$

Thus, the Cobb-Douglas function is a homogeneous function with a degree of homogeneity $k = b_1 + b_2$

# Production Elasticity Coefficients for the Cobb-Douglas Function
The elasticity of production with respect to factor input $x_i$ is calculated using the general formula:
$$E_{x_i} = \frac{\partial f(x_1,x_2,...,x_k)}{\partial x_i}  \cdot  \frac{x_i}{y}$$
The elasticity of production of y with respect to x1 has the form:
$$E_{x_i} = b_0 \cdot b_1 x_1^{b_1 - 1} \cdot x_2^{b_2} \cdot \frac{x_1}{b_0 \cdot x_1^{b_1} \cdot x_2^{b_2}} = b_1$$
The elasticity of production of y with respect to x2 has the form:
$$E_{x_i} = b_0 \cdot  x_1^{b_1} \cdot b_2x_2^{b_2-1} \cdot \frac{x_2}{b_0 \cdot x_1^{b_1} \cdot x_2^{b_2}} = b_2$$
The Cobb-Duglas production function is a function of constant production elasticity (independent of the amount of factor inputs)


# Scale Elasticity for the Cobb-Duglas Function

$ESP = b_1 + b_2$ hence if the inputs of all factors of production increase by 1%, output increases by $(b_1+ b_2)$%  
The Cobb-Douglas function is a homogeneous function with degree of homogeneity $k= b_1+ b_2$. Hence the production:
- increases at a rate less than that of the inputs, if the $b_1 + b_2 < 1$
- increases at the same rate as inputs, if the $b_1 + b_2 = 1$
- increases at a faster rate than inputs if the $b_1 + b_2 > 1$


# Cobb -Douglas Function: Marginal Rates of Substitution

$$KSS_{x_1, x_2} = \frac{dx_2}{dx_1} = -\frac{PK_{x_1}}{PK_{x_2}} = -\frac{b_0 \cdot b_1 x_1^{b_1-1} \cdot x_2^{b_2}}{b_0 \cdot x_1^{b_1} \cdot b_2 x_2^{b_2-1}} = -\frac{b_1}{b_2} \cdot \frac{x_2}{x_1}$$

$$KSS_{x_2, x_1} = \frac{dx_1}{dx_2} = -\frac{PK_{x_2}}{PK_{x_1}} = -\frac{b_0 \cdot x_1^{b_1} \cdot b_2 x_2^{b_2 - 1}}{b_0 \cdot b_1 x_1^{b_1 - 1} \cdot x_2^{b_2}} = -\frac{b_2}{b_1} \cdot \frac{x_1}{x_2}$$
