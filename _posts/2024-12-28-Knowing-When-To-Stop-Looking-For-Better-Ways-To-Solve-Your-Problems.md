---
layout: post
mathjax: true
title: "Knowing When to Stop Looking for Better Ways to Solve Your Problems"
categories: [Note, ComplexityTheory]
---

*Given any problem, is it always possible to develop better or faster methods to solve it? Is there such a thing as the best method for solving a problem? If so, how can one determine which method is the best? And finally, when should one decide to stop searching for an even better or faster way to get to the solution?*

This blog offers an intuitive and engaging introduction to various lower-bounding techniques, presented in a playful and interactive manner that anyone—even without a mathematical background—can grasp. The follow-up post will delve into the mathematics behind elegant lower-bounding techniques that demonstrate, for a given problem, that no matter how clever one may be, it is impossible to surpass these fundamental limits. The art of giving lower bounds...

<div class="hint-box info">
<div class="hint-box-header"> For those who are not familiar with time complexity… (Click to expand) </div>
<div class="hint-box-content"> First of all, what is fast or slow? How to quantify time when it comes to computing? There are many ways to do this, but for us, time is the number of basic operations or steps needed to get to the solution. If your problem instance grows in size intuitively, for most cases, the number of steps needed to get to the solution also increases, right? To capture this dependence, we give the number of steps to solve a problem in terms of its input size (generally denoted as n). This quantity is called the time complexity.
    For the same problem, we could have a very dumb way of solving it that takes a zillion steps to get to the solution. At the same time, we might have a very clever way of solving this problem in just 10 steps. Thus, for a given problem, we can have many different algorithms with varied time complexities. 
</div>
</div>

Let’s start with a game. I have a number in mind (it is between 1 and 10,000), and you can ask me questions of the following and try to guess the number:
-	Is the number greater than equals x? >x
-	Is the number lesser than equals x? <x
-	Is the number equal to x? =x
Your task is to guess the number with the least number of questions. In particular, you win if you can find the number with just 14 questions or less. (14? By the end of this post, you will find where this number came from)

[Click here to play the Number Guessing Game](https://colab.research.google.com/drive/1Fb1I63PiL3OfgLemvOG5eEtXrYf9PybF#scrollTo=V0XzR_rS-OoT){:target="_blank"}

If you took a moment to play the game and returned, how did it go? Were you able to win? If so, what clever strategy did you use to guess the number *efficiently*?

An intuitive strategy is to try to decrease your space of possible numbers. So, one tends to ask questions such that one can throw away a large chunk of numbers. That is, asking the question if the number = 1, =2, or = 3, and so on, is very bad. At each step, all we manage to do is discard 1 number at a time from being a possible candidate. 

<div class="image-container">
  <img src="{{ site.baseurl}}/images/Post8/P8_1.png" alt="" width="600" class="zoom-image">
</div>

But how much can you throw away at a step? Can you be greedy and try to get rid of almost 90% of the possible candidates?

For that, let's plan another game. Here, you can choose any number you want to (between 1 and 10,000). Now I (actually, the computer) will try to guess the number.

[Click here to play the Guess Blocker Game](https://colab.research.google.com/drive/1aWgp8chhEYukRO7a4w37oTMuFiXAvL7F?usp=sharing){:target="_blank"}

One cunning strategy to pick a number is, to not pick at all! At every step, you can make sure to reduce the search space as little as possible and be consistent with your answers. Every time someone asks a question like “Is the number <= 70?” and hopes to get rid of all numbers below 70. Here, you can just say no and only reduce the search space by 30. You can go one like this and choose your number at the end, just making sure your answers are consistent.

<div class="image-container">
  <img src="{{ site.baseurl}}/images/Post8/P8_2.png" alt="" width="600" class="zoom-image">
</div>

Now, to your surprise, just the above two games you played and the strategy you used can be translated to a rigorous mathematical proof that no matter how clever one is, at least log_2(n) (here n = 10,000, so log_2(n)= 14. There we get our 14!) questions are needed to guess the number. (No matter whether you have an honest or cunning person at the other end).

The next blog post will present this rigorous but elegant mathematical proof to lower the number of steps needed to solve this. Those methods are not just useful for this problem but can be generalized and used for a large class of problems. 

<html>
  <head>
    <title>Knowing When to Stop Looking for Better Ways to Solve Your Problems</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "Knowing When to Stop Looking for Better Ways to Solve Your Problems",
      "image": [
        "{{ site.baseurl}}/images/Post2/P2_1.png"
       ],
      "datePublished": "2024-12-30T08:00:00+05:30",
      "dateModified": "2024-12-30T08:00:00+05:30",
      "author": [{
          "@type": "Person",
          "name": "Padmapriya S",
          "url": "https://o-qcblog.github.io/about/"
        }]
    }
    </script>
  </head>
  <body>
  </body>
</html>

