---
title: Projects
layout: page
sidebar: none
---

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-3@m uk-child-width-1-2@s uk-grid-medium" data-uk-grid>
  {% assign active_projects = site.projects | where: "active", true %}
  {% for project in active_projects %}
  <div>
    <div class="uk-card uk-card-default uk-card-hover">
      {% if project.image %}
      <div class="uk-card-media-top">
        <a href="{{ project.url | relative_url }}">
          <img src="{{ project.image }}" alt="{{ project.title }}" style="height:180px;width:100%;object-fit:cover;">
        </a>
      </div>
      {% endif %}
      <div class="uk-card-body">
        <h3 class="card-title-xsmall article-title-font">
          <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
        </h3>
        {% if project.description %}
        <p class="content-secondary uk-margin-small-bottom">{{ project.description | truncate: 120 }}</p>
        {% endif %}
        {% if project.members.size > 0 %}
        <div class="card-meta">{{ project.members.size }} member{% if project.members.size != 1 %}s{% endif %}</div>
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}
</div>
</div>
