---
layout: default
title: "Normal coordinates on a Riemannian manifold"
---


# Normal coordinates

Working on a tangent space is generally straightforward: tangent spaces are linear and this simplifies many things. Working on manifolds can be more complicated: manifolds can be curved, and the standard notions of addition and subtraction may no longer work.

Today, we'll look at normal coordinates. These coordinates allow us to translate perturbation in $\mathbb{R}^m$ to perturbations on our manifold, and provide some sort of addition and subtraction.
Normal coordinates are constructed via the Riemannian exponential map: we can move around the tangent space and then map this movement to the manifold via the Riemannian exponential. This naturally means that the normal coordinates depend on the exponential, and therefore, on the geodesics (or alternatively: on the the affine connection or the Riemannian metric).

We define the construction of normal coordinates below and show a quick example on the orthonormal group $O(3)$.


### Normal coordinates on a surface
*See Section 10.3 in [[1]](#1),  for a detailed explanation of normal coordinates on a two-dimensional surface.*

Let $p$ be a point on a Riemannian surface $M^2$, and let
$\mathbf{e}, \mathbf{f}$ be an orthonormal frame at $p$. The map

$$(x,y) \in \mathbb{R}^2 \mapsto \Phi(x,y) := \exp_p(x\mathbf{e} + y\mathbf{f}) \in M$$

is a diffeomorphism of some neighborhood $0$ in $\mathbb{R}^2$ onto some
neighborhood of $p$ in $M$. Namely, we have the differential $\Phi_*$ at
$0$:

$$\left.\frac{\partial}{\partial x}\right|_{(x,y) = 0}\! \Phi(x,y) = \left. \frac{\partial}{\partial x} \right|_{x=0} \exp_p(x\mathbf{e}) = \mathbf{e} \implies \Phi_*\left(\frac{\partial}{\partial x}\right)=\mathbf{e},$$

and similarly
$\Phi_*\left(\frac{\partial}{\partial y}\right) = \mathbf{f}$. Hence,
$\Phi$ is a local diffeo and $(x,y)$ map to local coordinates near
$p$. These are the **normal coordinates** with origin $p$.


This formulation can also be extended to higher-dimensional Riemannian
surfaces $M$. We let $T_pM$ be the $n$-dimensional tangent space at $p$.
The normal coordinates are defined in $M$ but are parametrized by
coordinates in $\mathbb{R}^n$. Hence, we require an isomorphism from a
neighborhood $0$ in $\mathbb{R}^n$ onto the tangent space $T_pM$,

$$E_p: \mathbb{R}^n\to T_pM,$$ 

for example defined by any basis of the
tangent space. We furthermore require the Riemannian exponential

$$\exp_p: T_pM\supset V\to M,$$ 

where $V$ is an open neighborhood in
$T_pM$ containing $0$.

The coordinates in $\mathbb{R}^m$ can then be used to define local
coordinates in $M$ near $p$, via the composite mapping

$$\Phi_p:= \exp_p \circ~E_p: \mathbb{R}^n\to U\subset M.$$ 

Note that we introduced an open subset $U\subset M$. The exponential map is only a
local diffeomorphism, and $U$ is defined precisely such that $\exp_p$
remains a diffeomorphism between $U$ and $V$. Note that $U$ depends on
$p$ and we should technically write $U_p$. Normal coordinates are
typically written using the inverse of $\Phi$, so we'll give it a
special character $\varphi$,

$$\varphi_p:=\Phi_p^{-1} = E_p^{-1}\circ\exp_p^{-1}: U\to\mathbb{R}^n.$$




### Example: $O(3)$

We consider the orthonormal group
$O(3)=\\{X\in \mathrm{GL}(3) : X^T X = XX^T = I\\}$.

Recall that the general linear group $\mathrm{GL}(3)$ consists of all
$3\times 3$ invertible matrices. The tangent space at $X$ is defined as

$$T_XO(3) = \left\{X\xi^T|\xi^T+\xi=0\right\},$$ 

or we could say that
$\xi\in\mathfrak{so}(3)$. We adopt the Riemannian metric
$g_X(X\xi, X\eta) = \mathrm{Tr}(\xi^T\eta)$, where
$\xi,\eta\in\mathfrak{so}(3)$. The Riemannian exponential is defined as

$$\begin{split}
    \exp_X: &~T_XO(3)\to O(3) \\
    &~X\xi\mapsto X\mathrm{Exp}(\xi),
\end{split}$$ 

where $\mathrm{Exp}(\cdot)$ is the matrix exponential.



#### Normal coordinates

The tangent space is three-dimensional, and we will construct an
isomorphism between $\mathbb{R}^3$ and $T_X O(3)$ via the hat map. The
hat map is itself an isomorphism between $\mathbb{R}^3$ and
$\mathfrak{so}(3)$: 

$$\begin{split}
    \hat\cdot: &~ \mathbb{R}^3\to\mathfrak{so}(3) \\
    &~\widehat{(x, y, z)} \mapsto\begin{bmatrix}
        0 & -z & y \\ z & 0 & -x \\ -y & x & 0
    \end{bmatrix}.
\end{split}$$ 

Subsequently, we define $E_X:\mathbb{R}^3\to T_XO(3)$ as
$E_X(x, y, z)=X\widehat{(x, y, z)}$. The exponential mapping was already
defined previously. 

Combining all terms, we have
$$\Phi_X(x, y, z) = X\mathrm{Exp}(\widehat{(x, y, z)}),$$ which tells us
how $x, y, z$ translate to local coordinates in $M$ near $X$.


#### Boxplus and boxminus

Using normal coordinates, perturbations in $\mathbb{R}^n$ can be
translated to perturbations on $M$. This is achieved by defining two
operations, *boxplus* $\boxplus$ and *boxminus* $\boxminus$
[[2]](#2), which are a generalization of classical
addition and subtraction. We let $p, q\in M$ and $u\in\mathbb{R}^n$. We
have 

$$\begin{split}
        \boxplus:&~M\times \mathbb{R}^n \to M ,\\
        &~(p, u) \mapsto p \boxplus u = \Phi_p(u);\\
        \boxminus:&~M\times M\to\mathbb{R}^n, \\
        &~(q, p) \mapsto q \boxminus p = \varphi_p(q).
    \end{split}$$

The $\boxplus$ indicates how a perturbation in $\mathbb{R}^{n}$
translates to a perturbation on the manifold, via the normal
coordinates. The $\boxminus$ shows the opposite: given two points on the
manifold and the normal coordinates, to which perturbation in
$\mathbb{R}^n$ does this correspond?

For $O(3)$, we can use the above definition of $\Phi$ and its inverse to
define the $\boxplus$ and $\boxminus$. This requires the matrix
logarithm $\mathrm{Log}(\cdot) = \mathrm{Exp}^{-1}(\cdot)$ and the
inverse $\check\cdot$ of the hat map $\hat\cdot$.

We let $X, Y\in O(3)$ and $u=(u_1, u_2, u_3)\in \mathbb{R}^3$. We thus
find 

$$\begin{split}
        X \boxplus u &= \Phi_X(u) = X\mathrm{Exp}(\hat u), \\
        Y \boxminus X &= \varphi_X(Y) = \check{}~\mathrm{Log}(X^T Y).
    \end{split}$$

(Note the $\check\cdot$ in the last equation; the formatting didn't work out. It acts on the logarithm.)


#### References
<a id="1">[1]</a> 
Frankel, T. (2011). The geometry of physics: an introduction. Cambridge university press.

<a id="2">[2]</a> 
Hertzberg, C. A Framework for Sparse, Non-Linear Least Squares Problems on Manifolds.

