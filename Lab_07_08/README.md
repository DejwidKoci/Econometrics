# Models with a Binary Explanatory Variable
Binomial (dichotomous) models are the simplest and most popular models in which the explanatory variable is a qualitative variable.
Let $y_i$ denote the i-th realisation of the zero-one variable Y. The variable $y_i$ has a Bernoulli distribution. It takes the value 1 with probability $P_i$ and a value of 0 with probability $1-P_i$.  

The expected value of variable $y_i$ is: $E(y_i) = 1 \cdot P_i + 0 \cdot (1 - P_i) = P_i$  

In binomial models, it is assumed that $P_i$ is a function of the vector of values of the explanatory variables $x_i$ for the i-th unit and the vector of parameters $\beta$:  

$$ P_i = P(y_i = 1 | x_i) = F(x^T_i \beta) $$

Depending on the type of F-function, different types of models. Among the best known are:
- Linear probability model, in which $P_i = x^T_i \beta$
- Logit model, in which $P_i = \frac{1}{1 + \exp(-x^T_i \beta)}$
- Probit model, in which $\int_{\infty}^{x^T_i \beta} \frac{1}{\sqrt{2\pi}} exp(-\frac{t^2}{2}) \ dx$

## Linear Probability Model
In LMP, the parameter $\beta_j$ in the variable $x_j$ is interpreted as an increase in the probability of an event due to an increase variable $x_j$ by a unit (assuming ceteris paribus).  
The probability of Pi can be estimated as follows:
1. The parameters of a linear probability model need to be estimated. In this case, the estimation of the parameter vector is expressed by the formula:  
$$b_{MNK} = (X^TX)^{-1} X^TY $$
2. The vector of theoretical probability values is assumed to be equal:
$$\hat{p_{MNK}} = Xb_{MNK}$$

In this case, it will be necessary to transform the variables:
- $x_{ji}^* = \frac{x_{ji}}{\sqrt{\hat{p_i}(1-\hat{p_i})}}$ for j = 0,1,...,k
- $y_{i}^* = \frac{y_{i}}{\sqrt{\hat{p_i}(1-\hat{p_i})}}$ for i = 1,2,...,n

For $Y$* and $X$* apply the usual Least Squares Method.

Attention: To be able to calculate $\sqrt{\hat{p_i}(1-\hat{p_i})}$, it should be: $0 < \hat{p_i} < 1$
Sometimes in case, when $\hat{p_i} \leq 0$ it is proposed accept $\hat{p_i}$ = 0.001, but when $\hat{p_i} \geq 1$ adopt $\hat{p_i} = 0.999$


# Parameter estimation for logit modelsand probit models
For parameter estimation  $\beta_0, \beta_1, ..., \beta_k$ the most reliable method is usually used reliability. If you have an n-element sanoke $y_1, y_2, ..., y_n,$ where
each of $y_i$ takes the value 1 with probability $P_i$ then the function of reliability has the form: 
$$L = \prod_{i=1}^n P_i^{y_i} (1 - P_i)^{1-y_i}$$
by logarithm we obtain:
$$lnL = \sum_{i=1}^{n}[y_i ln P_i + (1-y_i) ln(1-P_i)]$$
Where:
 - $P_i = F() =  \frac{1}{1 + \exp(-x^T_i \beta)}$ in logit model
 - $P_i = F(x_i^T \beta) =  \int_{\infty}^{x^T_i \beta} \frac{1}{\sqrt{2\pi}} exp(-\frac{t^2}{2}) \ dx$ in probit model

$$x_i^T \beta = \beta_0 + \beta_1 x_{1i} + ... + \beta_j x_{ji} + ... + \beta_k x_{ki} $$

With known values $y_i, x_{1i}, ..., x_{ki}, i = 1, 2, ..., n,$ estimate the parameters $\beta_0, \beta_1, ..., \beta_k,$  so that they ensure the maximum value of the logarithm of the credibility function.
