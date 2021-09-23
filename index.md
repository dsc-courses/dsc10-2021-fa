---
layout: home
title: Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }} 📊
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

[Zoom Links and OH Schedule](https://canvas.ucsd.edu/calendar?include_contexts=course_29590#view_name=month){: .btn .btn-blue } [Podcasts](https://podcast.ucsd.edu){: .btn .btn-green }

This schedule is subject to change.

{% for module in site.modules %}
{{ module }}
{% endfor %}
