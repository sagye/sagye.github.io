---
layout: default
title: Research
permalink: /research.html
---
# Research
A chronological list of all my publications can be found [here]({{ '/publications.html' | relative_url }}).

My background is in applied mathematics with a focus on computational mathematics for complex physical problems. My research interests include geometric methods for fluid dynamics and other physical systems, stochastic modelling, and data assimilation. Broadly, I aim to develop and explore computational methods that leverage geometry, stochasticity, and data to improve accuracy and efficiency for predicting and understanding complex physical phenomena.

My main research deals with computational methods in the following fields:
 - stochastic (turbulence) closure modelling;
 - geometric integration;
 - geometric numerical hydrodynamics.

[Stochastic Closure Modelling](#stochastic-modelling) [Geometric Integration](#geometric-integration) [Geometric Numerical Hydrodynamics](#geometric-numerical-hydrodynamics)
{: .pub-nav}

---

#### Stochastic (turbulence) closure modelling {#stochastic-modelling}  
Numerical simulations of turbulent systems and complex low-order "toy models" are frequently limited to coarse-grid resolutions due to computational constraints. This creates a need for closure modelling to account for the impact of unresolved small-scale dynamics on the resolved scales of motion. Without such models, the truncation of high-frequency interactions leads to physical inaccuracies, visible in, e.g., qualitatively different solution behaviour or the failure to reach correct statistical equilibria. A stochastic approach to closure is particularly effective because it represents these unresolved interactions in a probabilistic manner, reflecting the inherent information loss caused by coarsening and multiscale uncertainty of the underlying physics. 


#### Geometric integration {#geometric-integration}
Numerical simulations of dynamical systems profit from integration schemes that respect the underlying mathematical structure of the governing equations. Standard numerical methods often introduce non-physical artifacts, such as artificial dissipation or energy drift, which can compromise the long-term reliability of a simulation. Geometric integration provides a robust alternative by designing algorithms that preserve intrinsic invariants, such as energy, momentum, and Casimirs, or geometric properties like symplecticity and the Lie-Poisson structure. This approach is particularly effective because it maintains the physical consistency of the discrete system, ensuring that the numerical solution remains on the correct manifold and accurately reflects the long-term evolution of complex physical phenomena.

#### Geometric numerical hydrodynamics {#geometric-numerical-hydrodynamics}
Geometric numerical hydrodynamics treats fluid motion through the lens of differential geometry, viewing the evolution of a fluid as a geodesic flow on the group of diffeomorphisms. By deriving equations of motion from variational principles, this framework ensures that the resulting models inherently reflect the underlying symmetries and conservation laws. 
This theoretical rigor enables the use of precise numerics as a tool to study hydrodynamical systems and their properties, which has been particularly fruitful for geophysical flows on the sphere. By maintaining the Lie-Poisson structure and integral invariants such as vorticity and Casimirs, these methods provide a physically consistent laboratory for investigating the long-term stability, energy spectra, and topological characteristics of hydrodynamical models.



  
  



