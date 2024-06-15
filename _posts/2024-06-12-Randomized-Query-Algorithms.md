---
Layout: post
mathjax: true
title:  "Randomized Query Algorithms"
categories: [Note, ComplexityTheory]
---

*Like many other models of computation, can we add the power of randomization to decision trees? Can this reduce the number of queries? This blog post discusses randomized query algorithm, introducing it from two different lenses.*

Given that we are familiar with decision trees (if not, check out my post on [Deterministic Query Algorithms](https://o-qcblog.github.io/note/complexitytheory/Deterministic-Query-Algorithms/)), how would one incorporate randomness into this?

One way of doing this will be, along with querying the input bits, in the intermediate nodes toss a coin (can also be a biased coin) and depending on whether it is head or tail, we can choose to go to either the left or right node of the tree. The value of the coin tosses we can store as a random register r (0 for Head and 1 for Tail). 

<div class="video-container">
  <video controls>
  <source src="{{ site.baseurl }}/images/Post5/P5_1.mp4" type="video/mp4">
  </video>
</div>

Here, in this example, we are considering a random register of size 1 (i.e. 1 bit) and an algorithm running on input $x = 10 $

Note that you can choose to toss the coin at any node and at any number of times. You may also choose not to toss at all at a particular level of nodes.

Another way is to define a randomized decision tree as a probability distribution over deterministic decision trees. All the trees that occur with a non zero probability is called trees *in support of* the randomized algorithm.

<div class="video-container">
  <video controls>
  <source src="{{ site.baseurl }}/images/Post5/P5_2.mp4" type="video/mp4">
  </video>
</div>

Here, in this example, we are considering probability distribution over two deterministic trees $T_1$ and $T_2$ and the algorithm runs on input $x = 10 $

<div class="hint-box info">
  <div class="hint-box-header">
    <strong> Pause and ponder: These two interpretations are equivalent. Guess why?</strong> 
    Click to expand
  </div>
  <div class="hint-box-content">
    Depending on the value of the random bit, either the subtree on the left $T_1$ (say) or right $T_2$ (say) will be evaluated. If $r_1$ can be 0 or 1 with equal probability, then $T_1$ and $T_2$ can be thought of as coming from a uniform probability distribution from {$T_1$, $T_2$}. By induction, we can see this equivalence for random bits of any size.
  </div>
</div>

We say that a randomized decision tree computes $f$ with bounded-error if its output equals $f(x)$ with probability at least 2/3, for all $x \in ${0,1}$^n$. 

Formally, going by the first interpretation, we can view a randomized decision tree as one with input, not just $x$ but $(x,r)$ where $r$ is $k$ bit random string. (so there are $2^k$ possible random string). The randomized algorithm $A(x,r)$ computes $f$ if $A(x,r) = f(x)$ for all $x$ and for most ($> 2/3$) of the $r$.

Now we need to come up with a notion of randomized querry complexity. For randomized algorithms, we have two reasonable options for defining the worst-case number of queries:

One option is to take the worst case of $height(D,x)$ over both decision trees $D$ in the support of $R$ and over inputs $x$. The other option is to take the worst case of $\mathbb{E} [height(R, x)]$, expectation value computed over the deterministic trees in support of R.

**Definition:**

$height(R) = \max_x \max_D path(D,x)$

$\overline{height(R)} = \max_x \mathbb{E} [height(D, x)] $

here $D$ is a Deterministic decision tree such that $D$ computes $f$ and $D$ is in support of $R$.

When we relax the *cost* (*how we count the worst case queries?*) but not the *correctness* (*how much error we allow?*):

**Definition:**
Zero error randomized algorithm, $R_0(f)$, is defined as 
    
$R_0(f) = \min_R \overline{height(R)}$ 
    
such that $R$ computes $f$ with zero error. (Las Vegas algorithm)


When we relax the correctness but not the cost:

**Definition:**

$ R_{1/3}(f) = \min_R height(R)$
    
here $R$ is such that it computes f with error $\epsilon \leq \frac{1}{3}$ (Monte Carlo algorithm)
    
Note that at $\epsilon = 1/2$, this error can be achieved via randomly guessing $f(x)$ without reading the input at all. This means that to get a nontrivial new measure, we should pick $\epsilon \in (0, 1/2)$. As it turns out, within that range, we can move from one error level to another by amplifying: we can repeat a high-error algorithm several times on the same input $x$, take the majority vote of the outputs, and get an estimate for $f(x)$ whose error is smaller than the original error level.

## References

[Shalev Ben-David. Query complexity basis. Lecture notes.](https://cs.uwaterloo.ca/~s4bendav/CS860S20.html)

[Harry Buhrman and Ronald de Wolf. Complexity measures and decision tree complexity: a survey. In: Theoretical Computer Science, 288.1, 2002.](https://dl.acm.org/doi/10.1145/502090.502097)

[Rajat Mittal. Decision tree complexity. Lecture notes](https://www.cse.iitk.ac.in/users/rmittal/prev_course/f21/reports/4_dt.pdf)

