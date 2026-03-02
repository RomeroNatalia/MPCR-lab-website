---
title: Poster Gallery
layout: page
permalink: /posters/
---

<div class="uk-container">

{% comment %} Collect unique events for filter buttons {% endcomment %}
{% assign events = "" %}
{% for poster in site.posters %}
  {% if poster.event and poster.event != "" %}
    {% unless events contains poster.event %}
      {% if events == "" %}
        {% assign events = poster.event %}
      {% else %}
        {% assign events = events | append: "|" | append: poster.event %}
      {% endif %}
    {% endunless %}
  {% endif %}
{% endfor %}
{% assign event_list = events | split: "|" %}

{% if event_list.size > 0 %}
<div class="uk-margin-medium-bottom uk-text-center" id="poster-filters">
  <button class="uk-button uk-button-primary uk-button-small uk-margin-small-right poster-filter-btn" data-filter="all">All</button>
  {% for evt in event_list %}
  <button class="uk-button uk-button-default uk-button-small uk-margin-small-right poster-filter-btn" data-filter="{{ evt }}">{{ evt }}</button>
  {% endfor %}
</div>
{% endif %}

<div class="uk-child-width-1-3@l uk-child-width-1-2@m uk-child-width-1-1@s uk-grid-match" data-uk-grid>
  {% for poster in site.posters %}
  <div class="poster-card" data-event="{{ poster.event }}">
    <a href="{{ poster.url }}" class="uk-link-reset">
      <div class="uk-card uk-card-default uk-card-hover">
        {% if poster.thumbnail_image or poster.poster_image %}
        <div class="uk-card-media-top">
          <img src="{{ poster.thumbnail_image | default: poster.poster_image }}" alt="{{ poster.title | escape }}" style="width:100%; height:200px; object-fit:cover;">
        </div>
        {% endif %}
        <div class="uk-card-body uk-padding-small">
          <h4 class="uk-card-title" style="font-size:1rem">{{ poster.title }}</h4>
          {% if poster.event %}<p class="uk-text-meta uk-margin-remove-top">{{ poster.event }}{% if poster.semester %} · {{ poster.semester }}{% endif %}</p>{% endif %}
          {% if poster.authors and poster.authors.size > 0 %}
          <p class="uk-text-small uk-text-muted">
            {% for author_slug in poster.authors %}
              {% for person in site.people %}
                {% if person.slug == author_slug or person.username == author_slug %}
                  {{ person.title | default: person.slug }}{% unless forloop.last %}, {% endunless %}
                {% endif %}
              {% endfor %}
            {% endfor %}
          </p>
          {% endif %}
        </div>
      </div>
    </a>
  </div>
  {% endfor %}
</div>

</div>

{% if event_list.size > 0 %}
<script>
(function() {
  var buttons = document.querySelectorAll('.poster-filter-btn');
  var cards = document.querySelectorAll('.poster-card');
  buttons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var filter = this.getAttribute('data-filter');
      buttons.forEach(function(b) {
        b.classList.remove('uk-button-primary');
        b.classList.add('uk-button-default');
      });
      this.classList.remove('uk-button-default');
      this.classList.add('uk-button-primary');
      cards.forEach(function(card) {
        if (filter === 'all' || card.getAttribute('data-event') === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
})();
</script>
{% endif %}
