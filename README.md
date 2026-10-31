# Strompreis EPEX

The electricity price now as a tile, with the graph of today and tomorrow on bigger tiles and on a card of its own.
It reads the price sensor of the **EPEX Spot** integration (HACS `epex_spot`), for example
`sensor.epex_spot_data_total_price`, whose attribute `data` holds yesterday, today and (from the afternoon) tomorrow.

Built on [Electricity price](https://github.com/Heronimonimo/tessera-electricity-price) by Heronimonimo (MIT), with a
tile for EPEX Spot instead of Nord Pool, ENTSO-e and GE-Spot. The graph, the card, the tariff formula and the top bar
item work as there.

## Set up

1. Have the **EPEX Spot** integration (HACS `epex_spot`) set up in Home Assistant.
2. In Tessera, open **Plugins**, choose **Add with a link**, paste `https://github.com/Nekromonger/tessera-strompreis`,
   tick your screens and let each build once.
3. In Layout, place the **Electricity price (EPEX Spot)** tile from the library's Plugins group. A tile smaller than
   2x2 shows the price with the meter bar; from 2x2 up it adds the graph.
4. In the inspector, choose `sensor.epex_spot_data_total_price` (the list holds only sensors with a `data` attribute).
5. Choose the unit (ct/kWh by default) and the decimals. Tap the graph to see a bar's price and time slot (tap it again to
   let go); tap the row with the name and price over it to open the card with every quarter of an hour and the lowest
   and highest price still to come.

## Good to know

- Past bars are grey, the bar of now is the accent colour, and the bars to come are green, amber or red by their place
  between the lowest and highest price.
- Tomorrow's bars appear on their own once the sensor has them (in the afternoon).
- The total price sensor already holds surcharges and VAT, so the delivery formula can stay empty.

## 24 Stunden ab einer Uhrzeit (0.2.0)

The option **Graph starts at** (Diagramm ab Uhrzeit) shows exactly 24 hours from that hour, such as 13:00 to 13:00 the
next day, without a second day. Before 13:00 that is yesterday 13:00 to today 13:00, so the sensor's list must hold
yesterday's afternoon (the Tibber package `tibber_preise_tessera.yaml` keeps it). Slots the list does not hold yet stay
empty. 0 keeps today and tomorrow from midnight.
