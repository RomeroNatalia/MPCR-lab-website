---
layout: full
featured: true
tags: home
title: Home
redirect_from:
  - /index.php
images:
  - path: /uploads/news-pictures/2023-Spring-Sandbox-Grand-Opening.JPG
  - path: /uploads/news-pictures/astro-image-4.jpg
  - path: /uploads/news-pictures/Warwick_Pic_62.JPG
  - path: /uploads/news-pictures/2018-Aug-DD-Short-Course-2018-004.jpg
---

{% include section-slideshow-cropped.html %}


<div class="uk-container uk-margin-large uk-container uk-text-left">
  <article class="uk-article">
    <div class="content-primary">

{% capture my-include %}
* * *
<h2 class="section-title uk-text-center uk-margin">
  Meet the Leaders of the MPCR
</h2>

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

{% endcapture %}
{{ my-include | markdownify }}

    </div>
  </article>
</div>

{% include section-latest.html title="Latest News" limit="4" more="More News" %}
