---
title: Contact Us
layout: page
permalink: /contact/
sidebar: none
redirect_from:
  - /contact.php
---
* * *
<div class="uk-container uk-margin-medium-bottom">
  <div class="uk-child-width-1-3@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% for person in site.people %}
        {% if person.contact %}
          {% include content-people-top.html %}
        {% endif %}
    {% endfor %}
  </div>
</div>

{% comment %}
  Exclude this section for now.
  {% include formspree.html email="my_name@gmail.com" redirect="/thanks/" %}
{% endcomment %}
