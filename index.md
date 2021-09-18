---
layout: home
title: Home
nav_exclude: false
nav_order: 1
seo:
  type: Course
  name: Just the Class
---

# {{ site.tagline }} 📊
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

<!-- {: .mb-3 }
**Lecture:** MWF 10-11AM (A00), 11AM-12PM (B00), 9-10AM (C00)
{: .mb-0 .fs-5 .text-grey-dk-000 } -->

**This website is in progress and all content is subject to change.**

[Recordings, Zoom Links, and OH Schedule on Canvas](https://canvas.ucsd.edu/calendar?include_contexts=course_29590#view_name=month){: .btn .btn-blue }

{% for module in site.modules %}
{{ module }}
{% endfor %}
