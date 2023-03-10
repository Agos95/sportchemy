---
# Title, summary, and page position.
title: Match
summary: A match is a new archetype which represents a single game.
weight: 1
#icon: basketball
#icon_pack: fas

date: "2023-02-18"
type: book # Do not modify.
---

{{< toc hide_on="xl" >}}


## Archetype

Sportchemy defines a new archetype named `match` which represents a single game.

Each game is defined in its own markdown file under the `content/match/` directory. To create a new `match`:
```
hugo new --kind match match/my-match-name.md
```

An example of a `match` file is:

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
  name: Chase Center # optional
  address: Chase Center, San Francisco, California # optional
  link: https://goo.gl/maps/Dwk6Ua7ek4msvCz99 # optional
  lat: # not yet used
  long: # not yet used

# Schedule page publish date (NOT match date).
publishDate:  2022-09-01

tags: []

# Is this a featured match? (true/false)
featured: false
---
```

## Parameters

- `title`: Title of the match
- `summary`: Present to be aligned with other Wowchemy archetypes, but not used
- `date`: Match date. It **must** be in the format `YYYY-MM-DD HH:mm:ss`, otherwise sorting in blocks does not work
- `home`, `away`: Dictionaries containing information about the home and away team; keys are:
  - `name`: Team name
  - `logo`: Logo image for the team. It can be both a remote image (as in the example above), or an image stored in `assets/media/`.  
    Since it is common to have multiple matches per single team, you can also define the mapping between team names and logos in the file `data/sportchemy/team_logo.yaml` (create it with the intermediate directories if necessary). An example of this file is:
    ```yaml
    Atlanta Hawks: https://content.sportslogos.net/logos/6/220/full/8190_atlanta_hawks-primary-2021.png
    Boston Celtics: https://content.sportslogos.net/logos/6/213/full/boston_celtics_logo_primary_19977628.png
    Charlotte Hornets: https://content.sportslogos.net/logos/6/5120/full/1926_charlotte__hornets_-primary-2015.png
    Chicago Bulls: https://content.sportslogos.net/logos/6/221/full/chicago_bulls_logo_primary_19672598.png
    Dallas Mavericks: https://content.sportslogos.net/logos/6/228/full/3463_dallas_mavericks-primary-2018.png
    Denver Nuggets: https://content.sportslogos.net/logos/6/229/full/8926_denver_nuggets-primary-2019.png
    Golden State Warriors: https://content.sportslogos.net/logos/6/235/full/3152_golden_state_warriors-primary-2020.png
    Houston Rockets: https://content.sportslogos.net/logos/6/230/full/6830_houston_rockets-primary-2020.png
    Indiana Pacers: https://content.sportslogos.net/logos/6/224/full/4812_indiana_pacers-primary-2018.png
    Los Angeles Lakers: https://content.sportslogos.net/logos/6/237/full/uig7aiht8jnpl1szbi57zzlsh.png
    Miami Heat: https://content.sportslogos.net/logos/6/214/full/burm5gh2wvjti3xhei5h16k8e.gif
    Milwaukee Bucks: NBA/milwaukee_bucks_logo_primary_20165763.png
    New Orleans Pelicans: NBA/2681_new_orleans_pelicans-primary-2014.png
    Orlando Magic: NBA/orlando_magic_logo_primary_20117178.png
    Philadelphia 76ers: NBA/7034_philadelphia_76ers-primary-2016.png
    Phoenix Suns: NBA/phoenix_suns_logo_primary_20143696.png
    San Antonio Spurs: NBA/2547_san_antonio_spurs-primary-2018.png
    Toronto Raptors: NBA/7024_toronto_raptors-primary-2021.png
    Utah Jazz: NBA/utah_jazz_logo_primary_2023_sportslogosnet-8513.png
    ```
    The logic to assign the logo is the following:
    1. Use `logo` parameter in the Front Matter, if present.
    2. Look in `data/sportchemy/team_logo.yaml`, searching for the team name.
    3. Use a fallback image. Default is {{< icon name="users" pack="fas" >}}, but you can change it by creating the image `assets/media/sportchemy/team-placeholder.png` with your own placeholder.
- `score`: Final score of the game. This is a dictionary with the keys:
  - `home`: Points for the Home team.
  - `away`: Points for the Away team.
- `season`, `league`, `tournament`, `matchDay`: Additional match information, useful when filtering games in blocks.
- `court`: Playing field information; it is a dicionary with the keys:
  - `name`: Name of the playground.
  - `address`: Address of the playground.
  - `link`: Link to attach to the field name (for example a Google Maps link).
  - `lat`, `long`: Latitude and Longitude of the playground (not used yet).
  
  In blocks, a url is associated to the field name; it is constructed using the following logic:
  1. Use `link` parameter.
  2. Use `https://maps.google.com?{address}`, sanitizing the address.
  3. Use `https://maps.google.com?{name}`, sanitizing the address.
  4. Fallback to `#` ("empty" link).
- `publishDate`: Schedule page publish date (not match date). Hugo does not publish files with a future `publishDate`.

{{% callout warning %}}
If you don't need to work with different timezones, I suggest to add your timezone to the `config/_defaul/config.yaml` file (choosing from [this list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)), such as:
```yaml
timeZone: Europe/Rome
```
In this way, both match and publish dates are set to the same timezones. Otherwise, you can experience strange behaviours.
{{% /callout %}}
- `tags`: Tags to associate with the match.
- `featured`: set to `true` for a featured match (can be useful for filtering in blocks).