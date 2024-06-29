---
layout: post
mathjax: true
title: "Pebbling a Checkerboard"
categories: [Puzzle, Algorithms]
---
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Pebbling a Checkerboard",
  "description": "A problem from the textbook Sanjoy Dasgupta, Christos H. Papadimitriou, and Umesh Vazirani. 2006. Algorithms (1st. ed.). McGraw-Hill, Inc., USA.; Chapter 6, problem 6.5. I have rephrased the problem and provided an elaborate solution.",
  "author": {
    "@type": "Person",
    "name": "Padmapriya S"
  },
  "datePublished": "2024-05-29",
  "image": "https://o-qcblog.github.io/images/Post1/P1_1.png",
  "publisher": {
    "@type": "Organization",
    "name": "Quanta on Computing",
    "logo": {
      "@type": "ImageObject",
      "url": "https://raw.githubusercontent.com/o-qcblog/o-qcblog.github.io/master/images/logo.png"
    }
  }
}
</script>


*A problem from the textbook [Sanjoy Dasgupta, Christos H. Papadimitriou, and Umesh Vazirani. 2006. Algorithms (1st. ed.). McGraw-Hill, Inc., USA.](https://dl.acm.org/doi/10.5555/1177299#cited-by-sec); Chapter 6, problem 6.5. I have rephrased the problem and provided an elaborate solution.*

### Puzzle
After a long day of work, you and your friend go to a cafe. There is a checkerboard on the cafe table. Some pebbles lie around to enhance the ambience. Seeing this, your friend challenges you with a task. She is willing to bear a huge chunk of the bill depending on how well you complete the task. You, who love taking up challenges, readily agree. 

[<img src="{{ site.baseurl}}/images/Post1/P1_1.png" alt="" width="600" />]({{ site.baseurl}}/)

The checkerboard is of dimension $4 \times n$, and there are $2n$ pebbles at your disposal. Your friend writes an arbitrary integer on each square of the checkerboard. She challenges you to place these pebbles, one on each square, but on the condition that no two pebbles can be on horizontally or vertically adjacent squares (diagonal adjacency is fine). She is willing to pay a bill equivalent to the sum of integers written on the squares you tailed using these pebbles. 

You realise that the $n$ is too big. You are very hungry and can not afford to solve the puzzle slower than running a linear time algorithm to solve it. How can you write a clever algorithm and make a hearty meal?

<div class="hint-box info">
  <div class="hint-box-header">
    <strong>Hint:</strong> Click to expand.
  </div>
  <div class="hint-box-content">
    Consider just one column and enumarate the number of possible pebbling. Now think about which two can come adjacent..... 
  </div>
</div>

### Solution

Let's first look into what legal patterns that can occur in any column (in isolation, ignoring
the pebbles in adjacent columns).
8 patters are possible:

1 is leaving the blocks empty:

[<img src="{{ site.baseurl}}/images/Post1/P1_2.png" alt="1" width="60" />]({{ site.baseurl}}/)


3 patters with 2 pebbles:

[<img src="{{ site.baseurl}}/images/Post1/P1_3.png" alt="2" width="60" />]({{ site.baseurl}}/)
[<img src="{{ site.baseurl}}/images/Post1/P1_4.png" alt="3" width="60" />]({{ site.baseurl}}/)
[<img src="{{ site.baseurl}}/images/Post1/P1_5.png" alt="4" width="60" />]({{ site.baseurl}}/)

4 patterns with 1 pebble:

[<img src="{{ site.baseurl}}/images/Post1/P1_6.png" alt="5" width="60" />]({{ site.baseurl}}/)
[<img src="{{ site.baseurl}}/images/Post1/P1_7.png" alt="6" width="60" />]({{ site.baseurl}}/)
[<img src="{{ site.baseurl}}/images/Post1/P1_8.png" alt="7" width="60" />]({{ site.baseurl}}/)
[<img src="{{ site.baseurl}}/images/Post1/P1_9.png" alt="8" width="60" />]({{ site.baseurl}}/)


Now let us call two patterns compatible if they can be placed on adjacent columns to form a legal placement.

A natural way of solving any big problem is to look at smaller subproblems. These smaller problem may or may not be exactly the same as the actual problem. Such an algorithmic technique which considers subproblems whose solution is used in solving the bigger problem is called [Dynamic Programming](https://o-qcblog.github.io/note/algorithms/Dynamic-Programming/). 

Here the most intutive way of making the problem smaller is by reducing the size of the checkerboard. So, let us consider the subproblems consisting of pebbling the first $k$ columns ($1 \leq k \leq n$) of the checkerboard. Each subproblem can be assigned a type, which is the pattern occurring in the last column.

Let $C_j[k] =$ optimal value achieved by pebbling columns 1 to $k$ such that the final column is type $j$ ($j \in ${$1,2 \dots 8$} i.e one among the above 8 patterns). 

One important step in dynamic programming or recursion is to give the base case. Here $C_j[0] = 0$ for all $j$.

We want to maximise the sum. So we need to find maximum over all possible $j\prime$ on the i th column, that are compatable with the $j$ in $i+1$ th column. 

$C_j[i+1] =$ max {$ value ( C_{j, i+1}) + C_{j\prime}[i] $}

Where $value( C_{j, i+1})$ is the value of square(s) covered by $j$ in column $i+1$.

Note that the maximum is over all $j\prime =$ all columns compatible with $j$ and for each pattern there are only constant number of patterns compatible with it. So this running over all compatible $j\prime =$ costs $O (1)$.

We need to return $max_j$ $C_j[n]$. Which involves computing $C_j[i]$ for all $i$ from 1 to $n$. Therefore computing $C_j[n]$ is $O (n)$. Again max over $j$ just takes constant number of steps.

This completes our linear time algorithm:) Now you can have a hearthy meal!

