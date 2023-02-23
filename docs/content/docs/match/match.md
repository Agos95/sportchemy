---
# Title, summary, and page position.
title: Match archetype
summary: New match archetype for your team games.
weight: 2

date: "2023-02-18"
type: book # Do not modify.
---

Each game is defined in its own markdown file under the `content/match` directory.

An example of a `match` file is the following:

```yaml
---
title: Los Angeles Lakers vs Golden State Warriors
summary: # just for compatibility, not yet used

# match date (YYYY-MM-DD HH:mm:ss)
# format must be 'YYYY-MM-DD HH:mm:ss', otherwise ordering and sorting in blocks don't work
date: 2022-10-18 22:00:00

# Teams info
home:
  name: Los Angeles Lakers
  logo: https://content.sportslogos.net/logos/6/237/full/uig7aiht8jnpl1szbi57zzlsh.png

away:
  name: Golden State Warriors
  logo: https://content.sportslogos.net/logos/6/235/full/3152_golden_state_warriors-primary-2020.png

# Final Score
score:
  home: 109
  away: 123

# Match details
season: 2022-23
league: NBA
tournament: Regular Season
matchDay:
court:
  name: Chase Center
  address: Chase Center, San Francisco, California
  link: # optional
  lat: # optional
  long: # optional

# Schedule page publish date (NOT match date).
publishDate:  2022-09-01

tags: []

# Is this a featured match? (true/false)
featured: false
---
```