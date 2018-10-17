---
layout: home
title: Browse by species
description: "An archive of species sorted by species."
comments: false
---

{% assign tags = site.data.species %}
{% assign lst = '' %}

{% for tag in tags %}

  {% assign lst = lst | append: tag.species | append: ' ' %}

{% endfor %}

{% assign unique_tags = lst | split: ' ' | uniq | sort %}

<article>
<h2 class="tag-heading">All species</h2>
<ul>
{% for tag in unique_tags %}{% unless forloop.last %}
  {% for sp in tags %}
  {% if sp.species contains tag %}
  <li class="entry-title"><a href="{{ site.url }}/{{ sp.url }}" title="{{ sp.species }}">{{ sp.species }}</a></li>
  {% endif %}
  {% endfor %}
{% endunless %}{% endfor %}
</ul>
</article>