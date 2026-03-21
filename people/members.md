---
title: People
layout: page
sidebar: none
redirect_from:
  - https://mpcrlab.com/people/members
  - people/alumni
  - people/former-members
---

* * *

<h2 class="section-title uk-text-center uk-margin">Lab Leadership</h2>

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-3@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% assign directors = site.people | where: "director", true | sort: "title" %}
    {% for person in directors %}
      {% include content-people-top.html %}
    {% endfor %}
  </div>
</div>

* * *

<h2 class="section-title uk-text-center uk-margin">Active Members</h2>

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-4@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% assign active_non_directors = site.people | where: "active", true | sort: "title" %}
    {% for person in active_non_directors %}
      {% unless person.director %}
        {% include content-people-top.html %}
      {% endunless %}
    {% endfor %}
  </div>
</div>

* * *

<h2 class="section-title uk-text-center uk-margin no_toc" id="alumni">Lab Alumni</h2>

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-4@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% assign alumni = site.people | sort: "title" %}
    {% for person in alumni %}
      {% unless person.active %}
        {% include content-people-top.html %}
      {% endunless %}
    {% endfor %}
  </div>
</div>
