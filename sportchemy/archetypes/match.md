---
title: "{{ replace .Name "-" " " | title }}"
summary:

# match date (YYYY-MM-DD HH:mm:ss)
date: {{ .Date }}

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

# Match details
season:
league:
matchDay:
court:
  name:
  address:
  link:
  lat:
  long:

# Schedule page publish date (NOT match date).
publishDate: {{ .Date }}

tags: []

# Is this a featured match? (true/false)
featured: false
---
