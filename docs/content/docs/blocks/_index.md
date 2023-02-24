---
# Title, summary, and page position.
title: Sportchemy Collection Block
summary:
weight: 2
icon: calendar
icon_pack: fas

date: "2023-02-24"
type: book # Do not modify.
---

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
        # additional parameters specific to each view
      # Choose single or dual column layout
      columns: '1'
```

## Parameters

`sportchemy-collection` supports the [general parameters](https://wowchemy.com/docs/getting-started/page-builder/#personalizing-blocks) of every Wowchemy block, plus some additional one specific for `match`.

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

Sportchemy defines two views for its collection block.

{{% callout warning %}}
As for now, the `design/view_params` parameter is not yet implemented, but in the future it will allow to customize some aspects of the views.
{{%/ callout %}}

### Card View

The `sportchemy-card-view` layout displays games using Bootstrap cards:

{{< figure src="card-view.png" >}}

Cards are arranged in 3, 2 or 1 columns, depending on the screen size.

### Table View

The `sportchemy-table-view` layout displays games using a Table:

{{< figure src="table-view.png" >}}