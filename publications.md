---
title: Publications
layout: page
sidebar: none
permalink: /publications/
---

* * *

<div class="uk-container uk-margin-medium-bottom">

{% assign pubs_by_year = site.publications | group_by: "year" | sort: "name" | reverse %}

{% if pubs_by_year.size == 0 %}
<p class="uk-text-center uk-text-muted uk-margin-large-top">Publications coming soon.</p>
{% endif %}

{% for year_group in pubs_by_year %}
<h2 class="uk-heading-line uk-margin-medium-top"><span>{{ year_group.name }}</span></h2>

<ul class="uk-list uk-list-divider">
  {% for pub in year_group.items %}
  <li>
    <div class="uk-margin-small-bottom">
      <strong>{{ pub.title }}</strong>
    </div>
    {% if pub.authors and pub.authors.size > 0 %}
    <div class="uk-text-small uk-margin-small-bottom">
      {% for author in pub.authors %}
        {% assign found_person = false %}
        {% for person in site.people %}
          {% if pub.author_slugs contains person.slug or pub.author_slugs contains person.username %}
            {% for a_slug in pub.author_slugs %}
              {% if a_slug == person.slug or a_slug == person.username %}
                {% if author == person.title %}
                  <a href="{{ person.url }}">{{ author }}</a>{% unless forloop.last %}, {% endunless %}
                  {% assign found_person = true %}
                {% endif %}
              {% endif %}
            {% endfor %}
          {% endif %}
        {% endfor %}
        {% unless found_person %}{{ author }}{% unless forloop.last %}, {% endunless %}{% endunless %}
      {% endfor %}
    </div>
    {% endif %}
    <div class="uk-text-meta">
      {% if pub.venue %}<em>{{ pub.venue }}</em>{% endif %}
      {% if pub.year %} ({{ pub.year }}){% endif %}
    </div>
    {% if pub.doi or pub.url or pub.pdf_url %}
    <div class="uk-margin-small-top">
      {% if pub.doi %}<a href="https://doi.org/{{ pub.doi }}" class="uk-button uk-button-text uk-margin-small-right" target="_blank">DOI</a>{% endif %}
      {% if pub.url %}<a href="{{ pub.url }}" class="uk-button uk-button-text uk-margin-small-right" target="_blank">Link</a>{% endif %}
      {% if pub.pdf_url %}<a href="{{ pub.pdf_url }}" class="uk-button uk-button-text" target="_blank">PDF</a>{% endif %}
    </div>
    {% endif %}
    {% if pub.tags and pub.tags.size > 0 %}
    <div class="uk-margin-small-top">
      {% for tag in pub.tags %}<span class="uk-label uk-label-default uk-margin-small-right" style="font-size:0.75rem">{{ tag }}</span>{% endfor %}
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endfor %}

</div>
