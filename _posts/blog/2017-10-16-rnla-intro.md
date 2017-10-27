---
layout: post
title:  "Randomized Methods in Numerical Linear Algebra - Introduction and
a Brief Survey"
date:   2017-10-16 17:04:07 -0500
categories: blog
tags: [rnla, numerical methods, linear algebra]
---

For the past few years there has been an increasing amount of research on
randomized methods in numerical linear algebra. It seems that these methods
will be more and more useful in the applications where the amount of data is
extremely large (say, matrices of the order $10^8$ data points and thousands
of features), at the same time we have some wiggle room for accuracy of
inference or prediction. One way to tackle such huge
matrices is to have access to extremely powerful servers armed with capable tools which 
can take advatage of underlying distributed compute and storage power and run
standard ML algoroithms (e.g. Spark), this doesn't reduce the complexity of computation
but atleast gives us a way to do computation over such large data matrices
which may not fit in the memory. 
Some algorithmic tools to tackle huge datasets are what we will talk about here.

The main idea is to sample the columns/rows (or individual entries) of a large matrix, 
so that the sample is a good approximation of the original matrix. The sampling
procedure depends on the application we intend to use the sampled matrix for. 
There are four main sampling methods:

1. Column/row norm squared sampling 
2. Leverage sampling
3. Volume sampling
4. Element wise sampling

There are various applications where sampling is useful, 
For example, if we want to approximate $A A^T$, we just need
to sample the columns of $A$. If we want to approximate matrix $A$ we need to
sample rows and columns of $A$. Leverage sampling uses the diagonal of $A^+ A$
to generate probabilities. Volume sampling samples a subset of columns, with
sampling probability proportional to the volume of the simplex these columns
form with the origin. Each of these sampling methods have approximation 
guarantees for various problems. We will discuss first three sampling methods
and some application for which there are approximation results.

### Approximate matrix multiplication

Given $A_{m \times n}$ and $B_{n \times p}$, we would like to approximate their
product. One way to write a product $AB$ is as follows:

$$
AB = \sum_{i=1}^n A[:,i] B[i,:]
$$

Which is the sum of the outer products of the columns of $A$ with the rows of $B$. Each
such outer product is a matrix itself. We need $n$ such outerproducts (for each
column of $A$ and corresponding row of $B$) to compute the product.

Now the idea is to approximate these $n$ outer products objects by a much smaller
number of outer products, say $s$. Let us assume that we have some probability
distribution $Pr$, and some random variable $z$ which follows that
distribution, so that $Pr(z = j) = p_j$. We will later discuss what these
probabilities should be.
Associated with this $z$ consider a random matrix $X$ such
that,

$$ 
Pr \Big(X = \frac{A[:,j] B[j,:]} {p_j} \Big) = p_j
$$

So $X$ is a random outer product matrix. We can see that its an unbiased
estimator for the product $AB$ since,

$$
\newcommand{\E}{}{\mathbb{E}} 
\E[X] = \sum_{j} p_j \Big(\frac{A[:,j] B[j,:]} {p_j} \Big) = AB
$$

Let us see what is the variance of this estimator. 

$$
\text{since } \mathbb{E}[X] = AB,~~~
\mathbb{E}[~\|X - AB\|^2_F~] = \mathbb{E}[~\|X - \mathbb{E}[X] \|^2_F~]  \\
$$

which is the sum of variances of all individual entries $x_{i,j}$ of

\begin{align*}
\mathbb{E}[~\|X - AB\|^2_F~] \
= \sum_{i=1}^m \sum_{j=1}^p Var(x_{i,j}) \\
= \sum_{i,j} \Big( \mathbb{E}[x_{i,j}^2] - \mathbb{E}^2[x_{i,j}] \Big) \
= \sum_{i,j} \Big(

\sum_{j} p_j \Big(\frac{A[:,j] B[j,:]} {p_j} \Big) = AB
\end{align*}
