---
layout: default
title: Publications
permalink: /publications/
---

<div class="container">
<div class="page-header">
  <h1>Publications</h1>
  <p>* equal contribution &nbsp;·&nbsp; # corresponding author</p>
</div>

<div class="publications-intro">
  {% if site.author.google_scholar %}
  <a class="btn btn-outline" href="{{ site.author.google_scholar }}" target="_blank">
    <i class="fas fa-graduation-cap"></i> Google Scholar
  </a>
  {% endif %}
  {% if site.author.orcid %}
  <a class="btn btn-outline" href="https://orcid.org/{{ site.author.orcid }}" target="_blank">
    <i class="fab fa-orcid"></i> ORCID
  </a>
  {% endif %}
  <a class="btn btn-outline" href="{{ '/assets/pdf/CV.pdf' | relative_url }}">
    <i class="fas fa-file-pdf"></i> Full CV
  </a>
</div>

{% assign pubs_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% for year_group in pubs_by_year %}
<div class="pub-year-group">
  <div class="year-label">{{ year_group.name }}</div>

  {% assign items = year_group.items %}
  {% for pub in items %}
  <div class="pub-item">
    <span class="pub-num">{{ forloop.index }}.</span>
    <div class="pub-content">
      <span class="pub-title">
        {% if pub.url %}<a href="{{ pub.url }}" target="_blank">{{ pub.title }}</a>{% else %}{{ pub.title }}{% endif %}
      </span>
      <div class="pub-authors">
        {{ pub.authors | replace: "**Haiqin Wang**", "<strong>Haiqin Wang</strong>" }}
      </div>
      <div class="pub-venue">
        <em>{{ pub.journal }}</em>{% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}{% if pub.year %} ({{ pub.year }}){% endif %}
      </div>
      <div class="pub-links">
        {% if pub.pdf %}
        <a class="pub-badge" href="{{ pub.pdf | relative_url }}" target="_blank">
          <i class="fas fa-file-pdf"></i> PDF
        </a>
        {% endif %}
        {% if pub.arxiv %}
        <a class="pub-badge preprint" href="https://arxiv.org/abs/{{ pub.arxiv }}" target="_blank">
          arXiv:{{ pub.arxiv }}
        </a>
        {% endif %}
        {% if pub.doi %}
        <a class="pub-badge" href="https://doi.org/{{ pub.doi }}" target="_blank">
          DOI
        </a>
        {% endif %}
        {% if pub.code %}
        <a class="pub-badge code" href="{{ pub.code }}" target="_blank">
          <i class="fas fa-code"></i> Code
        </a>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>
{% endfor %}

<div style="margin-top: 3rem; padding: 1.25rem; background: var(--card-bg); border-radius: var(--radius); font-size: 0.85rem; color: var(--muted);">
  <i class="fas fa-sync-alt"></i>
  This list is automatically updated from Google Scholar on a weekly schedule via GitHub Actions.
  Last updated: <em id="update-date">see git history</em>
</div>

</div>
