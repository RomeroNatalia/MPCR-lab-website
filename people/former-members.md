---
title: Former Members
layout: page
sidebar: none

redirect_from:
  - people/alumni
---
{% comment %}
<!-- {% include image.html img="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fworkday.fau.edu%2Fimages%2Fmarketing%2Fvisit%2Ffau-campus.jpg&f=1&nofb=1" alt="Alt for image" %} -->
{% endcomment %}

* * *

<div class="uk-container uk-margin-medium-bottom">
  <div class="uk-child-width-1-4@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% for person in site.people %}
        {% if person.active != true %}
          {% include content-people-top.html %}
        {% endif %}
    {% endfor %}
  </div>
</div>
