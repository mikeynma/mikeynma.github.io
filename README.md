# Games for the ZX Spectrum Next

The hub page at https://mikeynma.github.io/: a card for each Next game, linking to its own page. Hand-written: add a card to index.html when a new game gets a page (newest live games first, coming-soon ones after).

Under them, "Also: for the original Spectrum": a card for Borders & Loaders, the border and loader demos for the 48K and 128K (its own site, generated in the ZX Spectrum repository's `sitegen/`). Its picture and logo come from that site, so they stay current when it is published.

`favicon-32.png` and `apple-touch-icon.png` are the hub's own icon, a pixel joystick: `python3 icon.py` redraws them.

`share.png` is the picture a shared link shows (Facebook, WhatsApp): `python3 share.py` redraws it from the games' own shots. Rerun it when the games on the card change.
