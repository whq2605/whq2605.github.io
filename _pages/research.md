---
layout: default
title: Research
permalink: /research/
---

<div class="container">
<div class="page-header">
  <h1>Research</h1>
  <p>
    My research lies at the interface of statistical physics and biology, focused on understanding
    collective and emergent phenomena in living systems far from thermodynamic equilibrium.
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
    <!-- List your key collaborators here -->
    I collaborate with researchers across biophysics, soft matter, and mathematical biology.
    Key collaborators include Prof. Xinpeng Xu (GTIIT), Prof. Yariv Kafri (Technion),
    and Dr. Julien Tailleur (Paris Diderot).
  </p>
</div>

</div>
