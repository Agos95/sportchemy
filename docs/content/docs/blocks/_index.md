---
# Title, summary, and page position.
title: Collection Block
summary: Sportchemy defines a new Collection block designed specifically for the match archetype. It also provides two different views to display the games.
weight: 2
#icon: calendar
#icon_pack: fas

date: "2023-02-24"
type: book # Do not modify.
---

{{< toc hide_on="xl" >}}

## Usage

Sportchemy defines a new block called `sportchemy-collection`. This block is inspired by the [Wowchemy Page Collection](https://wowchemy.com/blocks/collection/), but it adds some additional parameters specific for the `match` archetype.

```yaml
---
title: My page
type: landing

sections:
  - block: sportchemy-collection
    id:
    content:
      title:
      subtitle:
      text:
      text_below:
      # Choose how many matches you would like to display (0 = all pages)
      count: 6
      # Filter on criteria
      filters:
        # The folders to display content from
        team:
          -
        season:
          -
        league:
          -
        tournament:
          -
        category:
        tag:
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        # you can also filter using a date range from "from" to "to"
        from:
        to:
      # Choose how many pages you would like to offset by
      # Useful if you wish to show the first item in the Featured widget
      offset: 0
      # Field to sort by, such as Date
      sort_by: 'Date'
      sort_ascending: false
      archive:
        enable: true
    design:
      # Choose a listing view from:
      # sportchemy-card-view, sportchemy-table-view
      view: sportchemy-card-view
      view_params:
        # common parameters
        date_format:
        time_format:
        # additional parameters are specific to each view
        # ...
      # Choose single or dual column layout
      columns: '1'
```

## Parameters

`sportchemy-collection` supports the [general parameters](https://wowchemy.com/docs/getting-started/page-builder/#personalizing-blocks) of every Wowchemy block, with the possibility to also add a text below the matches using the `text_below` key. In addition, it defines some additional parameters specific for `match`.

### Filters

Additional parameters are added to filter games:
- `team`: List of teams to display (both home and away games). If empty, all teams are included.
- `season`: List of seasons to include in the block. If empty, all seasons are included.
- `league`: List of leagues to include in the block. If empty, all leagues are included.
- `category`, `tags`: List of categories and tags to include, to be aligned with Wowchemy collection.
- `featured_only`: set to `true` to include only featured games.
- `exclude_featured`: set to `true` to display only non-featured games
- `exclude_future`: set to `true` to display only past games
- `exclude_past`: set to `true` to display only future games
- `from`: set to a date to only show matches from that date
- `to`: set to a date to only show matches until that date

## Views

Sportchemy defines two views for its Collection block.  
Some customizations can be specified using the `degign/view_params` parameter. See the description of each view to see which 
options are available.

### Card View

The `sportchemy-card-view` layout displays games using Bootstrap cards:

{{< figure src="card-view.png" >}}

Cards are arranged in 3, 2 or 1 columns, depending on the screen size.

#### Card View Parameters

- *`date_format` : default `Mon, 2 Jan 2006`*
- *`time_format` : default `15:05`*  
  Date and time are defined using [Hugo constants](https://wowchemy.com/docs/getting-started/customization/#datetime-options).

### Table View

The `sportchemy-table-view` layout displays games using a Table:

{{< figure src="table-view.png" >}}

#### Table View Parameters

- *`date_format` : default `Mon, 2 Jan 2006`*
- *`time_format` : default `15:05`*  
  Date and time are defined using [Hugo constants](https://wowchemy.com/docs/getting-started/customization/#datetime-options).
- *`show_league` : default `false`*  
  If `true`, add a column which shows the league of each match. Can be useful in case of multiple leagues in the same table.

### View Hooks

Differently from Wowchemy, Sportchemy views are called inside a hook function:
- [`sportchemy-card-view-hook`](https://github.com/Agos95/sportchemy/blob/main/sportchemy/layouts/partials/views/sportchemy-card-view-hook.html) creates a `<div class="row justify-content-center">`, where ther columns containing the cards are inserted.
- [`sportchemy-table-view-hook`](https://github.com/Agos95/sportchemy/blob/main/sportchemy/layouts/partials/views/sportchemy-table-view-hook.html) defines the header row of the Table; then each `match` is rendered as a row.