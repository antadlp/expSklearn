#from:
#http://scikit-learn.org/stable/auto_examples/
#linear_model/plot_lasso_and_elasticnet.html

print(__doc__)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

'''
what is 'r2_score'?

from: 
http://stackoverflow.com/questions/23309073/
how-is-the-r2-value-in-scikit-learn-calculated

@eickenberg
The R^2 in scikit learn is essentially the same as what is
described in the wikipedia article on the coefficient of
determination (grep for "the most general definition"). It is 1 -
residual sum of square / total sum of squares

from:
http://stattrek.com/statistics/dictionary.aspx?definition=
coefficient_of_determination

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

'''

np.random.seed(42)

'''
What does np.random.seed(42)?

from:
http://stackoverflow.com/questions
/21494489/what-does-numpy-random-seed0-do

@Zhun Chen
If you set the np.random.seed(a_fixed_number) every time you
call the numpy's other random function, the result will be the
same

@John1024
np.random.seed(0) makes the random numbers predictable, examples:

>>> numpy.random.seed(0) ; numpy.random.rand(4)
array([ 0.55,  0.72,  0.6 ,  0.54])
>>> numpy.random.seed(0) ; numpy.random.rand(4)
array([ 0.55,  0.72,  0.6 ,  0.54])

'''
##generate some sparse data to play with
#begin

n_samples, n_features = 50, 200


X = np.random.randn(n_samples, n_features)
#Matrix of n_samples * n_features
#its the same notation of ng coursera tutorial
#the rows are the training sets and
#the colums are the features.


coef = 3 * np.random.randn(n_features)
#just an vector 

inds = np.arange(n_features)
np.random.shuffle(inds)
coef[inds[10:]] = 0 # sparsify coef


y = np.dot(X, coef)
'''
How np.dot(), operates?

from:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html

For 2-D arrays it is equivalent to matrix multiplication, and for 1-D arrays to
inner product of vectors (without complex conjugation). For N dimensions it is
a sum product over the last axis of a and the second-to-last of b

So,

y = np.dot(X, coef) is:
[in latex notation begin]

\begin{equation}
\sum_{l=1}^{n-features}X_{m\times l}Coef_{l\times1}=y_{m\times1}
\end{equation}

[in latex notation end]

m: is the number of training examples (n_samples)
l: is the number of features (n_features (i dont know if lasso or elastic take
count the bias as feature))

open question: What advantage np.dot() has over np.matmul()? or for what reason
the example chose np.dot() over np.matmul()

'''

# add noise
y+= 0.01 * np.random.normal((n_samples,))

# Split data in train set and test set
n_samples = X.shape[0]
X_train, y_train = X[:n_samples / 2], y[:n_samples / 2]
x_test, y_test = X[n_samples /2:], y[n_samples / 2]

#end
##

##Lasso







