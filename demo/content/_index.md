---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: sportchemy-collection
    id:
    content:
      title: Match Cards
      subtitle:
      text:
      page_type: match
      # Choose how many pages you would like to display (0 = all pages)
      count: 6
      # Filter on criteria
      filters:
        # The folders to display content from
        category: ""
        tag: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        season:
          # - 2022-23
        league:
          # - promozione
        team:
          # - Pallacanestro Arcella
        from:
        to:
        
      # Choose how many pages you would like to offset by
      # Useful if you wish to show the first item in the Featured widget
      offset: 0
      # Field to sort by, such as Date or Title
      sort_by: 'Date'
      sort_ascending: true
    design:
      # Choose a listing view
      view: sportchemy-card
      # Choose single or dual column layout
      columns: '1'
---
