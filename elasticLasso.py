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
"The R^2 in scikit learn is essentially the same as what is
described in the wikipedia article on the coefficient of
determination (grep for "the most general definition"). It is 1 -
residual sum of square / total sum of squares"

from:
http://stattrek.com/statistics/dictionary.aspx?definition=
coefficient_of_determination

"The coefficient of determination (denoted by R2) is a key output
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
20 percent is predictable; and so on".

'''

np.random.seed(42)

'''
What does np.random.seed(42)?

from:
http://stackoverflow.com/questions
/21494489/what-does-numpy-random-seed0-do

@Zhun Chen
"If you set the np.random.seed(a_fixed_number) every time you
call the numpy's other random function, the result will be the
same"

@John1024
"np.random.seed(0) makes the random numbers predictable, examples:

>>> numpy.random.seed(0) ; numpy.random.rand(4)
array([ 0.55,  0.72,  0.6 ,  0.54])
>>> numpy.random.seed(0) ; numpy.random.rand(4)
array([ 0.55,  0.72,  0.6 ,  0.54])"

'''
##generate some sparse data to play with
#begin

n_samples, n_features = 50, 200

X = np.random.randn(n_samples, n_features)
'''
Matrix of n_samples * n_features
its the same notation of ng coursera tutorial
the rows are the training sets and
the colums are the features.
'''

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

"For 2-D arrays it is equivalent to matrix multiplication, and for 1-D arrays to
inner product of vectors (without complex conjugation). For N dimensions it is
a sum product over the last axis of a and the second-to-last of
b"

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

'''
What is sparsify coef?
and what is it for?

from: 
http://searchdatamanagement.techtarget.com/definition/sparsity-and-density

"A table that is 10% dense has 10% of its cells populated with
non-zero values. It is therefore 90% sparse – meaning that 90% of
its cells are either not filled with data or are zeros"

Analyzing, the block of code in which 'sparsify' is use:
   
1   coef = 3 * np.random.randn(n_features)
2   inds = np.arange(n_features)
3   np.random.shuffle(inds)
4   coef[inds[4:]] = 0 # sparsify coef

Using as an example n_features = 10

In the first line a matrix of random coefficients 1 x n_features is
created with 3 of amplitude. Example:
   
array([ 0.0869964 ,  1.11780373,  3.54187459, -5.69404868, -0.57016024,
       -0.70152387, -2.85919651, -2.61254577, -4.82311611, -4.90727145])

In the second line a matrix of 1 x n_features is created, where
every element is in upward order. Example:

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

In the third line, the matrix above is 'sorted' or as the
function say, its shuffle randomly. Example: 

array([0, 7, 8, 6, 5, 4, 9, 2, 1, 3])

The fourth line does zeros 6 elements (using inds[4:] instead of
inds[10:]) of the matrix coefficient. Example:

array([ 0.0869964 ,  0.        ,  0.        ,  0.        ,  0.        ,
        0.        , -2.85919651, -2.61254577, -4.82311611,  0.        ])

So, in resume for 'sparcify' and the block of code that use it:

   Randomly makes zeros some coeficcients, in this case, makes
   150 coefficients zero.

open question, how is related with elastic and lasso?

'''

# add noise
y+= 0.01 * np.random.normal((n_samples,))

# Split data in train set and test set
n_samples = X.shape[0]
'''
The instruction above is possibly not needed, or maybe is a
security measure for the n_sample variable if the matrix X is
somehow changed. In line 80 'n_samples, n_features = 50, 200' is
already defined.

'''

#X_train, y_train = X[:n_samples / 2], y[:n_samples / 2]
#x_test, y_test = X[n_samples /2:], y[n_samples / 2]
'''
The code above as is declared (till this date on the sklearn
tutorial (04-28-2017)), produce the following error

TypeError                                 Traceback (most recent call last)
<ipython-input-3-846e1b2f93eb> in <module>()
     14 # Split data in train set and test set
     15 n_samples = X.shape[0]
---> 16 X_train, y_train = X[:n_samples / 2], y[:n_samples / 2]
     17 X_test, y_test = X[n_samples / 2:], y[n_samples / 2:]

TypeError: slice indices must be integers or None or have an __index__ method

To fix this, as is declared in the Github proyect:
scikit-learn/examples/linear_model/plot_lasso_and_elasticnet.py 

just use '//' floor division
'''
X_train, y_train = X[:n_samples // 2], y[:n_samples // 2]
X_test, y_test = X[n_samples //2:], y[n_samples // 2:]
'''
Halved the data in a training set and a test set. The first half
[n_samples//2:] is the test set, and the second half
[:n_samples//2] is the training set.
'''
#generate some sparse data to play with
##end



##Lasso
#begin

from sklearn.linear_model import Lasso

alpha = 0.1
lasso = Lasso(alpha=alpha)

y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(lasso)
print("r^2 on test data : %f" % r2_score_lasso)

##Lasso
#end

##Elastic net
#begin
from sklearn.linear_model import ElasticNet

enet = ElasticNet(alpha=alpha, l1_ratio=0.9)

y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(enet)
print("r^2 on test data : %f" % r2_score_enet)

##Elastic Net
#end

##plot 
#begin
plt.plot(enet.coef_, color='lightgreen', linewidth=2,
      label='Elastic net coefficients')
plt.plot(lasso.coef_, color='gold', linewidth=2,
      label='Lasso coefficients')
plt.plot(coef, '--', color='navy', label='original coefficients')
plt.legend(loc='best')
plt.title("Lasso R^2: %f, Elastic Net R^2: %f"
      % (r2_score_lasso, r2_score_enet))
plt.show()
##plot
#end














