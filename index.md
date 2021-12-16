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

<p style="color:red">Looking for the Winter 2022 site? <a style="color:red" href="https://dsc-courses.github.io/dsc10-2022-wi">Click here</a>.</p>

{{ site.staffersnobio }}

[Zoom Links and Office Hours Schedule](https://canvas.ucsd.edu/calendar?include_contexts=course_29590#view_name=month){: .btn .btn-blue } [Podcasts](https://podcast.ucsd.edu){: .btn .btn-green }

This schedule is subject to change.

{% for module in site.modules %}
{{ module }}
{% endfor %}
