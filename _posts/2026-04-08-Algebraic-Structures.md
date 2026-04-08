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
- $G$ is *closed* under $*$: $g * h \in G, \forall g,h \in G$.
- $*$ is *associative*: $(g * h) * l = g * (h * l)$.
- $G$ has an *identity*: $\exists e \in G$ such that $e * g =g, \forall g \in G$.
- Every element in $G$ has an *inverse*: $\forall g \in G, \exists g^{-1} \in G$ such that $g * g^{-1}=e$.

Adding one more axion, *commutativity*, we get an *abelian group*.

##### Abelian Group  $(G,*)$
An *abelian group* is a group $(G, * )$ with $*$ being *commutative*. That is $h * g = g * h, \forall h,g \in G$.

<div class="hint-box info">
<div class="hint-box-header"> <b>Example:</b> Consider the same set $S$ from the previous example, which is a collection of all ordered pairs of real numbers of the form $(a,b)$ where $a,b \in \mathbb{R}.$ Define a binary operation $+$ such that $(a, b) + (c, d) = (a + c, b + d)$ for all $a,b,c,d \in S$. One could check that $(S, +)$ forms a group.
</div>
</div>

Groups are algebraic structures with single operation. Adding more operations to a set gives other fascinating structures.

### Lattice $(L, \lor, \land)$
A *lattice* is a set $L$ along with two binary, associative and commutative operations,  *join* denoted as $\lor$ and *meet* denoted as $\land$, such that $\forall a, b \in L$ the following is satisfied,
- *Absorption Law*: $a \lor (a \land b ) =a$ and $a \land (a \lor b ) =a$.
- *Idempotent Law*: $a \lor a = a$ and $a \land a = a$.

<div class="hint-box info">
<div class="hint-box-header"> Lattices also have an interesting place in *order theory*. Click to know more.
</div>
<div class="hint-box-content">
A <i>partially ordered set</i> $(L, \leq)$ is called a <i>lattice</i> if each two element subset $\{a,b\} \subseteq L$ has a least upper bound (<i>supremum</i>), called <i>join</i> denoted as $a \lor b$, and a greatest lower bound (<i>infimum</i>), called <i>meet</i> denoted as $a \land b$.

Some examples include:
- $L=$ Power set of a set $S$ with the partial order being set inclusion. Here join is the union of sets and meet in the intersection of sets.
- $L=$ Set of natural numbers with partial order being divisibility. Here join is the least common multiple of two natural numbers and the meet is the greatest common divisor of the two natural numbers. 

One might naturally wonder how these two definitions of lattice is connected?

Given an algebraic definition of lattice $(L, \lor, \land)$, define partial order $\leq$ on $L$ by setting $a \leq b$ if $a = a \land b$ or $a \leq b$ if $b = a \lor b$ for all $a,b \in L$. With the law of absorption one can verify that both these ways of setting $a \leq b$ are equivalent. Similarly given a partial order on $L$, $(L, \leq)$, we can define two binary, associative and commutative operations and prove that they satisfy the absorption and idempotent law.
</div>
</div>

One of the most important algebraic structure in theoretical computer science, which is a lattice, is the Boolean algebra. 

##### Boolean algebra
A *Boolean algebra* is a complemented distributive lattice with $L = \{0,1\}^n$, where $n$ is a natural number. That is in addition to join $\lor$ and meet $\land$ (also known as bitwise OR \& bitwise AND), there is another unitary operation compliment denoted as $\lnot$ and the join and meet distribute over each other. The following is satisfied for all $a\in L$,
- *Identity*: $a \lor 0^n =a$ and $a \land 1^n =a$.
- *Compliment*: $a \lor \lnot a =1^n$ and $a \land \lnot a = 0^n$.

Is element in $L$ is referred to as Boolean string or just *string*. The set $L = \{0,1\}^n$ can be represented as a *Boolean hypercube* as shown in the below figure. 

<!-- Figure -->

With two binary operations satisfying different set of axioms we get a different algebraic structure, a *ring*. Unlike lattice which are quite different from groups, a ring can be thought of adding a new binary operation to an abelian group. 

### Rings $(R, +, *)$
A *ring* is a set $R$ with two binary operations $+$ and $*$ such that,
- $(R, +)$ is an abelian group: $(R, +)$ is a group with $s + r = r + s, \forall s,r \in R$ .
- $R$ is closed under $*$: $s * r \in R, \forall s,r \in R$.
- $*$ is associative: $(s * r) * t = s * (r * t), \forall s,r,t \in R$.
- $*$ distributes over $+$: $s * (r+t) = (s * r) + (s * t), \forall s,r,t \in R$.
- Identity with respective to $*$: $\exists e \in R$ such that $s * e =e, \forall s \in R$.

Adding further axioms one gets two important types of rings: *commutative ring* and *division ring*.

- **Commutative ring**: A ring $(R, +, * )$ where $*$ is commutative, that is $s * r =r * s, \forall s,r \in R.$
- **Division ring**: A ring $(R, +, * )$ such that every element of the ring has an inverse in the ring with respect to $*$. That is $\forall r \in R, \exists r^{-1}$ such that $r * r^{-1} = e$, where $e$ is the identity element with respect to $*$ ($e * e^{-1} = e$).

In theoretical computer science, especially algebraic complexity theory, one important example of a ring that is often studied is a *polynomial ring* (also referred to as just *polynomials*).

<div class="hint-box info">
<div class="hint-box-header"> Note that the $+$ and $*$ operations are loosely referred to as "addition" and "multiplication" operations though they might not refer to the usual high school addition or multiplication.
</div>
</div>

##### Polynomial Ring (polynomials over a ring)
A *polynomial* in single variable over a ring $R$ is a *formal sum* $a_n x^n + \dots a_1 x + a_0$ where the coefficients, $a_0, \dots ,a_n$, are elements of ring $R$. The set of all polynomials in one variable over a ring $R$ is denoted as $R[x]$. This set $R[x]$ forms a commutative ring with the two binary operations being the usual addition and multiplication of polynomials. This can be generalized to multivariable forming a commutative ring $R[x_1, \dots x_m]$. 

<div class="hint-box info">
<div class="hint-box-header"> We saw Boolean algebra under lattice, surprisingly they can also be viewed as a ring. As an exercise try to see how. Click for the solution.
</div>
<div class="hint-box-content">
One tempting way to view Boolean algebra as ring might be to map $\lor$ to $+$ and $\land$ to$\ *$. But it is worth noting that in a ring $\ *$ distributes over $+$ but the other way need not hold. Whereas if we consider the above map then both $\lor$ and $\land$ distributes over each other. Note that here $\lor$ and $\land$ are bitwise OR and bitwise AND respectively. 

So to view a Boolean algebra $(B, \vee, \wedge, \neg)$ as a ring, we instead map $+$ to *XOR*. That is for all $a,b \in B$ we define the binary operation $+$ to be,
$$a + b = (a \wedge \neg b) \vee (\neg a \wedge b) = a \oplus b$$
The binary operation $*$ is define as,
$$a * b = a \wedge b$$
for all $a,b \in B$.

Note that this definition of $*$ makes it a commutative ring. Also Boolean algebra turns out to be a special ring where with following two properties,
- <i>Idempotency</i> ($x^2 = x * x = x$): If you bitwise AND a string with itself, you just get the exact same string back.
- <i>Characteristic 2</i> ($x + x = 0$): If you bitwise XOR a string with itself, every $1$ cancels out its matching $1$, resulting in all zeros. Every element is its own additive inverse.
</div>
</div>

<div class="hint-box info">
<div class="hint-box-header"> <b>Example:</b> Once again considering the $S$ of all ordered pairs of real numbers of the form $(a,b)$ where $a,b \in \mathbb{R}$, along with the binary operation $+$ such that $(a, b) + (c, d) = (a + c, b + d)$ holds for all $a,b,c,d \in S$. Note this is an abelian group. Let us try to make it a ring by adding another binary operation $*$.

There are many ways to define $*$ to make $(S,+, * )$ a ring. One non-trivial way is to define such that $(a, b) \cdot (c, d) = (ac - bd, ad + bc)$ holds for all $a,b,c,d \in S$. Checking this forms a ring is left as an exercise. 
</div>
</div>

### Fields $(F,+,*)$
A *field* is a commutative division ring. 

Equivalently one can say that $(F,+)$ and $(F,* )$ are abelian groups.

<div class="hint-box info">
<div class="hint-box-header"> Boolean algebra as fields! Click to learn more.
</div>
<div class="hint-box-content">
In abstract algebra, the set $\{0,1\}$ with XOR and AND is actually the simplest possible Field, known as the finite field of two elements, denoted as $\mathbb{F}_2$ (or $\mathbb{Z}_2$).When you look at the set $\{0,1\}^n$, you are looking at the direct product of $n$ copies of this field:$$\mathbb{F}_2 \times \mathbb{F}_2 \times \dots \times \mathbb{F}_2 = \mathbb{F}_2^n$$. While $\mathbb{F}_2$ on its own is a Field (and therefore a Division Ring), the product space $\mathbb{F}_2^n$ is not a Field. It drops down the hierarchy to become just a Commutative Ring (specifically, a Boolean Ring). This happens because it has "zero divisors." For example, 1000 $\cdot$ 0111 $=$ 0000, which means non-zero elements can multiply together to create zero, something strictly forbidden in Fields and Division Rings.
</div>
</div>

Algebraically closed fields
An *algebraically closed field* is a field such that the polynomials in $F[x]$ have all their roots in $F$. Note that this is equivalent to saying that all polynomials in $F[x]$ factorizes into linear factors. 

When a particular field is not algebraically closed then mathematicians like to "extend" the field to make it algebraically closed. For example in $\mathbb{R}$ the polynomial $x^2 +1$ does not have roots. But we can extent the reals making a new field of complex numbers where  $x^2 +1$ is algebraically closed. This is called *field extensions*.

##### Polynomial Ring (polynomials over a field) 
We already saw polynomial rings, where the polynomials has its coefficients as elements of a ring. Recall that rings do not demand the existence of inverses. As long as we wish to talk about the usual addition and multiplication of polynomials this structure is enough. But in order to make sense of polynomial division (computing greatest common divisor (gcd) of two polynomials) we have to define polynomials over a field $F$. 

The set of all single variable polynomials over a field $F$ is denoted as $F[x]$, which again forms a commutative ring under usual addition and multiplication of polynomial. This can be generalized to multivariable forming a commutative ring $F[x_1, \dots x_m]$. 

Although polynomials over a field lets us talk about gcd of two polynomials, not necessarily we have inverses of all polynomials. Where as if we include rational functions this forms a field. 

<div class="hint-box info">
<div class="hint-box-header"> <b>Example:</b> Continuing the example of $(S,+,*)$, such that for all $a,b,c,d \in S$ the two binary operations are defined as,
- $(a, b) + (c, d) = (a + c, b + d)$ 
-  $(a, b) \cdot (c, d) = (ac - bd, ad + bc)$
where $S$ is the set of all ordered pairs of real numbers of the form $(a,b)$ where $a,b \in \mathbb{R}$.

To make this a valid field, let us add commutativity of $*$ as an axiom. Note that $(1,0)$ serves as identity with respect to $*$ and for every $(a, b)$ there exists an inverse with respect to $*$ which is $\left(\frac{a}{a^2 + b^2}, \frac{-b}{a^2 + b^2}\right)$. These makes $(S, +, * )$ a field.

A keen observer might note that this is none other than the field of complex numbers $\mathbb{C}$! 
</div>
</div>

<div class="image-container">
  <img src="{{ site.baseurl}}/images/Post14/Post14_1.png" alt="" width="600" class="zoom-image">
</div>

### Modules $(M,+,*)$ over a ring $R$

Consider a ring $(R,\oplus,\cdot)$ with $e$ being the identity with respect to $\cdot$, then a *left-$R$ module* $(M,+,* )$ is abelian group with respect to $+$ and the operation $*$, often referred to as *scalar multiplication*, is defined as a function $R \times M \rightarrow M$ such that $\forall r,s \in R$ and $x,y \in M$, 
- Scalar multiplication $*$ distributes over $+$ of module elements (on the left): $r * (x +y) = (r * x)+(r * y), \forall r \in R, \forall x,y \in M.$
- Scalar multiplication $*$ distributes over $\oplus$ of ring elements (on the left): $(r \oplus s) * x =(r * x) + (s * x), \forall r,s \in R, \forall x \in M.$
- Scaling is associative: $(r\cdot s) * x = r * (s * x), \forall r,s \in R, \forall x \in M.$
- Ring identity with respect to $\cdot$ is the identity for scalar multiplication $*$ (on the left): $e * x = x \forall x \in M.$

A *right-$R$ module* $(M,+,* )$ is defined exactly the same way except that the scalar multiplication is defined a function $M \times R \rightarrow M$ with all the above axioms holding but on the right. 

Note that in standard textbooks, the “addition” and “multiplication” operations of a ring (denoted here by $\oplus$ and $\cdot$) are typically not distinguished notationally from those of a module (denoted here by $+$ and $*$). In practice, the same symbols, usually $+$ and $\cdot$, are used for both structures. This abuse of notation is generally preferred for the sake of simplicity, with the intended meaning inferred from the context (namely, the objects on which the operations act).

However, this can be confusing for a new learner. For this reason, the presentation here is deliberately more pedantic, using different symbols to emphasize that these operations act on fundamentally different objects. In this case, a ring and a module.

A module can be left and right modules of two different rings simultaneously. These are called $(L,R)$-bimodule, where $L$ and $R$ are the corresponding rings. When the module is over a commutative ring $R$ then by default it becomes $(R,R)$-bimodule, referred to as $R$-module.

<!-- Example-->

<!-- Close Example-->
### Vector space $(V, +, *)$ over a field $F$
Consider a field $(F,\oplus,\cdot)$ with $e$ being the identity with respect to $\cdot$, then a *vector space* $(V,+,*)$ is abelian group with respect to $+$ and the operation $*$, often referred to as *scalar multiplication*, is defined as a function $F \times M \rightarrow M$ such that $\forall r,s \in F$ and $x,y \in V$, 
- Scalar multiplication $*$ distributes over $+$ of vector space elements: $r * (x +y) = (r * x)+(r * y), \forall r \in F, \forall x,y \in V$.
- Scalar multiplication $*$ distributes over $\oplus$ of field elements: $(r \oplus s) * x =(r * x) + (s * x), \forall r,s \in F, \forall x \in V.$
- Scaling is associative: $(r\cdot s) * x = r * (s * x), \forall r,s \in F, \forall x \in V.$
- Field identity with respect to $\cdot$ is the identity for scalar multiplication $*$: $e * x = x \forall x \in M.$

A careful reader can instantly notice the similarity between modules and vector spaces. Modules are generalized vector spaces, where the scalars are elements of a ring instead of a field. $F$-module is a vector space when $F$ is a field.

<!-- Example-->

<!-- Close Example-->

Our mathematical curiosity needn't stop here. What if we add another operation to the vector space which is over a field? 
### Algebra $(A, +,\cdot,*)$ over a field $F$

Consider a field $F$. An *algebra* $(A, +,\cdot,*)$ is a vector space $(A, +,\cdot)$ over $F$ with another operation $*: A \times A \rightarrow A$ such that for all $a,b,c \in A$ and $r,s \in F$,
- $*$ left and right distributes over $+$: $a * (b +c) = (a * b) + (a * c)$ and $(a + b) * c = (a * c) + ( b * c)$.
- $*$ is *compatible* with the scalar multiplication $\cdot$: $(r \cdot a) * (s \cdot b) = (r \cdot s)\cdot (a * b)$.

When $*$ is associative, that is $a *( b * c) = (a * b) * c$, we have **associative algebra**.

<!-- Example-->

<!-- Close Example-->

<div class="image-container">
  <img src="{{ site.baseurl}}/images/Post14/Post14_2.png" alt="" width="600" class="zoom-image">
</div>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------------- -->
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
