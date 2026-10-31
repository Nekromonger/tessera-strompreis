# Changelog

## 0.3.0 - 2026-10-31
- The tile's graph shows hours: 48 bars for today and tomorrow instead of up to 100. The card a tap opens still shows
  every quarter of an hour. The tile takes 13 KB of the screen's layout memory instead of 16 KB.
- The stepped line without its fill makes no bars at all, so it is the lightest graph on the screen.
- A tap anywhere on the tile opens the card. A bar's price is chosen on the card, where the bars are wide enough.

## 0.2.0 - 2026-10-28
- Option "Graph starts at": a 24-hour graph from any hour to the same hour the next day (such as 13:00 to 13:00),
  with empty bars where the list has no prices yet.

## 0.1.0 - 2026-10-28
- First version: a tile for the EPEX Spot price sensor, with the graph of today and tomorrow, the card and the top bar
  item of the Electricity price plugin 0.11.0.
