---
layout: post
title:  "Faster SVD Computation in Python with Numpy"
date:   2018-1-5 17:04:07 -0500
categories: blog
tags: [numerical methods, linear algebra, python, numpy, svd]
---

If you call the Singular Value Decomposition (SVD) routine of numpy 
(`numpy.linalg.svd`), on an array which is
too fat or too thin ($X_{m \times n}$ has either $m \gg n$ or $m \ll
n$) it is simply extremely slower than it
needs to be. For a matrix of size $10000 \times 10$, it takes a few seconds and the 
memory usage spikes up. 
If we bump up the matrix to a size $100000 \times 10$,
we can get a memory error on an 4 GB RAM machine.
Though we can use a simple trick to do this much more efficiently (and this is
without using fancy techniques like [randomized svd] [randSVD]).

If $X$ has the SVD $X = U \Sigma V^T$, and
if the rank is $r$ then $U_{m \times r}$ and $V_{n \times r}$ are the
singular vector matrices with their dimensions. 
We make the following trivial observation, $X X^T = U \Sigma^2 U^T$
(and $X^T X = V \Sigma^2 V^T$).
Now if $m \ll n$ (or $m \gg n$) we can get $U$ (or $V$) by computing the
Eigenvalue decomposition of $X X^T$ (or $X^T X$), which is now a very small matrix and
computing Eigenvalue decomposition is faster and doesn't require too much memory as
well.

Once we have EVD of $X^T X$, we do the following to compute the SVD of $X$

$$ 
\begin{align}
X = U \Sigma V^T &= \sum_{i=1}^{r} \sigma_i u_i v_i^T  \\
u_i^T X &= \sigma_i v_i^T ~~\forall{i} \\
v_i^T &= \frac{u_i^T X} {\sigma_i} ~~\forall{i} \\
\end{align} \\
$$

We can use the same idea with EVD of $X X^T$ as well. Now what we just need to
do is check if $m > n$ or $n > m$ and then in each case just use the derivation
    like above to compute the SVD of $X$ from the EVD of $X X^T$ or $X^T X$.

In the code below we assuming $m > n$, and we use the method used for computing the 
k-SVD approximation to matrix $X$, that is, we approximate $X$ by first $k$ singular vectors.
we can compute the SVD the traditional
way (using `ksvd_bad`) or with the method we just discussed (`ksvd_optim`).

{% highlight python %}
def ksvd_bad(X, k = 2):
  U, s ,Vt = LA.svd(X)
  X_approx = U[:,:k] @ np.diag(s[:k]) @ Vt[:k,:]
  return X_approx
{% endhighlight %}

{% highlight python %}
def ksvd_optim(X, k = 2): 
  X_approx = np.zeros(X.shape)    
  m, n = X.shape
  if m >= n: 
    e, V = LA.eig(X.T @ X)
    idx = np.argsort(-e) # sorting the eigens in descending order
    e = e[idx]     
    V = V[:,idx]
    for i in range(k):
      e = e[i]
      v = V[:,i]
      X_approx += X @ np.outer(v, v.T)

  # similar case for m < n
  return X_approx
{% endhighlight %}
We can compare the relative speeds of these methods. 

I'm sure that programmers used to dealing with numerical linear algebra will be
definitely familliar with these kinds of optimization, nevertheless it
interesting that just a few more lines of code can get such a good performance
boost in terms of memory and computation time.

[randSVD]: https://research.fb.com/fast-randomized-svd/
