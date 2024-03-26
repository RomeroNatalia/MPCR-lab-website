---
title: Laboratories
layout: post
hidden: true
# sidebar: right
---
<!-- {% include image.html img="https://source.unsplash.com/qX9Ie7ieb1E/900x500" alt="Alt for image" %} -->

<div class="uk-container uk-margin-medium-bottom">
<div class="uk-child-width-1-2@s uk-child-width uk-grid-medium uk-flex-center uk-grid-divider" data-uk-grid>
    {% for lab in site.labs %}
      {% if lab.active %}
        {% include content-media-left-1-3.html %}
      {% endif %}
    {% endfor %}
  </div>
</div>
