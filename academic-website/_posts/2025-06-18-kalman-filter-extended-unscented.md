---
layout: default
title: "The Kalman filter: standard, extended, unscented"
---
# The Kalman filter: standard, extended, unscented


Now we'll have a look at some extensions to the Kalman filter.
Specifically, we will introduce the extended Kalman filter (EKF) and the
unscented Kalman filter (UKF). Let's first recap the standard Kalman
filter.

## The Kalman filter 

### Model formulation 

Recall the discrete-time linear dynamics subject to Gaussian noise,
$$z^{n+1} = Fz^n + B + \Xi^n.$$ Here $F$ and $B$ describe how the state
$z$ transitions from one time instance to the next, and $\Xi^n$ is
(multivariate) Gaussian process noise with mean zero and covariance
matrix $Q$.

The forward (observation) model is also assumed to be linear and subject
to noise: $$y^n = Hz^n + \Sigma^n,$$ where $H$ is an appropriately sized
matrix and $\Sigma$ and is a (multivariate) Gaussian process with mean
zero and covariance matrix $R$.

### Forecast and analysis  

Simulating the dynamics of this system and incorporating measurements
consists of two steps: i) predict (or *forecast*), and ii) update (or
*analysis*).

1.  The prediction step takes place whenever no new observations are
    available. For the linear case with Gaussian noise, we the mean
    state and the covariance evolved as follows: 
    
    $$\begin{aligned}
            \text{Mean state:} \quad & \bar z^{n+1} = F\bar{z}^n + B, \\
            \text{Covariance:} \quad & P^{n+1} = F P^n F^T + Q.    
    \end{aligned}$$

2.  The update step takes place when new observations become available.
    Let's say this happens after computing $\bar z^n$ and $P^n$. Then,
    $(\bar z^n, P^n)$ will be our forecast pair, and we'll denote these
    by $(\bar z^f, P^f)$ for now. An observation $y_\mathrm{obs}$ of the
    true signal then allows us to transform the forecast pair into an
    analysis pair $(\bar z^a, P^a)$ by applying the Kalman filter:
    
    $$\begin{aligned}
            \text{Innovation:} \quad & x = y_\mathrm{obs} - H \bar z^f, \\
            \text{Innovation covariance:} \quad & S = H P^f H^T + R, \\
    \text{Kalman gain:} \quad & K = P^f H^T S^{-1}, \\
    \text{Updated state:} \quad & \bar z^a = \bar z^f + Kx, \\
    \text{Updated covariance:} \quad & P^a = (I - K H) P^f.
    \end{aligned}$$

It's good to keep in mind that $P^f$ and $P^a$ (in the update step) are
defined at the same point in time. The analysis pair can then be used to
predict the state and covariance at the next time instance.

That's all there is for the Kalman filter: it's a clean, *optimal*
algorithm for linear models subject to additive Gaussian noise. But what
if the evolution of the true state is nonlinear? The extended Kalman
filter (EKF) can then be used instead.

## The extended Kalman filter 

Many real-world problems are described by nonlinear equations. In such
cases, the assumptions underlying the standard Kalman filter no longer
apply. Different methods should then be used to accurately incorporate
observations into predictions. The extended Kalman filter (EKF) is a
popular method that does just that.

### Model formulation 

Our discrete-time dynamics is now no longer assumed to be linear.
Instead, we write 

$$\begin{split}
        z^{n+1} = f(z^n) + \Xi^n, \\
        y^n = h(z^n) + \Sigma^n,
    \end{split}$$ 
    
where $f$ and $h$ are differentiable functions. The
properties of $\Xi$ and $\Sigma$ are the same as before.

### Forecast and analysis

Predicting the state at time level $n+1$ is straightforward: simply
compute $f(z^n)$. Predicting the covariance $P^{n+1}$ is more difficult,
and we have to linearize the dynamics $f$ instead to approximate the
covariance at the new time level. This is achieved via linearization,
using the Jacobian as an approximation of the true dynamics.

The forecast and analysis steps in the EKF are as follows.

1.  The prediction relies on the nonlinear dynamics for the state
    estimate and linearized dynamics for the covariance. Note that the
    linearized state transition is evaluated at $z^n$. 
    
    $$\begin{aligned}
            \text{State:} \quad & z^f = f(z^n), \\
            \text{Linearized state transition:} \quad & F = \frac{\partial f}{\partial z}\Big|_{z^n}\\
            \text{Covariance:} \quad & P^f = F P^n F^T + Q.
    \end{aligned}$$

2.  The update is similar to that of the Kalman filter, but again relies
    on linearized dynamics on certain places. The linearized observation
    is evaluated at $z^f$ 
    
    $$\begin{aligned}
            \text{Innovation:} \quad & x = y_\mathrm{obs} - h(z^f), \\
            \text{Linearized observation:}\quad  & H = \frac{\partial h}{\partial x}\Big|_{z_f}\\
            \text{Innovation covariance:} \quad & S = H P^f H^T + R, \\
        \text{Kalman gain:} \quad & K = P^f H^T S^{-1}, \\
        \text{Updated state:} \quad &  z^a =  z^f + Kx, \\
        \text{Updated covariance:} \quad & P^a = (I - K H) P^f.
    \end{aligned}$$

The Kalman gain is now no longer optimal, owing to the approximate
evolution of the covariance. As a result of the linearization, errors in
the state estimate might grow if above a certain threshold - possibly
leading to divergent predictions.

## The unscented Kalman filter

A different tactic is used to tackle the nonlinear dynamics in the
unscented Kalman filter (UKF). The discrete-time model that we considere
here is the same nonlinear model as used in the EKF. The difference now
is that the covariance will no longer be propagated by linearized
dynamics - and hence computing Jacobians is avoided. Rather, so-called
*sigma points* are sampled that represent the underlying Gaussian
distribution. These points evolve according to the nonlinear dynamics
and produce a predicted mean and covariance, and are also used in the
analysis. We provide a brief overview below, see [[1]](#1) for
more details.

### Sigma points

Our state variable $z$ is considered an $N_z$-dimensional random
variable, for which we can define a mean $\bar z$ and covariance $P$.
Then we define $N$ *sigma points* $s_1, \ldots, s_N$
$\in\mathbb{R}^{N_z}$, which can be any vector, along with specific
weights.

The first-order weights $W_1^m, \ldots, W_N^m$ must satisfy

- $\sum_{j=1}^N W_j^m = 1$;

- $\sum_{j=1}^N W_j^m s_j = \bar z$.

The second-order weights $W_1^c, \ldots, W_N^c$ must satisfy

- $\sum_{j=1}^N W_j^c = 1$;

- an element-wise quadratic constraint, for all pairs
  $(i,l)\in \{1, \ldots N_z\}$:
  $\sum_{j=1}^N W_j^c (s_j)_i(s_j)_l = \mathbb{E}[z_i z_j]$.

The idea is the following. If we have a random variable $z$ with mean
$\bar z$ and covariance $P$, then what are the mean and covariance of
the random variable $y=h(z)$. Specifically, if $h$ is nonlinear, we want
efficient and unbiased methods to compute these statistics of $y$. The
sigma points form a set of appropriately chosen weighted points that
parametrize the means and covariances of the distributions up to third
order for any nonlinear transformation.

There are several popular choices for sigma points, which are not shown
here. These generally require knowing the mean $\bar z$ and the
covariance $P$ at the current point in time.

### Forecast and analysis 

Having chosen the sigma points $s^n_j$, $j=1,\ldots, N,$ based on the
mean $\bar z^n$ and covariance $P^n$, these points can be propagated in
time to compute the forecast pair $(\bar z^f, P^f)$.

1.  The sigma points are propagated,

    $$s_j^f = f(s_j^n), \quad j=1,\ldots,N,$$ 
    
    after which the forecast pair is computed via 
    
    $$\begin{aligned}
            \text{State:} \quad &\bar z^f = \sum_j W_j^m s_j^f, \\
            \text{Covariance:} \quad &  P^f = \sum_j W_j^c(s_j^f - \bar z^f)(s_j^f - \bar z^f)^T + Q.        
            \end{aligned} $$ 

Thus, we see that the sigma points provide an empirical estimate of the mean and the covariance via weighted sums.

2.  The sigma points also play a role in the observation, so we compute

    $$y_j = h(s_j), \quad j=1,\ldots, N,$$ 
    
    and subsequently compute the corresponding mean and covariance, 
    
    $$\begin{aligned}
            \bar y &= \sum_j W_j^m y_j, \\
            S &= \sum_j W_j^c(y_j-\bar y)(y_j-\bar y)^T + R.
    \end{aligned}$$ 
    
    The cross-covariance matrix $C_{zs}$ between the
    prediction $z$ and the observation $y$ is also required,
    
    $$C_{zy} = \sum_{j}W_j^c(s_j^f - \bar z^f)(y_j - \bar y)^T,$$ 
    
    This leads to the Kalman gain and the update of the state and covariance
    
    $$\begin{aligned}
            \text{Kalman gain:} \quad & K = C_{zy}S^{-1}, \\
            \text{Updated state:} \quad & \bar z^a = \bar z^f + K(y_\mathrm{obs} - \bar y)\\
            \text{Updated covariance:} \quad & P^a = P^f - KSK^T.\\
    \end{aligned}$$
    
#### References
<a id="1">[1]</a> 
Julier, S. J., & Uhlmann, J. K. (1997, July). New extension of the Kalman filter to nonlinear systems. In Signal processing, sensor fusion, and target recognition VI (Vol. 3068, pp. 182-193). Spie.