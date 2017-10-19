---
layout: post
title:  "SVD and the Johnson-Lindenstrauss Lemma : two very different dimensionality
reduction methods"
date:   2017-3-11 17:04:07 -0500
categories: blog
tags: [svd, machine-learning, statistics]
---

Recently we had a discussion in our research group meeting about Singular Value 
Decomposition (SVD) and the 
random projection method (where the Johnson-Lindenstrauss Lemma comes into play). 
Both are dimensionality reduction techniques but they differ in the promises they
make in terms of the properties of the output. 

Roughly speaking SVD computes a projection of the input points in a lower
dimensional space such that the sum of the errors is minimized. JL-lemma gives a 
projection with a promise in terms of the worst case distortion of pair-wise distances of
the points. Also SVD expects you to input a dimension where as JL-lemma method 
expects a worst case erorr as input. Let us discuss both in in more detail. 

## SVD

Given a dimension $k$, SVD is used to find the best $k$ dimensional subspace which minimizes the sum of squared errors (the sum of distances of original points to the output points). These output points are the projection of original points on the 'best' $k$
dimensional subspace. Let $X$ be a $D \times n$ matrix with columns $x_i$ are points in a $D$ dimensional space. SVD solves the following problem:

$$ 
\min_{A} \| X - A \|_F^2  \\
\text{ s.t. rank($A$) = $k$} 
$$

The $A$ that minimizes the objective function is the reduced SVD of $X$. Here
reduced SVD means we just use first $k$ singular values and left and right
singular vectors.
Thus $A = \sum_{i=1}^{k} \sigma_i (u_i v_i^T) $. With $u_i$ and
$v_i$ are the $i^{th}$ left and right singular vectors and $\sigma_i$ is the $i^{th}$
singular value of $X$. 
We write it as $A = U_k \Sigma_k V_k^T$. Let $P = U_k$ and $Y = \Sigma_k
V_k^T$. $Y$ will be a $k \times n$ matrix, with each column $y_i$ being $k$
dimensional. We can write the error as:

$$
e = \| X - A \|_F^2 = \|X - PY \|_F^2 
= \sum_{i=1}^{n} \|x_i - P y_i\|_2^2
$$

We can see that minimizing the objective function of SVD is the same as
minimizing the sum of distances of points $x_i$ from their lower dimensional
projections $y_i$.

When we increase the number of dimension $k$ we get better approximation of the
original matrix $X$. Let us see how the error varies as a function of $k$.
This is how we can do the SVD computation with `numpy`.
{% highlight python %}
import numpy as np
import matplotlib.pyplot as plt
D = 20; n = 30
X = np.random.normal(size=(D, n))
U, s, Vt = np.linalg.svd(X)
k = 5
e = np.linalg.norm(X - (U[:,:k] @ np.diag(s[:k]) @ Vt[:k,:]), 'fro')**2
{% endhighlight %}

We let $k$ vary from $1$ to $D$ and plot the error.
{% highlight python %}
k_range = range(1,D)
errors = []
for k in k_range:
    e = np.linalg.norm(X - (U[:,:k] @ np.diag(s[:k]) @ Vt[:k,:]), 'fro')**2
    errors.append(e)
plt.plot(k_range, errors, 'x-')
{% endhighlight %}

## Random Projections and the JL-lemma

The JL-lemma method guarantees that the pairwise distances of the input points are not distorted
too drastically in the given an final error tolerance JL-lemma.
