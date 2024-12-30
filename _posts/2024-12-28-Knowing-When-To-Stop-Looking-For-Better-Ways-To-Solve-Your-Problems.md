---
layout: post
mathjax: true
title: "Knowing When to Stop Looking for Better Ways to Solve Your Problems"
categories: [Note, ComplexityTheory]
---

*Given any problem, is it always possible to develop better or faster methods to solve it? Is there such a thing as the best method for solving a problem? If so, how can one determine which method is the best? And finally, when should one decide to stop searching for an even better or faster way to get to the solution?*

This blog post explores elegant lower-bounding techniques that demonstrate, for a given problem, that no matter how clever one may be, it is impossible to surpass these fundamental limits. The art of giving lower bounds...

Let’s start with a game. I have a number in mind (it is between 1 and 10,000), and you can ask me questions of the following and try to guess the number:
-	Is the number greater than equals x? >x
-	Is the number lesser than equals x? <x
-	Is the number equal to x? =x
Your task is to guess the number with the least number of questions. In particular, you win if you can find the number with just 14 questions or less. (14? By the end of this post, you will find where this number came from)

<iframe src= "https://mybinder.org/v2/gh/o-qcblog/o-qcblog.github.io/tree/master/_codes/HEAD?labpath=voila%2Frender%2F_codes%2FPost8_InteractiveCode1.ipynb" ></iframe>

