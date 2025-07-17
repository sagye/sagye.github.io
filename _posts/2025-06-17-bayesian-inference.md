---
layout: default
title: "Bayes' theorem and Bayesian inference"
---

# Bayes' theorem and Bayesian inference

Bayes' theorem is a powerful mathematical tool that helps us say something meaningful about a process $Z$ when we have (possibly partial) observations of this process. We denote the observation process by $Y$. We assume that the $Z$ and $Y$ are subject to independent sources of uncertainty. We want to optimally use the observations to gain, or *infer*, knowledge about the process $z$, while simultaneously accounting for the uncertainties. This is where Bayes' theorem comes in.

We will describe how Bayes' theorem is used to determine the distribution of the true process based on the observation, and provide a simple example for linear dynamics and Gaussian noise. This will show us, in a simple way, how to compute the *posterior distribution* - we'll get to that!

Bayesian inference uses probability to quantify uncertainties, requiring us to view particular values $z$ and $y$ as realizations of random variables. Hence, we also have to think in terms of *distributions*. The random variables $Z$ and $Y$ respectively have probability distribution functions (PDFs) $\pi_Z$ and $\pi_Y$. We'll see how these distributions are related to each other and to the observation noise.



## General inference model

The observations $y$ of a process $z$ are given through a *forward map* $h$, which in total defines a *forward model*. A general forward model can be written as

$$
y = h(z) + \Xi,
$$

where $y \in \mathbb{R}^{N_y}$ is the observed variable, $z \in \mathbb{R}^{N_z}$ is the true state and $\Xi$ is observation noise. Here, $h$ is a continuous forward map, not necessarily linear.

The observation noise $\Xi$ also has a PDF denoted by $\pi_\Xi$. This PDF, along with that of $Z$, will help us find an expression for the PDF of $Y$. Namely, the PDF of $Y$, conditional to $Z = z$, is given by

$$
\pi_Y(y|z) = \pi_\Xi(y - h(z)).
$$

Loosely speaking, this can be thought of as the probability of observing the value $y$, provided that $z$ is the true state. Alternatively, you can think of this as the probability of the observation noise $\Xi$ equaling $y - h(z)$.

The joint distribution $\pi_{ZY}$ of $(Z, Y)$ is given by

$$
\pi_{ZY}(z, y) = \pi_Y(y|z)\pi_Z(z).
$$

The distribution of $Y$ is then found by marginalizing:

$$
\pi_Y(y) = \int_{\mathbb{R}^{N_x}} \pi_Y(y|z)\pi_Z(z)\, \mathrm{d}z = \int_{\mathbb{R}^{N_x}} \pi_\Xi(y - h(z))\pi_Z(z)\, \mathrm{d}z.
$$



## Bayes' theorem

Given a particular observation $y_\mathrm{obs}$, 
the conditional PDF $\pi_Z(z|y_\mathrm{obs})$ tells us the likelihood of a true state $z$ given the observation. We can compute this value via Bayes' formula:

$$
\pi_Z(z|y_\mathrm{obs}) = \frac{\pi_Y(y_\mathrm{obs}|z)\pi_Z(z)}{\pi_Y(y_\mathrm{obs})}.
$$

The components of this formula are important in many data assimilation methods. We have:

- $\pi_Z(z)$: the *prior PDF*, quantifying uncertainty about $Z$ before observing $y_\mathrm{obs}$;
-  $\pi_Z(z \vert y_\mathrm{obs})$: the *posterior PDF*, quantifying uncertainty after observing $y_\mathrm{obs}$;
-  $\pi_Y(y \vert z) $: the *likelihood function* of observing $y$ given a particular value $z$;
- $\pi_Y(y_\mathrm{obs})$: the *evidence*, which is simply a normalization factor and can often be ignored.

Specifically, the last point means that

$$
\pi_Z(z|y_\mathrm{obs}) \propto \pi_\Xi(y_\mathrm{obs} - h(x))\pi_X(x).
$$

The terms *forecast* and *analysis* are also commonly used in data assimilation. These terms refer to random variables: the forecast variable gives rise to the prior, and the assimilation step (using Bayes' formula) then leads to the analysis with its marginal distribution as the posterior.



## Inference in linear models with Gaussian noise

We can get a feeling for Bayes' theorem via a simple example. We are interested in finding $\pi_Y$ in the case where $z$ and $\Xi$ are multivariate normal random variables. Here, $z$ will have mean $\bar{z}$ and covariance matrix $P$, and $\Xi$ will have mean zero and covariance matrix $R$. The forward operator is assumed to be linear and can thus be written as $h(z) = Hz$, where $H$ is a matrix of appropriate dimension.

### The evidence
While we will not use the evidence in our calculations any time soon, it is a good exercise to compute it.

Recall that the PDF of a multivariate normal distribution with mean $\bar{z}$ and covariance $P$ is of the form  

$$
    \pi_Z(z) \propto \exp\left(-\frac{1}{2}(z - \bar z)^T P^{-1} (z - \bar z)\right).
$$

We write $\propto$, since we can normalize the distribution after the calculation and the normalizing constant is not important for our current purposes. A similar expression is used for $\pi_\Xi(y - Hz)$, where we use that $\pi_\Xi$ has mean zero:  

$$
    \pi_\Xi(y - Hz) \propto \exp\left(-\frac{1}{2}(y - Hz)^T R^{-1} (y - Hz)\right).
$$

Finally, for $\pi_Y$ we compute the following:

$$    \pi_Y(y) \propto \int_{\mathbb{R}^{N_z}} \!\exp\left(-\frac{1}{2}(y - Hz)^T R^{-1} (y - Hz)\right) \times \exp\left(-\frac{1}{2}(z - \bar z)^T P^{-1} (z - \bar z)\right)\,\text{d} z.
$$

We can combine the terms in the exponents in the integrand, and denote this by $I$. We have

$$
    I = -\frac{1}{2}\left((y - Hz)^T R^{-1} (y - Hz) + (z - \bar z)^T P^{-1} (z - \bar z)\right)
$$

For symmetric matrices $C$, the identity

$$
    z^T C z - 2d^T z = (z - C^{-1}d)^T C (z - C^{-1}d) - d^T C^{-1} d
$$

can be used to simplify $I$. We write

$$
\begin{split}
    I &= -\frac{1}{2}\left\{ (z - C^{-1} d)^T c (z - C^{-1} d) - d^T C^{-1} d + y^T R^{-1} y + \bar z^T P^{-1} \bar z \right\}, \\
    C &= P^{-1} + H^T R^{-1} H, \\
    d &= H^T R^{-1} y + P^{-1}  z.
\end{split}
$$


### The posterior
The posterior distribution is of critical importance in data assimilation methods. In this simple case of a linear forward model and Gaussian noise, we can actually compute it explicitly! We assume that we have observed $y_\mathrm{obs}$, and we will use Bayes' formula to compute the posterior. This illustrates how we can use knowledge of the prior to compute the posterior.

We start by using Bayes' formula:

$$
    \begin{split}
        \pi_Z(z|y) & \propto \pi_\Xi(y - Hz)\pi_Z(z) = \exp\left(-\frac{1}{2}\left[ (y - Hz)^T R^{-1} (y - Hz) + (z - \bar z)^T P^{-1} (z - \bar z) \right]\right) \\
        & \propto \exp\left(-\frac{1}{2}(z - C^{-1} d)^T C (z - C^{-1} d)\right).
    \end{split}
$$

We recognize a multivariate normal distribution in the last line. This means that $\pi_Z(z|y_\mathrm{obs}) = \mathcal{N}(z; \mu, S)$, with 
covariance 

$$S = C^{-1} = (P^{-1} + H^T R^{-1} H)^{-1}$$ 

and mean

$$
    \mu = C^{-1} d = \bar z - S H^T R^{-1} (H \bar z - y_\mathrm{obs}).
$$

We see that the mean of the posterior is influenced by the mean of the prior ($\bar z$) as well as the observation $y_\mathrm{obs}$ and the forward map $H$. The covariance is related both to the covariance of the prior as well as the observation. In fact, the update from the prior to the posterior takes into account the uncertainties in the prior and in the observation. If there is no uncertainty in the observation, then the mean of the posterior will be exactly the observation -  after all, we would then be absolutely certain that the observation is the truth. The update from prior to posterior in the linear Gaussian case is a key element in the well-known Kalman filter.
