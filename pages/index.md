---
title: Necessary Conditions of Learning
permalink: /
---
# Reflections on Necessary Conditions of Learning

The material presented here contains my reflections on Ference Marton's 
*Necessary Conditions of Learning*. I developed the material to use as a 
starting point for a "flipped-colloquium" on learning theory.


## Contents

{% for module in site.data.navigation.modules %}
  - [{{ module[1].title }}]({{ module[1].path | relative_url }}) {% if module[1].p  ath == "/" %}(this page){% endif %}
{% endfor %}


