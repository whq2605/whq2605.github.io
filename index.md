---
layout: default
title: Home
---

<div class="container">
<div class="home-layout">

<!-- ── Sidebar ── -->
<aside class="profile-sidebar">
  <img src="{{ '/assets/img/profile.jpg' | relative_url }}" alt="Haiqin Wang" class="profile-photo">

  <div class="profile-name">Haiqin Wang</div>
  <div class="profile-position">
    Postdoc Research Scholar<br>
    Harvey Mudd College
  </div>

  <ul class="profile-contacts">
    <li>
      <span class="icon"><i class="fas fa-envelope"></i></span>
      <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>
    </li>
    {% if site.author.google_scholar %}
    <li>
      <span class="icon"><i class="fas fa-graduation-cap"></i></span>
      <a href="{{ site.author.google_scholar }}" target="_blank">Google Scholar</a>
    </li>
    {% endif %}
    {% if site.author.github %}
    <li>
      <span class="icon"><i class="fab fa-github"></i></span>
      <a href="https://github.com/{{ site.author.github }}" target="_blank">github.com/{{ site.author.github }}</a>
    </li>
    {% endif %}
    {% if site.author.orcid %}
    <li>
      <span class="icon"><i class="fab fa-orcid"></i></span>
      <a href="https://orcid.org/{{ site.author.orcid }}" target="_blank">ORCID</a>
    </li>
    {% endif %}
  </ul>

  <div class="social-row">
    {% if site.author.google_scholar %}
    <a class="social-btn" href="{{ site.author.google_scholar }}" target="_blank">
      <i class="fas fa-graduation-cap"></i> Scholar
    </a>
    {% endif %}
    {% if site.author.github %}
    <a class="social-btn" href="https://github.com/{{ site.author.github }}" target="_blank">
      <i class="fab fa-github"></i> GitHub
    </a>
    {% endif %}
    <a class="social-btn" href="{{ '/assets/pdf/CV.pdf' | relative_url }}">
      <i class="fas fa-file-pdf"></i> CV
    </a>
  </div>
</aside>

<!-- ── Main content ── -->
<div class="about-content">
  <h1>About Me</h1>

  <div class="about-text">
    <p>
      I am a Postdoc Research Scholar at <strong>Harvey Mudd College</strong>.
      My research focuses on theoretical biophysics and statistical physics, with emphasis on
      active matter, nonequilibrium dynamics, and their applications to biological systems.
    </p>
    <p>
      I received my Ph.D. in Physics from <strong>The University of Hong Kong</strong> (2016),
      where I studied run-and-tumble motion and differential dynamic microscopy under
      Prof. Huang Jian-Dong and Dr. Julien Tailleur.
      Before joining Harvey Mudd, I was an Associate Professor at Soochow University
      and held postdoctoral positions at Shanghai Jiao Tong University and Université Paris Diderot.
    </p>
    <p>
      <!-- Add a sentence about your current research focus at HMC -->
      Currently, I am working on [brief description of your current research project at HMC].
    </p>
  </div>

  <!-- Research Interests -->
  <div style="margin-bottom: 2.5rem;">
    <div class="section-title">Research Interests</div>
    <ul class="interests-list">
      <li class="interest-tag">Active Matter</li>
      <li class="interest-tag">Nonequilibrium Statistical Physics</li>
      <li class="interest-tag">Biological Physics</li>
      <li class="interest-tag">Pattern Formation</li>
      <li class="interest-tag">Tissue Mechanics</li>
      <li class="interest-tag">Systems Biology</li>
      <li class="interest-tag">Stochastic Dynamics</li>
    </ul>
  </div>

  <!-- News -->
  <div style="margin-bottom: 2.5rem;">
    <div class="section-title">News</div>
    <ul class="news-list">
      <li class="news-item">
        <span class="news-date">2025</span>
        <span class="news-text">Joined Harvey Mudd College as a Postdoc Research Scholar.</span>
      </li>
      <li class="news-item">
        <span class="news-date">2022</span>
        <span class="news-text">
          Preprint: "<a href="https://arxiv.org/abs/2210.11696" target="_blank">Spontaneous Bending of Hydra Tissue Fragments Driven by Supracellular Actomyosin Cables</a>" posted on arXiv.
        </span>
      </li>
      <li class="news-item">
        <span class="news-date">2022</span>
        <span class="news-text">Invited talk at the 12th National Conference on Soft Matter and Biological Physics.</span>
      </li>
      <li class="news-item">
        <span class="news-date">2021</span>
        <span class="news-text">Invited talk at Xiamen Soft Matter Forum 2021 &amp; ICAM-China 2021.</span>
      </li>
      <!-- Add more news items here -->
    </ul>
  </div>

  <!-- Featured Publications -->
  <div>
    <div class="section-title">Selected Publications</div>
    {% assign featured = site.data.publications | where: "featured", true %}
    {% for pub in featured limit: 3 %}
    <div class="featured-pub">
      <div class="pub-title">
        {% if pub.url %}<a href="{{ pub.url }}" target="_blank">{{ pub.title }}</a>{% else %}{{ pub.title }}{% endif %}
      </div>
      <div class="pub-authors">{{ pub.authors | replace: "**Haiqin Wang**", "<strong>Haiqin Wang</strong>" }}</div>
      <div class="pub-links" style="margin-top: 0.3rem;">
        {% if pub.arxiv %}<a class="pub-badge preprint" href="https://arxiv.org/abs/{{ pub.arxiv }}" target="_blank">arXiv</a>{% endif %}
        {% if pub.doi %}<a class="pub-badge" href="https://doi.org/{{ pub.doi }}" target="_blank">DOI</a>{% endif %}
        {% if pub.pdf %}<a class="pub-badge" href="{{ pub.pdf | relative_url }}" target="_blank">PDF</a>{% endif %}
      </div>
    </div>
    {% endfor %}
    <p style="margin-top: 1rem; font-size: 0.88rem;">
      <a href="{{ '/publications/' | relative_url }}">View all publications →</a>
    </p>
  </div>
</div>

</div><!-- .home-layout -->
</div><!-- .container -->
