---
title: "{{ replace .Name "-" " " | title }}"
summary:

# match date (YYYY-MM-DD HH:mm:ss)
date: {{ .Date }}

# Match details
details:
  season:
  league:
  match_day:
  court:
    name:
    address:
    gmap:
    lat:
    long:

# Teams info
home:
  name:
  logo:

away:
  name:
  logo:

# Final Score
score:
  home:
  away:

# Schedule page publish date (NOT match date).
publishDate: {{ .Date }}

tags: []

# Is this a featured match? (true/false)
featured: false
---
