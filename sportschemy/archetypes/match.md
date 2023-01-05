---
title: "{{ replace .Name "-" " " | title }}"
summary:
abstract:

# (YYYY-MM-DD HH:mm:ss)
date: {{ .Date }}

# Match details
court:
  name:
  address:
  url:
league:

# Teams info
home:
  team:
  img:
  score:

away:
  team:
  img:
  score:

# Schedule page publish date (NOT event date).
publishDate: {{ .Date }}

tags: []

# Is this a featured match? (true/false)
featured: false
---
