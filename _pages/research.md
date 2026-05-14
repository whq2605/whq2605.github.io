---
layout: default
title: Research
permalink: /research/
---

<div class="container">
<div class="page-header">
  <h1>Research</h1>
  <p>
    My research applies theory and simulation to soft and biological matter — polymer solutions,
    biopolymer gels, cell migration, and active matter — grounded in non-equilibrium
    statistical mechanics and variational principles.
  </p>
</div>

<!-- Project cards -->
<div class="projects-grid">
  {% for project in site.data.projects %}
  <div class="project-card">
    <div class="project-img">{{ project.icon }}</div>
    <div class="project-body">
      <div class="project-title">{{ project.title }}</div>
      <div class="project-desc">{{ project.description }}</div>
      <div class="project-tags">
        {% for tag in project.tags %}
        <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
      {% if project.papers and project.papers.size > 0 %}
      <div class="project-papers">
        <div class="project-papers-label">Related papers:</div>
        {% for paper in project.papers %}
        <a href="{{ paper.url | default: '#' }}" {% if paper.url %}target="_blank"{% endif %}>
          {{ paper.title }}
        </a>
        {% endfor %}
      </div>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

<!-- Collaborators / Broader context section -->
<div style="padding: 2rem 0; border-top: 1px solid var(--border);">
  <div class="section-title">Collaborators</div>
  <p style="color: var(--muted); font-size: 0.92rem;">
    I am fortunate to work with collaborators across soft matter, biophysics, and applied
    mathematics, including Prof. Bilin Zhuang (Harvey Mudd College), Prof. Xinpeng Xu and
    Prof. Yariv Kafri (Technion), Prof. Tiezheng Qian and Prof. Penger Tong (HKUST),
    Prof. Masao Doi and Prof. Shigeyuki Komura (Wenzhou Institute), Prof. Dadong Yan
    (Beijing Normal University), and Prof. Kinjal Dasbiswas and Prof. Arvind Gopinath (UC Merced).
  </p>
</div>

</div>
