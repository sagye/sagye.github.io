---
layout: default
title: Home
---

<div class="bio-container">

<div class="bio-text">


Welcome to my webpage!  

<p>I'm a postdoctoral researcher in applied mathematics working with Darryl Holm at Imperial College London.


My research interests include geometric methods for fluid dynamics and other physical systems, stochastic modelling, and data assimilation. Broadly, I aim to develop and explore computational methods that leverage geometry, stochasticity, and data to improve accuracy and efficiency for predicting and understanding complex physical phenomena. </p>


Research interests

 - Stochastic computational methods for fluid dynamics and magnetohydrodynamics
 - Geometric (stochastic) integration
 - Geometric numerical hydrodynamics
 - Stochastic (turbulence) closure modelling
 - Data assimilation



Currently, I'm a research associate at Imperial College London working together with Prof. Darryl D. Holm. I'm a guest researcher at the Technical University of Munich (TUM) in the group of Prof. Christian Kühn.

Previously, I was a postdoctoral researcher based at Chalmers University of Technology (Sweden) in the group of Prof. Klas Modin, working on geometric numerical hydrodynamics. Prior to this, I completed my PhD at the University of Twente (The Netherlands) on stochastic computational models for geophysical fluid dynamics, under the supervision of Prof. Bernard Geurts.  


</div>


<div>
  <img src="assets/placeholder.jpg" alt="Sagy" class="bio-image" />
</div>

</div>

### Recent News

<ul>
  {% assign sorted_news = site.data.news | sort: 'date' | reverse %}
  {% for item in sorted_news limit:3 %}
    <li><strong>{{ item.date | date: "%b %d, %Y" }}</strong> — {{ item.text }}</li>
  {% endfor %}
</ul>