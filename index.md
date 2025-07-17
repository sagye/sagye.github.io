---
layout: default
title: Home
---

<div class="bio-container">

<div class="bio-text">


Welcome to my webpage!  

<p>I'm a postdoctoral researcher in applied mathematics.  
My research interests include geometric methods for fluid dynamics and other physical systems, stochastic modeling, and data assimilation. Broadly, I aim to develop and explore computational methods that leverage geometry, stochasticity, and data to improve accuracy and efficiency for predicting and understanding complex physical phenomena. </p>


<p>Currently, I'm based at Chalmers University of Technology (Sweden) in the group of Klas Modin, working on geometric numerical hydrodynamics. Prior to this, I completed my PhD at the University of Twente (The Netherlands) on stochastic computational models for geophysical fluid dynamics, under the supervision of Bernard Geurts.  </p>


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