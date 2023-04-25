---
outputs:
- html
- Calendar

title: "{{ replace .Name "-" " " | title }}"
subtitle:
summary:

publishDate: {{ .Date }}

# Choose how many matches you would like to display (0 = all pages)
count: 6
# Filter on criteria
filters:
  # The folders to display content from
  team:
    # -
  season:
    # -
  league:
    # -
  tournament:
    # -
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
# Field to sort by, such as Date or details.match_day
sort_by: 'Date'
sort_ascending: false

view: sportchemy-table-view
---