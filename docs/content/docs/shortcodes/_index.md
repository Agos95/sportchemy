---
# Title, summary, and page position.
title: Shortcodes
summary: Sportchemy introduces some additional shortcodes in addition to the Wowchemy ones.
weight: 3
#icon: calendar
#icon_pack: fas

date: "2023-02-26"
type: book # Do not modify.

gallery_item:
- album: players
  image: kareem-abdul-jabbar.jpg
  caption: Kareem Abdul Jabbar
- album: players
  image: karl-malone.jpg
  caption: Karl Malone
- album: players
  image: kobe-bryant.jpg
  caption: Kobe Bryant
- album: players
  image: larry-bird.jpg
  caption: Larry Bird
- album: players
  image: magic-johnson.jpg
  caption: Magic Johnson
- album: players
  image: michael-jordan.jpg
  caption: Michael Jordan
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
- `delimiter`, default `","`  
  Cell delimiter.
- `header`: default `"true"`  
  If `"true"`, first row is interpreted as the header.
- `caption`, optional  
  Caption for the table.
- `striped`, default `"true"`  
  If true, add the class `table-striped`, to make alternate rows of different colors.
- `hover`, default `"true"`  
  If true, add the class `table-hover`, to enable a hover state on the current row.
- `responsive`, default `"true"`  
  If `"true"`, it defaults to `"md"`.  
  If a str must be one of [`"sm"`, `"md"`, `"lg"`, `"xl"`], otherwise it defaults to `"md"`.  
  If not false, add the class `table-responsive-$responsive`, to make the table horizontable scrollable under the specified breakpoint.
- `small`, default `"false"`  
  If `"true"`, add the class `table-sm`, to make the table more compact by cutting cell padding in half.
- `halign`, default `"left"`  
  Horizontal text alignment for the table. If passed, must be one of [`"left"`, `"center"`, `"right"`], otherwise it defaults to `"left"`.
- `id`, optional  
  Specific id for the table, useful for targetting the specifc table with CSS.

### Example

```go
{{</* sportchemy-table path="games.csv" header="true" */>}}
```

{{< sportchemy-table path="games.csv" header="true" >}}


## Sportchemy Gallery

Sportchemy defines a variant of the Wowchemy `gallery` shortcodes, called `sportchemy-gallery`, which displays the image caption even outside the fancybox.

Configuration is done in the same way as the [original shortcode](https://wowchemy.com/docs/content/writing-markdown-latex/#image-gallery).

All the galleries created with this shortcode inherit the `sportchemy-gallery` CSS class.

### Parameters

- `album`, default `"gallery"`  
  Album folder in `assets/media/albums/` to search the images in.
- `order`, default `"asc"`  
  One of [`"asc"`, `"desc"`]. Sorting order by image Name.
- `processing`, default `"resize"`  
  One of [`"resize"`, `"fit"`], otherwise it defaults to `"resize"`. Set the hugo image processign function, respectively [`.Resize`, `.Fit`].  
  See [Hugo documentation](https://gohugo.io/content-management/image-processing/) for the differences.
- `resize_options`, optional  
  Resize options passed to Hugo image processing function.
  Defaults to `"x500"` if processing is `"resize"`,
  or to `"500x500"` if processing is `"fit"`.
- `fig_style`, optional  
  Additional style parameters for each `<figure>` tag.
  For instance, you can specify a padding between pictures.
- `img_style`, default `"max-height:300px;"`  
  Additional style parameters for each `<img>` tag.
  To have a better results, the advice is to set max-height a bit lower than the resize option.
- `id`, optional  
  Specific id for the table, useful for targetting the specifc table with CSS.

### Example

In Front Matter:

```yaml
# ... other things in Front Matter ...

gallery_item:
- album: players
  image: kareem-abdul-jabbar.jpg
  caption: Kareem Abdul Jabbar
- album: players
  image: karl-malone.jpg
  caption: Karl Malone
- album: players
  image: kobe-bryant.jpg
  caption: Kobe Bryant
- album: players
  image: larry-bird.jpg
  caption: Larry Bird
- album: players
  image: magic-johnson.jpg
  caption: Magic Johnson
- album: players
  image: michael-jordan.jpg
```

Then:
```go
{{</* sportchemy-gallery album="players" processing="resize" resize_options="x300" fig_style="margin:5px 0px 5px 0px" */>}}
```

{{< sportchemy-gallery album="players" processing="resize" resize_options="x300" fig_style="margin:5px 0px 5px 0px" >}}