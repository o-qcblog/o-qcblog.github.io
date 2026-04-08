---
layout: post
mathjax: true
title: "Algebraic Structures"
categories: [Note, Mathematics]
---
*This blog offers a concise overview of several algebraic structures commonly encountered in theoretical computer science and graduate-level mathematics. It is intended as a convenient reference for essential definitions, while also providing insight into the relationships among these structures.*

Algebra is a broad field of study in mathematics. The Wikipedia definition of algebra is, "a branch of mathematics that deals with abstract systems, known as algebraic structures, and the manipulation of expressions within those systems". Starting with the very fundamental object in mathematics, a *set*, interesting and useful *algebraic structures* are formed by embellishing it with *operations* and *axioms*.

An *algebraic structure* consists of three things:
- a *non-empty set* $S$,
- a collection of *operations* on $S$ and
- a finite set of *axioms* that these operations satisfy.

The notion of *set* is very fundamental to mathematics and giving a precise definition of a set is challenging. While the other two italicized words are easier to define and understand. An $\alpha$-ary *operation* on a set $S$ is a function $S^\alpha \rightarrow S$ where $\alpha$ is an *ordinal*. When $\alpha \in \mathbb{N}$, the operation is said to be *finitary*, one that takes finitely many arguments. Axioms on these operations are mathematical statements about them that are given to be true.

Returning to sets, a set is itself a mathematical object, often described informally as a collection of mathematical objects. Of course, this raises a natural question: what exactly is a “mathematical object”? Exploring this question leads to a rich and fascinating history, culminating in the development of *axiomatic set theory*. But for the purposes of this blog post, it is sufficient to work with this intuitive understanding of a set as a collection of objects.

### Sets $S$
A *set* can be seen as an algebraic structure with no operations.

<div class="hint-box info">
<div class="hint-box-header"> <b>Example:</b> $S$ be a collection of all ordered pairs of real numbers of the form $(a,b)$ where $a,b \in \mathbb{R}.$
</div>
</div>

Adding to a set a single binary operation with some axioms gives a *group*. 

Note that there are various other simpler and more general algebraic structure than the group. But here we will only look at the ones that are frequently encountered in theoretical computer science.

### Groups $(G,*)$
A *group* is a set $G$ along with a binary operation $*$ such that,
- $G$ is *closed* under \*: $g * h \in G, \forall g,h \in G$.
- \* is *associative*: $(g*h)*l = g*(h*l)$.
- $G$ has an *identity*: $\exists e \in G$ such that $e *g =g, \forall g \in G$.
- Every element in $G$ has an *inverse*: $\forall g \in G, \exists g^{-1} \in G$ such that $g*g^{-1}=e$.

Adding one more axion, *commutativity*, we get an *abelian group*.

##### Abelian Group  $(G,*)$
An *abelian group* is a group  $(G,*)$ with $*$ being *commutative*. That is $h*g = g*h, \forall h,g \in G$.


<html>
  <head>
    <title>Algebraic Structures</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "Algebraic Structures",
      "image": [
        ""
       ],
      "datePublished": "2026-04-08T08:00:00+05:30",
      "dateModified": "2026-04-08T08:00:00+05:30",
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
