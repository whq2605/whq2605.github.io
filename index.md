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
    Postdoctoral Researcher<br>
    Department of Chemistry<br>
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
      I am a postdoctoral researcher in the <strong>Department of Chemistry</strong> at
      <strong>Harvey Mudd College</strong>, working with Prof. Bilin Zhuang.
      My research uses theory and simulation to understand soft and biological matter —
      from polymer solutions and biopolymer gels to cell migration and active matter —
      through the lens of non-equilibrium statistical mechanics.
    </p>
    <p>
      I received my Ph.D. in Physics from the <strong>Technion – Israel Institute of Technology</strong>
      in 2024, advised by Prof. Xinpeng Xu and Prof. Yariv Kafri. I earned my M.Sc. from
      Beijing Normal University and my B.Sc. from Capital Normal University, and was a visiting
      student in mathematics at HKUST. Most recently, I was a research assistant at the
      Wenzhou Institute, working with Prof. Masao Doi and Prof. Shigeyuki Komura.
    </p>
    <p>
      At Harvey Mudd, I am developing hybrid particle–continuum simulation methods for aqueous
      polymer solutions and studying the flow-driven translocation of macromolecules across
      biological barriers, such as the kidney glomerular slit diaphragm.
    </p>
  </div>

  <!-- Research Interests -->
  <div style="margin-bottom: 2.5rem;">
    <div class="section-title">Research Interests</div>
    <ul class="interests-list">
      <li class="interest-tag">Polymer Solutions: Theory &amp; Simulation</li>
      <li class="interest-tag">Soft &amp; Biological Matter Physics</li>
      <li class="interest-tag">Non-equilibrium Statistical Mechanics</li>
      <li class="interest-tag">Variational &amp; Machine-Learning Methods</li>
      <li class="interest-tag">Cell Migration</li>
      <li class="interest-tag">Active Matter</li>
      <li class="interest-tag">Multiscale Simulation</li>
    </ul>
  </div>

  <!-- News -->
  <div style="margin-bottom: 2.5rem;">
    <div class="section-title">News</div>
    <ul class="news-list">
      <li class="news-item">
        <span class="news-date">2026</span>
        <span class="news-text">Co-teaching Chem 161: Classical and Statistical Thermodynamics at Harvey Mudd College (Spring 2026).</span>
      </li>
      <li class="news-item">
        <span class="news-date">2026</span>
        <span class="news-text">Presenting a poster at the Berkeley Statistical Mechanics Meeting, UC Berkeley.</span>
      </li>
      <li class="news-item">
        <span class="news-date">2025</span>
        <span class="news-text">
          New paper in <em>Biophysical Journal</em>:
          "Biphasic curvature-dependence of cell migration inside microcylinders."
        </span>
      </li>
      <li class="news-item">
        <span class="news-date">2025</span>
        <span class="news-text">Joined Harvey Mudd College as a postdoctoral researcher in the Department of Chemistry.</span>
      </li>
      <li class="news-item">
        <span class="news-date">2024</span>
        <span class="news-text">
          New paper in <em>Biophysical Journal</em>:
          "Elastic interactions compete with persistent cell motility to drive durotaxis."
        </span>
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
