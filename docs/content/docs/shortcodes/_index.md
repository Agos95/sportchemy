---
# Title, summary, and page position.
title: Shortcodes
summary: Sportchemy introduces some additional shortcodes in addition to the Wowchemy ones.
weight: 3
#icon: calendar
#icon_pack: fas

date: "2023-02-26"
type: book # Do not modify.
---

## Sportchemy Table

Sportchemy defines a variant of the Wowchemy `table` shortcode, called `sportchemy-table`. It allows a deeper configuration, introducing the possibility of:
- striped tables (`table-striped`)
- hoverable rows (`table-hover`)
- responsive table (`table-responsive-XX`)
- small tables (`table-sm`)
- defining the horizontal text alignment in the cells.
In addition, the header row is encapsuled inside the `<thead>` tag, allowing a easier target for CSS.

All the tables create with this shortcode inherit the `sportchemy-table` CSS class.

### Parameters

- `path`: 
  Path or url to the csv table.  
  Path is relative to the folder where the shortcode is called.
- `delimiter`, default ","  
  Cell delimiter.
- `header`: default "true"  
  If "true", first row is interpreted as the header.
- `caption`, optional  
  Caption for the table.
- `striped`, default "true"  
  If true, add the class `table-striped`, to make alternate rows of different colors.
- `hover`, default "true"  
  If true, add the class `table-hover`, to enable a hover state on the current row.
- `responsive`, default "true"  
  If "true", it defaults to "md".  
  If a str must be one of ["sm", "md", "lg", "xl"], otherwise it defaults to "md".  
  If not false, add the class `table-responsive-$responsive`, to make the table horizontable scrollable under the specified breakpoint.
- `small`, default "false"  
  If "true", add the class `table-sm`, to make the table more compact by cutting cell padding in half.
- `halign`, default "left"  
  Horizontal text alignment for the table. If passed, must be one of ["left", "center", "right"], otherwise it defaults to "left".
- `id`, optional  
  Specific id for the table, useful for targetting the specifc table with CSS.

### Example

```go
{{</* sportchemy-table path="games.csv" header="true" */>}}
```

{{< sportchemy-table path="games.csv" header="true" >}}