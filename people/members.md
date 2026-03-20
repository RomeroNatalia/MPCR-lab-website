---
title: People
layout: page
sidebar: none
redirect_from:
  - https://mpcrlab.com/people/members
---

* * *

<h2 class="section-title uk-text-center uk-margin">Lab Leadership</h2>

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-3@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% if site.data.people %}
      {% for person in site.data.people %}
        {% if person.director %}
          {% include content-people-top-data.html %}
        {% endif %}
      {% endfor %}
    {% else %}
      {% for person in site.people %}
        {% if person.director %}
          {% include content-people-top.html %}
        {% endif %}
      {% endfor %}
    {% endif %}
  </div>
</div>

* * *

<h2 class="section-title uk-text-center uk-margin">Active Members</h2>

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-4@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% if site.data.people %}
      {% for person in site.data.people %}
        {% if person.active and person.director != true %}
          {% include content-people-top-data.html %}
        {% endif %}
      {% endfor %}
    {% else %}
      {% for person in site.people %}
        {% if person.active and person.director != true %}
          {% include content-people-top.html %}
        {% endif %}
      {% endfor %}
    {% endif %}
  </div>
</div>
