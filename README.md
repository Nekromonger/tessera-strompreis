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
5. Choose the unit (ct/kWh by default) and the decimals. Tap a bar to see its price and time slot; tap beside the bars
   to open the card with the lowest and highest price still to come.

## Good to know

- Past bars are grey, the bar of now is the accent colour, and the bars to come are green, amber or red by their place
  between the lowest and highest price.
- Tomorrow's bars appear on their own once the sensor has them (in the afternoon).
- The total price sensor already holds surcharges and VAT, so the delivery formula can stay empty.

## 24 hours from an hour of your choice (0.2.0)

The option **Graph starts at** shows exactly 24 hours from that hour, such as 13:00 to 13:00 the next day, without a
second day. 0 keeps today and tomorrow from midnight. Slots the list does not hold yet stay empty.

Before 13:00 that is yesterday 13:00 to today 13:00, so the sensor's list must still hold yesterday's afternoon. The EPEX
Spot sensor does. Tibber gives only today and tomorrow; for it, this repository has a Home Assistant package that keeps
the last 24 hours:

1. Copy [`tibber_preise_tessera.yaml`](tibber_preise_tessera.yaml) to `/config/packages/` in Home Assistant (with the
   File editor or Studio Code Server add-on, or over Samba).
2. If your `configuration.yaml` has no packages yet, add
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```
3. Restart Home Assistant. It needs the **Tibber** integration; the package calls its action `tibber.get_prices`
   every 15 minutes.
4. Choose `sensor.tibber_preise_tessera` in the tile's inspector. Its price already holds surcharges and VAT, so leave
   the delivery formula empty.

Right after you add it, the slots before today's midnight stay empty until the sensor has lived through them, so the
graph is complete from the next day on. Home Assistant may log that the sensor's attributes are too big for the
recorder; that only means the history of the list is not saved, the tile is not affected.

## Tried on

- Sunton ESP32-8048S070 (7-inch, 800 x 480), with EPEX Spot and with the Tibber package.
- The plugin bench (`tools/preview.py`) on every screen it renders, light and dark.
