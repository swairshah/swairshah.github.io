---
layout: post
title:  "Randomized Methods in Numerical Linear Algebra - Introduction and
a Brief Survey"
date:   2017-10-16 17:04:07 -0500
categories: blog
tags: [rnla, numerical methods, linear algebra]
---

For the past few years there have been an increasing amount of research on
randomized methods in numerical linear algebra. It seems that these methods
will be more and more useful in the applications where the amount of data is
extremely large (say, matrices of the order $10^8$ data points and thousands
of features), at the same time we have some wiggle room for accuracy of
inference or prediction applied to these datasets. One way to tackle such huge
matrices is access to extremely powerful servers armed with capable tools which 
can take advatage of underlying distributed compute and storage power and run
standard ML algoroithms (e.g. Spark). Some algorithmic tools to tackle huge datasets are what we will talk about here.


