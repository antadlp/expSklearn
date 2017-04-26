#from:
#http://scikit-learn.org/stable/auto_examples/
#linear_model/plot_lasso_and_elasticnet.html

print(__doc__)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

'''
what is 'r2_score'?

The R^2 in scikit learn is essentially the same as what is
described in the wikipedia article on the coefficient of
determination (grep for "the most general definition"). It is 1 -
residual sum of square / total sum of squares

http://stackoverflow.com/questions/23309073/
how-is-the-r2-value-in-scikit-learn-calculated

The coefficient of determination (denoted by R2) is a key output
of regression analysis. It is interpreted as the proportion of
the variance in the dependent variable that is predictable from
the independent variable.

The coefficient of determination is the square of the correlation
(r) between predicted y scores and actual y scores; thus, it
ranges from 0 to 1

With linear regression, the coefficient of determination is also
equal to the square of the correlation between x and y scores

An R2 of 0 means that the dependent variable cannot be predicted
from the independent variable

An R2 of 1 means the dependent variable can be predicted without
error from the independent variable

An R2 between 0 and 1 indicates the extent to which the dependent
variable is predictable. An R2 of 0.10 means that 10 percent of
the variance in Y is predictable from X; an R2 of 0.20 means that
20 percent is predictable; and so on.

http://stattrek.com/statistics/dictionary.aspx?definition=
coefficient_of_determination

'''








