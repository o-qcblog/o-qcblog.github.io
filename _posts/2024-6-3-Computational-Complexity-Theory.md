---
layout: post
mathjax: true
title: "Computational Complexity Theory"
categories: [Note, ComplexityTheory]
---

*What is computation? In loose terms computation is making a physical device (a computer) do some task for us. Things that as hard for humans can be easily done on a computer. So, can computers do anything and everything? Are there things that are hard even for computers? If so, how to quantify the hardness? Computational complexity theory trys to answer these and even more intreguing questions. I wish to give a really short bird's eye view of the field in this blog post.*

Computational complexity theory is the study of the inherent hardness or easiness of computational task. Given a task, the field of Algorithms tries to give a clever way of doing that task. There are multiple algorithms for doing the same task. On the other hand Complexity Theory is interested in giving bounds on a computational task such that no matter how clever one is, for a given task, they can never come up with an algorithm better then this bound. 

Computational complexity theory field can be broudly classified into two parts. 

Structural complexity deals with high-level complexity questions. To name a few, it deals with questions like: Is space a more powerful resource than time? Does randomness enhance the power of efficient computation? Is it easier to verify a proof than to construct one? etc. 
So far we do not know the answers to many of these questions; thus most results in structural complexity are conditional results that rely on varipus unproven assumptions like $P \neq NP$

Concrete complexity or circuit complexity as opposed to structural complexity is essentially a low- level study of computation. It deals with established lower bounds on the computational complexity of specific problems, like multiplication of matrices or detecting large cliques in graph or sorting a list (future blog link). It typically centers around particular models of computation such as decision trees, branching programs, boolean formulas, various classes of boolean circuits, and the like. This line of research aims to establish unconditonal lower bounds, which rely on no unproven assumptions. 

In the future you can hope to find individual blog post on each of the above stated examples and models of both structural and concrete complexity:)