---
Layout: post
mathjax: true
title:  "Dynamic Programming"
categories: [Note, Algorithms]
---

*This is a note on a powerful algorithmic technique called Dynamic Programming*

Dynamic programming techniques give a crafty and powerful way of designing algorithms.  The basic idea is simple: Given a problem, we break it into subproblems and solve them.

Let us consider a standard example of a dynamic programming algorithm. 


### Longest increasing subsequence

Given a sequence of positive integers $x_1, x_2, \dots x_n$, find the longest increasing subsequence i.e $x_{i_1} < x_{i_2} \dots x_{i_m}$ where $i_1 < i_2 \dots < i_m$. 

### Dynamic programming solution:

Consider the following example:

[<img src="{{ site.baseurl}}/images/Post2/P2_1.png" alt="" width="600" />]({{ site.baseurl}}/)

Here, as the size of the input is small, just by trial and error, we can see that the longest increasing subsequence is 

[<img src="{{ site.baseurl}}/images/Post2/P2_2.png" alt="" width="600" />]({{ site.baseurl}}/)

Here all possible increasing subsequences can be:

[<img src="{{ site.baseurl}}/images/Post2/P2_3.png" alt="" width="600" />]({{ site.baseurl}}/)


<div class="hint-box info">
  <div class="hint-box-header">
    <strong>Do you notice any stark features of these arrows?</strong> 
  </div>
  <div class="hint-box-content">
    They always go from left to right. In graph theory, such a structure is called a Directed Acyclic Graph (DAG). Notice that as the arrows always go from left to right, there are no cycles in such a graph. (No arrows go from right to left to complete a cycle.)  
  </div>
</div>

Is there a better way to solve this without trial and error? Most big problems become easy if we make the problem size small. 

So, let us start by considering a smaller subproblem. Note that the subproblem does not need to be the same problem. It can be a modified new problem on a smaller size of input that ultimately leads to solving our main problem.

In this case, let us terminate our sequence at a point and talk about the longest subsequence ending at that point.

For the base case, i.e. when 𝑛=1
The longest increasing subsequence ending at index 1 is the number itself. So the length is 1.

[<img src="{{ site.baseurl}}/images/Post2/P2_4.png" alt="" width="600" />]({{ site.baseurl}}/)

Now, we can increase the value of $n$ one by one and see the length of the longest increasing sequence. 
For instance, when $n=i$, say 6 (at this point, we assume we have computed the length of the longest increasing subsequence ending at $x_i$ for all $i\leq 5$). 

[<img src="{{ site.baseurl}}/images/Post2/P2_5.png" alt="" width="600" />]({{ site.baseurl}}/)

How would one naturally go about finding the longest increasing subsequence ending at index 6? We have the number 6 at position 6. If our sequence should necessarily end at 6, then (as it is an increasing sequence) all numbers to the left of 6 in the sequence shoule be $x_i < 6$. So, either 3, 2 or 5 can come before 6. We want to get the longest sequence possible.

[<img src="{{ site.baseurl}}/images/Post2/P2_6.png" alt="" width="600" />]({{ site.baseurl}}/)

So, it makes sense to pick 3 as it has the longest subsequence ending where it is. (The subsequence being 2-3-). 

Like this we can keep going and find the longest increasing subsequence ending at the last number, here $x_8 = 7$.

So, what should we output now?
