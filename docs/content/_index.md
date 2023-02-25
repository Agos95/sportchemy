---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: markdown
    content:
      title: Sportchemy
      subtitle: Sports addon for Wowchemy
      text: |-
        [Wowchemy](https://wowchemy.com/) is an amazing website builder for the [Hugo](https://gohugo.io/) Static Site Generator. **Sportchemy** is an extension for Wowchemy, and it aims to provide functionalities to create a website for a Sport team or club. The inspiration behind this project is given by the [SportsPress](https://wordpress.org/plugins/sportspress/) plugin for WordPress.

        {{< cta cta_text="Learn more in the **Docs**!" cta_link="docs" cta_new_tab="false" cta_alt_text="See the code on **GitHub**!" cta_alt_link="https://github.com/Agos95/sportchemy" cta_alt_new_tab="true" >}}

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
      offset: 2
      # Field to sort by, such as Date or Title
      sort_by: 'Date'
      sort_ascending: true
      archive:
        enable: false
    design:
      # Choose a listing view
      view: sportchemy-card-view
      # Choose single or dual column layout
      columns: '1'

  - block: sportchemy-collection
    id:
    content:
      title: Match Table
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
      offset: 2
      # Field to sort by, such as Date or Title
      sort_by: 'Date'
      sort_ascending: true
      archive:
        enable: false
    design:
      # Choose a listing view
      view: sportchemy-table-view
      # Choose single or dual column layout
      columns: '1'
---
