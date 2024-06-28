---
layout: post
mathjax: true
title: "School on Sundays!"
categories: [Puzzle, Miscellaneous]
---

*An Intimidating puzzle, which leads to exploring projective geometry…*

### Puzzle

You are the head of a committee in charge of making class timetables for school students. The school offers seven courses. Every day of the week (including Sundays), classes are scheduled. As the school works even on Sundays, every day is kept light with exactly three classes. 
You are asked to schedule classes so that, every day, three different courses are taught. Also, given two different days of the week, there is precisely one course common on both days, and given two different courses, there is exactly one day when both these courses are taught. Furthermore, there should be a set of 4 courses such that no three are taught on the same day. 

It seems like a monumental task! Does such a timetable exist? If so, how to make one?

### Solution

The quest for finding a solution to this puzzle takes us on a tour into the fascinating world of combinatorial design.

<div class="hint-box info">
  <div class="hint-box-header">
   Combinatorial design theory is the part of combinatorial mathematics that deals with the existence, construction, and properties of systems of finite sets whose arrangements satisfy generalized concepts of balance and/or symmetry.
  </div>
</div>

Specifically, into finite projective planes…

First, let's see what a finite projective plane is,

A *projective plane* is a set of “points” and “lines” lines such that they follow the following properties:

1.	Given two distinct points, there is exactly one line passing through it
2.	Give two distinct lines, they intersect at exactly one point 
3.	There exists a set of 4 points such that no three points are colinear.

I have put points and lines under quotation because these need not necessarily be the points and lines we are used to (That of $\mathbb{R}^2$). However, these can represent a more general quantity. 

So, more generally, a projective plane is a non-empty set $X$ (whose elements are called “points”), along with a non-empty collection $L$ of subsets of $X$ (whose elements are called “lines”).

<div class="hint-box info">
  <div class="hint-box-header">
    One example of a projective plane is an extended Euclidean plane, which is constructed from the ordinary Euclidean plane. As an exercise, try to figure out by adding what set of lines and/or points one can achieve this construction. (After thinking through, click to see how this can be done)  
  </div>
  <div class="hint-box-content">
Ordinary Euclidian plane, one can turn into the projective plane (called the extended Euclidian plane) by the following procedure:
    
1.	Consider a maximum set of mutually parallel lines. To each of such a set, associate a single new point, which is considered incident with each line in this set. These points are called *points at infinity*.
2.	Now, we need to have a line passing through the points at infinity. So, introduce a new line, which is considered to be incident with all points at infinity and no other points. This is called the *line at infinity*.
  </div>
</div>

There is a geometric way of constructing an extended Euclidean plane. Each point in the Euclidean plane $\mathbb{R}^2$ can be mapped to a geometric line in $\mathbb{R}^3$ which passes through the origin, and each line in $\mathbb{R}^2$ can be mapped to geometric plane through the origin in $\mathbb{R}^3$.

<div class="video-container">
  <video controls>
  <source src="{{ site.baseurl }}/images/Post7/Post7_1.mp4" type="video/mp4">
  </video>
</div>

Now we have some flavor of projective planes. When the number of points and lines is finite, it is called a *finite projective plane*.

A very famous example of a finite projective plane is a Fano plane.

[<img src="{{ site.baseurl}}/images/Post7/Post7_2.jpg" alt="" width="600" />]({{ site.baseurl}}/)

We can see that this satisfies all the conditions listed for the projective plane. This has a finite number of lines and points, and both are equal to 7.  

Try to make a finite projective plane with 8 or 6 lines and points. Can you make one?

Not any arbitrary number of points and lines can satisfy these properties. The next possible finite projective plane is known to have 13 points and 13 lines. (Yes! always the number of points and lines turn out to be same for a finite projective plane).

<div class="hint-box info">
  <div class="hint-box-header">
    <b> Extras! For mathematically inclined readers</b> Click to expand
  </div>
  <div class="hint-box-content">
    
  It is known that the number of lines and points is always equal for a finite projective plane (let this number be $N$). Furthermore, all lines contain the same number of points, and all points have the same number of lines incident on them. And these two numbers are equal as well! Say this number, the number of points on a line (as well as the number of lines coming from a point), is $k$. We can write $N = k^2 - k + 1$, and it is conjectured that $k-1$ has to be prime. $k-1$ is called the order of the projective plane.
    
  </div>
</div>

Larger projective planes become more challenging to draw. They are complex but pretty looking. You can try to pull the one with 13 lines and 13 points as a challenge. 

[<img src="{{ site.baseurl}}/images/Post7/P7_3.png" alt="" width="600" />]({{ site.baseurl}}/)

This is a finite projective plane with 31 lines and points. 

[<img src="{{ site.baseurl}}/images/Post7/P7_4.png" alt="" width="600" />]({{ site.baseurl}}/)

This with 91!

Now, finally, let us come back to our puzzle. What if I say the Fano plane is the solution to our puzzle? Yes! We can consider the line to be the days of the week and points to be the courses (or vice versa), and you will see all the needed conditions are satisfied!  

[<img src="{{ site.baseurl}}/images/Post7/Post7_5.jpg" alt="" width="600" />]({{ site.baseurl}}/)


## References and sources








