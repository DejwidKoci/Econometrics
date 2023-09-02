# Multi-equation models 
A multi-equation model is a model containing at least 2 equations. Not all equations need to be stochastic, i.e. not every equation must contain a random component. Some of the equations may be identities. In a multi-equation model econometric model, at least one equation must be stochastic.  
Example - Keynesian model:  
$c_t = \alpha_0 +  \alpha_1 y_t + \epsilon_t$  
$y_t = c_t + i_t$
- $c_t$ - denotes consumption expenditure in period t,  
- $y_t$ - national income in period t,  
- $i_t$ - investment in period t.

The first equation is stochastic, the second equation is deterministic, i.e. it is an identity.  


Example of simple model has the form:
$$y_{1t} = \gamma_{11} z_{1t} + \gamma_{12} z_{2t} + \epsilon_{1t}$$
$$y_{2t} = \gamma_{21} z_{1t} + \gamma_{23} z_{3t} + \epsilon_{2t}$$  

In task simple_model_estimation.py we estimate simple model based on monthly expenditure on food in thousand PLN per person (Y1), monthly expenditure on clothing and footwear in PLN per person (Y2) and monthly income in thousand PLN per person (Z1)  

Example of recursive model has the form:
$$y_{1t} = \gamma_{11} z_{1t} + \gamma_{12} z_{2t} + \epsilon_{1t}$$
$$y_{2t} = \gamma_{11} y_{1t} + \gamma_{23} z_{3t} + \epsilon_{1t}$$  

In task recursive_model_estimation.py we estimate recursive model based on yields of 4 basic cereals in q per hectare (P), meat production in kg per hectare of utilised agricultural area (M) and land quality indicator (W)

Example of interdependent equation estimation has the form:
$$y_{1t} = \gamma_{11} y_{2t} + \gamma_{12} z_{2t} + \epsilon_{1t}$$
$$y_{2t} = \gamma_{11} y_{1t} + \gamma_{22} z_{2t} + \gamma_{23} z_{3t}+ \epsilon_{2t}$$

In the task interdependent_equation_estimation.py we estimate this kind of model. 
