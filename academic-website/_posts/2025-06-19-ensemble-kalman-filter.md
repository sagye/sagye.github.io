---
layout: default
title: "The ensemble Kalman filter"
---
# The ensemble Kalman filter


The standard Kalman filter yields an algorithm that transforms a
Gaussian forecast pair $(\bar z^f, P^f)$ to an analysis pair
$(\bar z^a, P^a)$, under the assumption of a linear model subject to
Gaussian noise. A general approach to transform empirical forecast PDFs
to analysis PDFs is particle filtering. The downside to this is that
computational costs can grow quickly when many particles are used to
approximate the empirical PDFs. The ensemble Kalman filter (EnKF) sits
somewhere in the middle, and has become a popular tool for state
estimation in high-dimensional physics problems. Its suitability for
high-dimensional nonlinear problems stems from the fact that the
covariance matrix is not propagated, but is instead computed empirically
from an ensemble. 

For full details, see, e.g.,
[[1]](#1), [[2]](#2).

We outline the EnKF below.

### Model formulation

We consider a discrete-time system with nonlinear dynamics,

$$\begin{split}
        z^{n+1} &= f(z^n) + \Xi^n, \\
        y^n &= h(z^n) + \Sigma^n. 
    \end{split}$$ 
    
Here, $z^n$ denotes the system state at time instance
$n$, $y^n$ denotes the corresponding measurement, and $\Xi^n$ and
$\Sigma^n$ are independent zero-mean multivariate Gaussian processes
with covariance matrices $Q$ and $R$, respectively.

### Forecast and analysis

Rather than relying on an exact covariance matrix, as in the traditional
Kalman filter, or sigma points, as in the unscented Kalman filter, the
Ensemble Kalman Filter (EnKF) employs a Monte Carlo method to estimate
forecast and analysis statistics. This is achieved by considering an
ensemble approach in both the forecast and the analysis.

We assume that, at some time instance, we have obtained a forecast
ensemble of size $q$:

$$Z^{f} = \left(z^{f}_{1}, z^{f}_{2}, \ldots, z^{f}_{q}\right)$$ 

where $z^{f}_{i}$ is the $i^\mathrm{th}$ ensemble member.

The true state and covariance are not known, hence we approximate the
statistics based on the available ensemble data. We do so as

$$\begin{split}
\bar{z}^{f} &= \frac{1}{q} \sum_{i=1}^{q} z^{f}_{i}, \\
P^{f} & = \frac{1}{q-1} \sum_{i=1}^{q} \left(z^{f}_{i} - \bar{z}^{f} \right) \left(z^{f}_{i} - \bar{z}^{f} \right)^{T}.
\end{split}$$ 

The underlying assumption is that the forecast ensemble
mean is the best forecast estimate of the state and that the ensemble
spread describes the error between the best forecast and the actual
state.

The analysis step is also formulated in terms of ensembles. The
observation ensemble must have mean equal to $y_{\text{obs}}$ and
covariance equal to $R$,

$$y_{\mathrm{obs}, i} = y_{\text{obs}} + \epsilon_{i}, \quad \epsilon_{i} \sim \mathcal{N}(0, R)$$

The actual analysis then acts on each ensemble member as

$$z^{a}_{i} = z^{f}_{i} + K \left(y_{\text{obs}, i} - h(z^{f}_{i}) \right),$$

where $K$ is the classical Kalman gain determined by the approximations
of the covariances as 

$$K = P^{f}_{zy} \left(P^{f}_{yy}\right)^{-1}.$$

Here, the covariance approximations are given by 

$$\begin{split}
P^{f}_{zy} &= \frac{1}{q-1} \sum_{i=1}^{q} \left(z^{f}_{i} - \bar{z}^{f} \right) \left(y^{f}_{i} - \bar{y}^{f} \right)^{T}, \\ 
P^{f}_{yy} &= \frac{1}{q-1} \sum_{i=1}^{q} \left(y^{f}_{i} - \bar{y}^{f} \right) \left(y^{f}_{i} - \bar{y}^{f} \right)^{T},
\end{split}$$ 

where $y_i^f = h(z_i^f)$.


#### References
<a id="1">[1]</a> 
Evensen, G. (2003). The ensemble Kalman filter: Theoretical formulation and practical implementation. Ocean dynamics, 53, 343-367.

<a id="2">[2]</a> 
Gillijns, S., Mendoza, O. B., Chandrasekar, J., De Moor, B. L. R., Bernstein, D. S., & Ridley, A. (2006, June). What is the ensemble Kalman filter and how well does it work?. In 2006 American control conference (pp. 6-pp). IEEE.

