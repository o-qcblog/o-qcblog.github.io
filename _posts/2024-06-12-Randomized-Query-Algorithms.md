---
Layout: post
mathjax: true
title:  "Randomized Query Algorithms"
categories: [Note, ComplexityTheory]
---

*As in many other models of computation, we can add the power of randomization to decision trees. Given the power of randomness, can we reduce the number of queries? This blog post discusses randomized query algorithm, introducing it from two different lenses.*

Given that we are familiar with decision trees (if not, check out my post on [Deterministic Query Algorithms](https://o-qcblog.github.io/note/complexitytheory/Deterministic-Query-Algorithms/)), how would one incorporate randomness into this?

One way of doing this will be, along with querying the input bits, in the intermediate nodes toss a coin (can also be a biased coin) and depending on whether it is head or tail, we can choose to go to either the left or right node of the tree. The value of the coin tosses we can store as a random register r (0 for Head and 1 for Tail). 

<div class="video-container">
  <video controls>
  <source src="{{ site.baseurl }}/images/Post5/P5_1.mp4" type="video/mp4">
    Here in this example we are considering a random register of size 1 (i.e. 1 bit) and an algorithm running on input $x = 10 $
  </video>
</div>

Another way is to define a randomized decision tree as a probability distribution over deterministic decision trees.

<div class="video-container">
  <video controls>
  <source src="{{ site.baseurl }}/images/Post5/P5_2.mp4" type="video/mp4">
     Here in this example we are considering probability distribution over two deterministic trees $T_1$ and $T_2$ and the algorithm runs on input $x = 10 $
  </video>
</div>
