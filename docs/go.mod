module github.com/wowchemy/starter-hugo-academic

go 1.19

replace(
	github.com/Agos95/sportchemy/sportchemy => ../sportchemy
)

require (
	github.com/Agos95/sportchemy/sportchemy v0.0.0-20230224093537-57ffd305f42a // indirect
	github.com/wowchemy/wowchemy-hugo-themes/modules/wowchemy-plugin-netlify v1.0.0 // indirect
	github.com/wowchemy/wowchemy-hugo-themes/modules/wowchemy/v5 v5.7.1-0.20230213200301-f55ff594c0f6
)
