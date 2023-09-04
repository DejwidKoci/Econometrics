# Identifying Influential and Outlier Observations

In data analysis, it's important to identify influential or outlier observations that can significantly impact the results of regression models. Here are some common metrics used for this purpose:

## Residuals

One way to identify influential observations is by examining the residuals, which represent the differences between empirical and theoretical values.
$$u = y - y^*$$

## Leverage 

Leverage, denoted as `h_i`, measures the influence of an observation on its own fitted value in a regression model. It is calculated using the formula:
$$h_i = x_i \cdot (X^T \cdot X)^{-1} \cdot x_i^T$$

## Influence 

The influence of an observation can also be assessed using the influence statistic, which is calculated as:
$$\frac{u \cdot h_i}{1 - h_i}$$



## DFFITS

DFFITS is another useful measure for identifying influential observations. It is calculated using the formula:
$$DFFITS_i = r_i \cdot \sqrt{\frac{h_i}{1 - h_i}}$$

The i-th observation is therefore considered to be atypical for which $|\text{DFFITS}_i| > 2 \sqrt{\frac{k+1}{n-k-1}}$

Where:
- `r_i` is the change in the predicted (fitted) value when the ith observation is excluded from the model.
- `h_i` is the leverage value for the ith observation.
- `n` is the number of observations.
- `k` is the number of depended variables.



In addition, graphs have been created showing which observations clearly stand out from the others.
These metrics help you pinpoint observations that may have a disproportionate impact on your regression analysis. Understanding and addressing influential observations is crucial for robust and reliable data analysis.
