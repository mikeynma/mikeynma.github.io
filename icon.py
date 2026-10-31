#!/usr/bin/env python3
"""Draw the hub's own icons: favicon-32.png and apple-touch-icon.png.
A pixel joystick on a dark violet tile (the page's colours), drawn on a 16x16 grid at 2x and 10x.
Change PIXELS and rerun, then look at both at their real size."""
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).parent
TILE = "#1e1033"                     # --primary-fg
COLOURS = {
    "w": "#fee2e2", "r": "#ef4444", "d": "#b91c1c",            # the ball: shine, red, shade
    "s": "#e4e4e7", "g": "#a1a1aa",                            # the stick
    "L": "#c4b5fd", "V": "#8b5cf6", "D": "#5b21b6",            # the base: top, front, shadow
    "y": "#facc15", "o": "#ca8a04",                            # the fire button
}
PIXELS = """
................
......rrr.......
.....rwrrr......
....rwrrrrd.....
....rrrrrdd.....
.....rrddd......
......ddd.......
.......sg.......
.......sg.......
.......sg.......
..yy...sg.......
.LyoLLLsgLLLLLL.
.LLLLLLLLLLLLLL.
.VVVVVVVVVVVVVV.
.DDDDDDDDDDDDDD.
................
""".split()


def draw(scale, pad):
    n = 16 * scale + 2 * pad
    img = Image.new("RGBA", (n * 4, n * 4))                    # the tile at 4x, for smooth corners
    ImageDraw.Draw(img).rounded_rectangle((0, 0, n * 4 - 1, n * 4 - 1), n, fill=TILE)
    img = img.resize((n, n), Image.LANCZOS)
    d = ImageDraw.Draw(img)
    for y, row in enumerate(PIXELS):
        for x, c in enumerate(row):
            if c != ".":
                x0, y0 = pad + x * scale, pad + y * scale
                d.rectangle((x0, y0, x0 + scale - 1, y0 + scale - 1), fill=COLOURS[c])
    return img


draw(2, 0).save(HERE / "favicon-32.png", optimize=True)
touch = Image.new("RGB", (180, 180), TILE)                     # iOS rounds the corners itself
big = draw(10, 10)
touch.paste(big, (0, 0), big)
touch.save(HERE / "apple-touch-icon.png", optimize=True)
print("favicon-32.png, apple-touch-icon.png")
