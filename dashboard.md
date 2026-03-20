---
title: Lab Dashboard
layout: page
sidebar: none
permalink: /dashboard/
---

{% comment %}
  ── Compute stats ──────────────────────────────────────────────────────
{% endcomment %}

{% assign active_members = site.people | where: "active", true %}
{% assign alumni_members = site.people | where: "alumni", true %}
{% assign active_projects = site.projects | where: "active", true %}
{% assign pub_count = site.publications.size %}
{% assign poster_count = site.posters.size %}
{% assign faculty_members = site.people | where: "faculty", true %}

* * *

<!-- ── Stat Cards ──────────────────────────────────────────────────── -->

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-3@m uk-child-width-1-2@s uk-grid-small uk-grid-match" data-uk-grid>

  <div>
    <div class="uk-card uk-card-primary uk-card-body uk-text-center" style="border-radius:8px">
      <h1 class="uk-heading-large uk-margin-remove" style="color:#fff">{{ active_members.size }}</h1>
      <p class="uk-margin-remove uk-text-small" style="color:rgba(255,255,255,.85)">Active Members</p>
    </div>
  </div>

  <div>
    <div class="uk-card uk-card-secondary uk-card-body uk-text-center" style="border-radius:8px">
      <h1 class="uk-heading-large uk-margin-remove" style="color:#fff">{{ alumni_members.size }}</h1>
      <p class="uk-margin-remove uk-text-small" style="color:rgba(255,255,255,.85)">Alumni</p>
    </div>
  </div>

  <div>
    <div class="uk-card uk-card-default uk-card-body uk-text-center" style="border-radius:8px; border-left:4px solid #0b3d69">
      <h1 class="uk-heading-large uk-margin-remove" style="color:#0b3d69">{{ active_projects.size }}</h1>
      <p class="uk-margin-remove uk-text-small uk-text-muted">Active Projects</p>
    </div>
  </div>

  <div>
    <div class="uk-card uk-card-default uk-card-body uk-text-center" style="border-radius:8px; border-left:4px solid #0b3d69">
      <h1 class="uk-heading-large uk-margin-remove" style="color:#0b3d69">{{ pub_count }}</h1>
      <p class="uk-margin-remove uk-text-small uk-text-muted">Publications</p>
    </div>
  </div>

  <div>
    <div class="uk-card uk-card-default uk-card-body uk-text-center" style="border-radius:8px; border-left:4px solid #0b3d69">
      <h1 class="uk-heading-large uk-margin-remove" style="color:#0b3d69">{{ poster_count }}</h1>
      <p class="uk-margin-remove uk-text-small uk-text-muted">Posters</p>
    </div>
  </div>

  <div>
    <div class="uk-card uk-card-default uk-card-body uk-text-center" style="border-radius:8px; border-left:4px solid #0b3d69">
      <h1 class="uk-heading-large uk-margin-remove" style="color:#0b3d69">{{ faculty_members.size }}</h1>
      <p class="uk-margin-remove uk-text-small uk-text-muted">Faculty</p>
    </div>
  </div>

</div>
</div>

<!-- ── Latest News ─────────────────────────────────────────────────── -->

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-card uk-card-default uk-card-body" style="border-radius:8px">
  <h3 class="uk-card-title"><span data-uk-icon="icon: bolt; ratio: 1.2"></span> Latest News</h3>
  <ul class="uk-list uk-list-divider">
    {% assign recent_posts = site.posts | slice: 0, 5 %}
    {% for post in recent_posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="uk-text-meta uk-margin-small-left">{{ post.date | date: "%B %-d, %Y" }}</span>
    </li>
    {% endfor %}
    {% if site.posts.size == 0 %}
    <li class="uk-text-muted">No news posts yet.</li>
    {% endif %}
  </ul>
  {% if site.posts.size > 5 %}
  <a href="/news/" class="uk-button uk-button-text uk-margin-small-top">View all news &rarr;</a>
  {% endif %}
</div>
</div>

<!-- ── Active Projects with Member Counts ──────────────────────────── -->

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-card uk-card-default uk-card-body" style="border-radius:8px">
  <h3 class="uk-card-title"><span data-uk-icon="icon: grid; ratio: 1.2"></span> Active Projects</h3>

  {% if active_projects.size == 0 %}
  <p class="uk-text-muted">No active projects.</p>
  {% else %}
  <div class="uk-overflow-auto">
  <table class="uk-table uk-table-hover uk-table-divider uk-table-small">
    <thead>
      <tr>
        <th>Project</th>
        <th class="uk-text-center" style="width:120px">Members</th>
        <th class="uk-text-center" style="width:100px">Tags</th>
      </tr>
    </thead>
    <tbody>
      {% for project in active_projects %}
      <tr>
        <td><a href="{{ project.url | relative_url }}">{{ project.title }}</a></td>
        <td class="uk-text-center">
          {% if project.members %}{{ project.members.size }}{% else %}0{% endif %}
        </td>
        <td class="uk-text-center">
          {% if project.tags %}{{ project.tags.size }}{% else %}0{% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
  </div>
  {% endif %}
</div>
</div>

<!-- ── Research Areas / Tag Cloud ───────────────────────────────────── -->

{% comment %}
  Collect all tags from active projects into a pipe-delimited string,
  then split and count occurrences for sizing.
{% endcomment %}

{% assign all_tags_str = "" %}
{% for project in active_projects %}
  {% if project.tags %}
    {% for tag in project.tags %}
      {% if all_tags_str == "" %}
        {% assign all_tags_str = tag %}
      {% else %}
        {% assign all_tags_str = all_tags_str | append: "|" | append: tag %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign all_tags_arr = all_tags_str | split: "|" %}

{% comment %} De-duplicate tags {% endcomment %}
{% assign unique_tags_str = "" %}
{% for tag in all_tags_arr %}
  {% assign tag_trimmed = tag | strip %}
  {% if tag_trimmed != "" %}
    {% unless unique_tags_str contains tag_trimmed %}
      {% if unique_tags_str == "" %}
        {% assign unique_tags_str = tag_trimmed %}
      {% else %}
        {% assign unique_tags_str = unique_tags_str | append: "|" | append: tag_trimmed %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% assign unique_tags = unique_tags_str | split: "|" %}

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-card uk-card-default uk-card-body" style="border-radius:8px">
  <h3 class="uk-card-title"><span data-uk-icon="icon: tag; ratio: 1.2"></span> Research Areas</h3>

  {% if unique_tags.size == 0 %}
  <p class="uk-text-muted">No research tags defined yet.</p>
  {% else %}
  <div class="uk-flex uk-flex-wrap uk-flex-center" style="gap:8px">
    {% for tag in unique_tags %}
      {% comment %} Count occurrences of this tag {% endcomment %}
      {% assign tag_count = 0 %}
      {% for t in all_tags_arr %}
        {% assign t_trimmed = t | strip %}
        {% if t_trimmed == tag %}
          {% assign tag_count = tag_count | plus: 1 %}
        {% endif %}
      {% endfor %}

      {% comment %} Size based on count: 1=small, 2=medium, 3+=large {% endcomment %}
      {% if tag_count >= 3 %}
        {% assign tag_size = "1.25rem" %}
        {% assign tag_weight = "bold" %}
      {% elsif tag_count == 2 %}
        {% assign tag_size = "1rem" %}
        {% assign tag_weight = "600" %}
      {% else %}
        {% assign tag_size = "0.85rem" %}
        {% assign tag_weight = "normal" %}
      {% endif %}

      <span class="uk-label" style="font-size:{{ tag_size }}; font-weight:{{ tag_weight }}; background:#0b3d69; padding:6px 14px; border-radius:20px">{{ tag }}</span>
    {% endfor %}
  </div>
  {% endif %}
</div>
</div>

<!-- ── People by Role ──────────────────────────────────────────────── -->

<div class="uk-container uk-margin-large-bottom">
<div class="uk-card uk-card-default uk-card-body" style="border-radius:8px">
  <h3 class="uk-card-title"><span data-uk-icon="icon: users; ratio: 1.2"></span> People at a Glance</h3>
  <div class="uk-child-width-1-3@m uk-child-width-1-1@s uk-grid-small" data-uk-grid>

    <div>
      <h4 class="uk-text-bold">Faculty</h4>
      <ul class="uk-list uk-list-bullet">
        {% for person in faculty_members %}
        <li><a href="{{ person.url | relative_url }}">{{ person.title }}</a></li>
        {% endfor %}
        {% if faculty_members.size == 0 %}
        <li class="uk-text-muted">None listed.</li>
        {% endif %}
      </ul>
    </div>

    <div>
      <h4 class="uk-text-bold">Active Members</h4>
      <ul class="uk-list uk-list-bullet">
        {% for person in active_members %}
          {% unless person.faculty or person.director or person.contact %}
          <li><a href="{{ person.url | relative_url }}">{{ person.title }}</a></li>
          {% endunless %}
        {% endfor %}
        {% if active_members.size == 0 %}
        <li class="uk-text-muted">None listed.</li>
        {% endif %}
      </ul>
    </div>

    <div>
      <h4 class="uk-text-bold">Recent Alumni</h4>
      <ul class="uk-list uk-list-bullet">
        {% assign recent_alumni = alumni_members | slice: 0, 10 %}
        {% for person in recent_alumni %}
        <li><a href="{{ person.url | relative_url }}">{{ person.title }}</a></li>
        {% endfor %}
        {% if alumni_members.size == 0 %}
        <li class="uk-text-muted">None listed.</li>
        {% endif %}
      </ul>
      {% if alumni_members.size > 10 %}
      <a href="/people/former-members/" class="uk-button uk-button-text">View all alumni &rarr;</a>
      {% endif %}
    </div>

  </div>
</div>
</div>
