---
layout: default
title: "A brief derivation of the Kalman filter"
---

# A brief derivation of the Kalman filter

The Kalman filter is a well-known data assimilation method. It is an algorithm that includes the observation optimally to improve the estimate of the true process. We assume linear dynamics of the true model, a linear observation model, and Gaussian process noise and observation noise.
While these simplifying assumptions sound restrictive, it permits the derivation of a closed form solution. This serves as a first step to more intricate data assimilation methods.

We start by describing the linear dynamics and illustrate some probabilistic properties of these dynamics. We then move on the Kalman filter, where we make use of *Bayesian inference in linear models with Gaussian noise*.


### Discrete-time linear dynamics
*Based on Example 4.6 from “Probabilistic forecasting and Bayesian data assimilation”.*

Consider a linear evolution equation in discrete time, \begin{equation}
    z^{n+1} = Fz^n + B + \Xi^n,
\end{equation}
where the superscripts indicate the time level. 
Here, $z^n\in\mathbb{R}^{N_z}$, $F\in\mathbb{R}^{N_z\times N_z}$ is a matrix describing how the state $z^n$ transitions to $z^n+1$, $B\in\mathbb{R}^{N_z}$ denotes additional input in the state evolution, and $\Xi^n$ is process noise.

This evolution equation is accompanied by a linear observation model (or forward model) \begin{equation}
    y^n = H z^n + \Sigma^n,
\end{equation}
where $ H\in \mathbb{R}^{N_y \times N_z}$ is the forward map, and $\Sigma^n$ is measurement noise. The values of $y^n$ are observations of the true dynamics $z^n$. Depending on the entries of $H$, these can be partial or full observations of $z^n$. 

For the derivation of the Kalman filter, we assume linear dynamics and a linear forward map $H$.
With the dynamical model and the observation model in place, the filtering problem is the following: given observations $y^0, \ldots, y^n$, estimate $z^n$.


### Noise processes
The noise processes $\{\Xi^n \}, ~\{ \Sigma^n \}$ are assumed to be Gaussian processes with mean zero and covariance matrices $Q$ and $R$, respectively. In other words, 

$$ \begin{split}
    &\mathbb{E}[\Xi^n] = 0 = \mathbb{E}[\Sigma^n], \\
    & \mathbb{E}\left[\Xi^n (\Xi^k)^T\right] = \delta_{nk} Q, \\
    & \mathbb{E}\left[\Sigma^n (\Sigma^k)^T\right] = \delta_{nk} R.
    \end{split}
$$ 

The noise processes are also uncorrelated to the states $z^n$, $y^n$, a property which will simplify our derivations below.

### Evolution of mean and covariance
The initial system state is assumed to be Gaussian, fully described by the mean and covariance. We take
\begin{align}
    \begin{split}
        &\mathbb{E}[z^0] = \bar{z}^0, \\
        &\mathbb{E}[(z^0 - \bar{z}^0)(z^0 - \bar{z}^0)^T] = P^0.
    \end{split}
\end{align}
We now show how the mean and the covariance evolve under the linear dynamics. We will repeatedly use the linearity of the expectation $\mathbb{E}[\cdot]$ and the independence of the noise process.

For the mean $\bar z^{n+1}$, we find \begin{equation}
    \bar z^{n+1} = \mathbb{E}[z^{n+1}] = \mathbb{E}[F z^n + B^n + \Xi^n] = F \bar{z}^n + B^n.
\end{equation}
This also shows us that $z^{n+1} - \bar z^{n+1} = F(z^n - \bar z^n) + \Xi^n$, which comes in handy for the covariance evolution.
The evolution of the covariance follows from 

$$
\begin{split}
    P^{n+1}&=\mathbb{E}\left[(z^{n+1} - \bar{z}^{n+1})(z^{n+1} - \bar{z}^{n+1})^T\right] \\&= \mathbb{E}\left[\left(F(z^n - \bar z^n) + \Xi^n\right)\left(F(z^n - \bar z^n) + \Xi^n\right)^T\right] \\
    & = \mathbb{E}\left[F(z^n - \bar z^n)(z^n - \bar z^n)^T F^T\right] + \mathbb{E}\left[\Xi^n(\Xi^n)^T\right] \\
    & = F P^n F^T + Q.
\end{split}
$$

Similarly, we can derive the evolution of the mean and covariance of $y$. We have \begin{equation}
        \bar y^{n+1} = \mathbb{E}[y^{n+1}] = \mathbb{E}[H z^n + \Sigma^n] = H \bar{z}^n 
\end{equation}
for the mean and \begin{equation}
        \mathrm{cov}(y^n, y^n) = \mathbb{E}\left[\left(H(z^n - \bar{z}^n) + \Sigma^n\right)\left(H(z^n - \bar{z}^n) + \Sigma^n\right)^T\right] = H P^n H^T + R
\end{equation}
for the covariance.




## The Kalman filter
*Based on Section 6.1 of "Probabilistic forecasting and Bayesian data assimilation".*

### Derivation
The mean and covariance are propagated over one or more time steps via the linear dynamics. The propagated mean and variance define a multivariate normal distribution, which we will call the forecast pair $(\bar z^f, P^f)$. Note that the superscript will be used to distinguish between the forecast and analysis pairs; it does not indicate a time instance now.

We assume now that we have arrived at the point in time when a new observation becomes available. The Kalman filter provides an algorithm to transform incorporate this observation into the forecast pair and, in doing so, compute the analysis pair. 

The observation is denoted by $y_\mathrm{obs}$ and recall that $y_\mathrm{obs}\sim\mathcal{N}(H\bar z^f, R)$. Substituting this into the posterior update for linear dynamics and normally distribution noise (see [Bayesian inference]({% link _posts/2025-06-17-bayesian-inference.md %})), 
we obtain the analysis pair $(\bar z^a, P^a)$,

$$
\begin{split}
    \bar z^a &= \bar z^f - P^a H^TR^{-1}(H\bar z^f-y_\mathrm{obs}), \\
    P^a &= ((P^f)^{-1} + H^T R^{-1} H)^{-1}.
\end{split}
$$

The equation for the analysis covariance still needs some work. Using the [Woodbury matrix identity](https://en.wikipedia.org/wiki/Woodbury_matrix_identity),
this can be rewritten to \begin{equation}
    \begin{split}
        P^a &= P^f - P^fH^T(R+HP^fH^T)^{-1}HP^f \\
        & = P^f - KHP^f.
    \end{split}
\end{equation}
The last step introduced a matrix $K$. This is the *Kalman gain matrix* defined as \begin{equation}
    K = P^fH^T(R+HP^fH^T)^{-1},
\end{equation}
This matrix tells us how strongly the forecast pair should be corrected based on the observation. The update for the mean can also be written using $K$, which highlights the correction strength (innovation): \begin{equation}
    \bar z^a = \bar z^f - K\underbrace{(H\bar z^f - y_\mathrm{obs})}_{-\text{innovation}}.
\end{equation}


### Posterior update algorithm
Summarizing, the Kalman filter transforms the prior to the posterior in to simple steps when a new observation becomes available. Using the notation introduced above, these steps are: 
1. Compute the Kalman gain matrix, 

$$ K = P^fH^T(R+HP^fH^T)^{-1}; $$

2. Update the mean and covariance

$$ \begin{split} z^a &= \bar z^f - K(H\bar z^f - y_\mathrm{obs}), \\
    P^a &= P^f - KHP^f. \end{split}
$$
