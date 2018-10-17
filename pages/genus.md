---
layout: home
title: Browse by Genus
description: "An archive of species sorted by Genus."
comments: false
---

{% assign tags = site.data.species %}
{% assign lst = '' %}

{% for tag in tags %}

  {% assign lst = lst | append: tag.genus | append: ' ' %}

{% endfor %}

{% assign unique_tags = lst | split: ' ' | uniq | sort %}

{% for tag in unique_tags %}{% unless forloop.last %}
  <span class="anchor-bookmark" id="{{ tag }}"></span>
  <article>
  <h2 class="tag-heading">{{ tag }}</h2>
  <ul>
  {% for sp in tags %}
  {% if sp.genus contains tag %}
  <li class="entry-title"><a href="{{ site.url }}/{{ sp.url }}" title="{{ sp.species }}">{{ sp.species }}</a></li>
  {% endif %}
  {% endfor %}
  </ul>
  </article>
{% endunless %}{% endfor %}