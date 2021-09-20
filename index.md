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

**This website is in progress and all content is subject to change.**

[Recordings, Zoom Links, and OH Schedule on Canvas](https://canvas.ucsd.edu/calendar?include_contexts=course_29590#view_name=month){: .btn .btn-blue }

{% for module in site.modules %}
{{ module }}
{% endfor %}
