# Games for the ZX Spectrum Next

The hub page at https://mikeynma.github.io/: a card for each game and demo, linking to its own page. Hand-written. Four sections (the owner's choice, 2026-11-20), each with a jump link at the top: **Next games**, **Next demos and labs**, **Spectrum games** (the original 48K and 128K), **Spectrum demos and labs**. A new card goes in its section, newest live ones first, coming-soon ones after, with a tags line under its logo (`<p class="tags">Next &middot; Game</p>`, or `48K &middot; 128K`, `Demo`/`Demos`) and its status badge. "How to play them" has a part for each machine.

The original Spectrum's sites (Borders & Loaders, the Spectrum Sound Lab, Shardstorm; INKWRIGHT when it is out) are generated in the ZX Spectrum repository's `sitegen/`. Their cards take their picture and logo from those sites, so they stay current when the sites are published.

`favicon-32.png` and `apple-touch-icon.png` are the hub's own icon, a pixel joystick: `python3 icon.py` redraws them.

`share.png` is the picture a shared link shows (Facebook, WhatsApp): `python3 share.py` redraws it from the games' own shots. Rerun it when the games on the card change.
