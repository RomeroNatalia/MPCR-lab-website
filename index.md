---
layout: full
featured: true
tags: home
title: Home
redirect_from:
  - /index.php
images:
  - path: /uploads/news-pictures/2018-Aug-DD-Short-Course-2018-004.jpg
  - path: /uploads/news-pictures/Warwick_Pic_62.JPG
  - path: /uploads/news-pictures/astro-image-4.jpg
  - path: /uploads/news-pictures/2023-Spring-Sandbox-Grand-Opening.JPG
---

<!-- {% include section-slideshow.html %} -->

{% include section-slideshow-cropped.html %}

<!-- {% include section-picture.html title="Picture" image="/uploads/news-pictures/2015-Mon-DD-Homepage-1.jpg" url="/uploads/news-pictures/2015-Mon-DD-Homepage-1.jpg" blank="true" %} -->


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
    {% for person in site.people %}
        {% if person.director %}
          {% include content-people-top.html %}
        {% endif %}
    {% endfor %}
  </div>
</div>

{% endcapture %}
{{ my-include | markdownify }}

    </div>
  </article>
</div>

{% comment %}
<!-- {% include section-featured.html title="Featured" %} -->
<!-- {% include section-spotlight.html title="Spotlight" %} -->
<!-- {% include calendar.html title= "Events" %} -->
{% endcomment %}


{% comment %}
<!-- Commenting Out News Letter Sign Up Until We Have One -->
  {% include section-mailchimp.html title="Newsletter Signup"
      text="Sign up for our mailing list to stay up to date with what is happening in the MPCR."
      button_text="Sign Up"
  %}
{% endcomment %}

{% include section-latest.html title="Latest News" limit="4" more="More News" %}

{% comment %}
  <!-- {% include section-cta.html title="Join / Contact Us?" %} -->
  {% include section-cta.html title="Interested in joining the MPCR?" text="We are looking for talented scientists at the undergraduate, masters and doctoral levels. If you have have similar research interests and skills in relevant disciplines, then please get in touch." button_text="Contact Us" button_url="/contact/" blank="true" %}
{% endcomment %}

{% comment %}
<!-- {% include section-author.html author="Author-ID" title="Title" %} -->
{% endcomment %}
