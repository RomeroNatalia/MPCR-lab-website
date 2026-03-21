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

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-4@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% comment %} Leadership first in specific order {% endcomment %}
    {% for person in site.people %}{% if person.slug == "Elan-Barenholtz" %}{% include content-people-top.html %}{% endif %}{% endfor %}
    {% for person in site.people %}{% if person.slug == "Susan-Schneider" %}{% include content-people-top.html %}{% endif %}{% endfor %}
    {% for person in site.people %}{% if person.slug == "William-Hahn" %}{% include content-people-top.html %}{% endif %}{% endfor %}
    {% for person in site.people %}{% if person.slug == "Natalia-Romero" %}{% include content-people-top.html %}{% endif %}{% endfor %}

    {% comment %} Rest of active members alphabetically {% endcomment %}
    {% assign active_members = site.people | where: "active", true | sort: "title" %}
    {% for person in active_members %}
      {% unless person.slug == "Elan-Barenholtz" or person.slug == "Susan-Schneider" or person.slug == "William-Hahn" or person.slug == "Natalia-Romero" %}
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
