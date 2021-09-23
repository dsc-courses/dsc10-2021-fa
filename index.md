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

[Recordings, Zoom Links, and OH Schedule on Canvas](https://canvas.ucsd.edu/calendar?include_contexts=course_29590#view_name=month){: .btn .btn-blue }

This schedule is subject to change.

{% for module in site.modules %}
{{ module }}
{% endfor %}
