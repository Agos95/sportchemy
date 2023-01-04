---
title: "{{ replace .Name "-" " " | title }}"
summary:
abstract:

# Match details
details:
  # (YYYY-MM-DD HH:mm:ss)
  date: {{ .Date }}
  address:
    name:
    street:
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
