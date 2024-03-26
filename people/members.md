---
title: Active Members
layout: page
sidebar: none
redirect_from:
  - https://mpcrlab.com/people/members
---
<!-- {% include image.html img="https://source.unsplash.com/qX9Ie7ieb1E/900x500" alt="Alt for image" %} -->

* * *

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-4@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% for person in site.people %}
      {% if person.active %}
        {% include content-people-top.html %}
      {% endif %}
    {% endfor %}
  </div>
</div>
