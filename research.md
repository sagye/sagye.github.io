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

### Stochastic (turbulence) closure modelling {#stochastic-modelling}  
Numerical simulations of turbulent systems and complex low-order "toy models" are frequently limited to coarse-grid resolutions due to computational constraints. This creates a need for closure modelling to account for the impact of unresolved small-scale dynamics on the resolved scales of motion. Without such models, the truncation of high-frequency interactions leads to physical inaccuracies, visible in, e.g., qualitatively different solution behaviour or the failure to reach correct statistical equilibria. A stochastic approach to closure is particularly effective because it represents these unresolved interactions in a probabilistic manner, reflecting the inherent information loss caused by coarsening and multiscale uncertainty of the underlying physics. 

**Contributions:**
 - General framework for assimilating statistics into statistically stationary turbulent flow
([J. Comp. Phys. 2025](https://doi.org/10.1016/j.jcp.2025.114234){:target="_blank"})
 - Structure-preserving stochastic modelling based on geometric mechanics
([J. Adv. Model. Earth Syst. 2023](https://doi.org/10.1029/2022MS003268){:target="_blank"},
[ArXiv 2026](https://arxiv.org/abs/2606.24275){:target="_blank"})
 - Continuous data assimilation ('nudging') of energy spectra to observed values
([Phys. Fluids 2023](https://doi.org/10.1063/5.0156942){:target="_blank"},
[J. Fluid Mech. 2023](https://doi.org/10.1017/jfm.2023.816){:target="_blank"},
[Phys. Rev. Fluids 2025](https://doi.org/10.1103/PhysRevFluids.10.013801){:target="_blank"})
 - Trajectory learning for ensemble forecasts via the continuous ranked probability score (CRPS) ([ArXiv 2025](https://arxiv.org/abs/2508.21664){:target="_blank"})
 - Dependence of spatial basis functions for reduced-order models on chosen numerics
([Multiscale Model. Simul. 2022](https://doi.org/10.1137/21M1452871){:target="_blank"})


---


### Geometric integration {#geometric-integration}
Numerical simulations of dynamical systems profit from integration schemes that respect the underlying mathematical structure of the governing equations. Standard numerical methods often introduce non-physical artifacts, such as artificial dissipation or energy drift, which can compromise the long-term reliability of a simulation. Geometric integration provides a robust alternative by designing algorithms that preserve intrinsic invariants, such as energy, momentum, and Casimirs, or geometric properties like symplecticity and the Lie-Poisson structure. This approach is particularly effective because it maintains the physical consistency of the discrete system, ensuring that the numerical solution remains on the correct manifold and accurately reflects the long-term evolution of complex physical phenomena.

**Contributions:**
 - Stochastic Lie-Poisson integration 
([Adv. Contin. Discrete Models 2024](https://doi.org/10.1186/s13662-023-03796-y){:target="_blank"},
[ArXiv 2024](https://arxiv.org/abs/2408.16701){:target="_blank"})
 - A symplectic integrator for stochastic spin systems
([Phys. Rev. E 2025](https://doi.org/10.1103/PhysRevE.111.054201){:target="_blank"})


---


### Geometric numerical hydrodynamics {#geometric-numerical-hydrodynamics}
Geometric numerical hydrodynamics treats fluid motion through the lens of differential geometry, viewing the evolution of a fluid as a geodesic flow on the group of diffeomorphisms. By deriving equations of motion from variational principles, this framework ensures that the resulting models inherently reflect the underlying symmetries and conservation laws. 
This theoretical rigor enables the use of precise numerics as a tool to study hydrodynamical systems and their properties, which has been particularly fruitful for geophysical flows on the sphere. By maintaining the Lie-Poisson structure and integral invariants such as vorticity and Casimirs, these methods provide a physically consistent laboratory for investigating the long-term stability, energy spectra, and topological characteristics of hydrodynamical models.

**Contributions:**
 - Derivation and numerical simulation of scaling laws for averaged turbulence on the sphere
([Physica D 2025](https://doi.org/10.1016/j.physd.2025.134808){:target="_blank"})
 - Numerical study of the dissipative properties of transport noise on the sphere 
([J. Comput. Dyn. 2025](http://dx.doi.org/10.3934/jcd.2025008){:target="_blank"})
 - Casimir-preserving method for global quasi-geostrophic flow
([J. Comp. Phys. 2025](https://doi.org/10.1016/j.jcp.2025.114155){:target="_blank"},
[ArXiv 2025](https://arxiv.org/abs/2409.05432){:target="_blank"},
[J. Comput. Dyn. 2026](https://doi.org/10.3934/jcd.2026005){:target="_blank"})
 - Derivation and geometric method for (thermal) quasi-geostrophic flow
([ArXiv 2024](https://arxiv.org/abs/2402.13707){:target="_blank"},
[Phys. Fluids 2025](https://doi.org/10.1063/5.0281814){:target="_blank"})
 - Study of minimum-enstrophy equilibria for quasi-geostrophic flow over topography
([ArXiv 2026](https://arxiv.org/abs/2604.25600){:target="_blank"})


  
  
[↑ Back to top](#){: .back-to-top}


