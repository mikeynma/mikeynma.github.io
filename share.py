#!/usr/bin/env python3
"""Draw share.png, the 1200x630 picture links to the hub show (og:image).
The games' pictures, three above and two below, from their repos in ~/www. Rerun after
changing which games the card shows, and look at the result."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
WWW = HERE.parent
GAMES = [  # 640x512 shots, drawn at a third: three above, two below
    WWW / "chaos/site/shots/title-card.png",
    WWW / "next-rogue/site/shots/hero.png",
    WWW / "quazadroid/site/shots/title.png",
    "unsung",
    WWW / "stargosy/site/shots/title-card.png",
]


def font(weight, size):
    return ImageFont.truetype(str(HERE / f"fonts/geist-{weight}.woff2"), size)


def mono(size):
    return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", size)


def unsung():  # its shots are 352x288 with no title: a corridor with its logo over it
    site = WWW / "unsung/site"
    im = Image.open(site / "shots/corridor.png").convert("RGB")
    im = im.crop((0, 3, 352, 284)).resize((320, 256), Image.LANCZOS)
    logo = Image.open(site / "logo.webp").convert("RGBA")
    logo = logo.resize((290, logo.height * 290 // logo.width), Image.LANCZOS)
    im.paste(logo, ((320 - 290) // 2, (256 - logo.height) // 2), logo)
    return im


W, H = 1200, 630
img = Image.new("RGB", (W, H), "#09090b")
d = ImageDraw.Draw(img)
CW, CH, gap = 210, 168, 14
gx, gy = W - 40 - (3 * CW + 2 * gap), (H - (2 * CH + gap)) // 2
corner = Image.new("L", (CW, CH), 0)
ImageDraw.Draw(corner).rounded_rectangle((0, 0, CW - 1, CH - 1), 8, fill=255)
for i, g in enumerate(GAMES):
    shot = unsung() if g == "unsung" else Image.open(g).convert("RGB")
    shot = shot.resize((CW, CH), Image.LANCZOS)
    row, col = divmod(i, 3)
    x = gx + col * (CW + gap) + (row * (CW + gap) // 2)   # (the two below sit between the three above)
    y = gy + row * (CH + gap)
    img.paste(shot, (x, y), corner)
    d.rounded_rectangle((x - 1, y - 1, x + CW, y + CH), 9, outline="#27272a")

x = 56
d.text((x, 160), "FREE  ·  ZX SPECTRUM NEXT", font=mono(17), fill="#c4b5fd")
y = 198
for line in ("Games for the", "ZX Spectrum", "Next"):
    d.text((x, y), line, font=font(600, 52), fill="#fafafa")
    y += 60
y += 24
for line in ("Written from scratch in", "Z80 assembly. Free to play."):
    d.text((x, y), line, font=font(400, 24), fill="#a1a1aa")
    y += 34
d.text((x, H - 70), "mikeynma.github.io", font=mono(18), fill="#71717a")
img.save(HERE / "share.png", optimize=True)
print("share.png")
