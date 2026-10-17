"""Upgrade every page in place: shared chrome, FAQ schema, cross-links, sitemap and llms.txt. Idempotent."""
import html
import json
import os
import re

from common import ORG, ROOT, SITE, VERSION, call_rail, e, footer, header, links_list
from data_static import SITES, ZONES

AREA_TO_ZONE = {"gulshan": "gulshan-banani-mohakhali", "banani": "gulshan-banani-mohakhali", "mohakhali": "gulshan-banani-mohakhali", "dhanmondi": "dhanmondi-new-market",
                "farmgate": "farmgate-shahbagh", "karwan-bazar": "farmgate-shahbagh", "mirpur": "mirpur", "agargaon": "mirpur", "kamlapur": "motijheel-old-dhaka",
                "sadarghat": "motijheel-old-dhaka", "tejgaon": "badda-purbachal"}

EXTRA_LINKS = {
    "billboard-advertising": ("Browse every billboard location", [("/static-billboards/", f"All {len(SITES)} billboard locations in Dhaka")] + [(f"/static-billboards/{k}/", f"Billboards in {v['short']}") for k, v in ZONES.items()]
                              + [("/expressway-billboard-advertising/", "Expressway billboards"), ("/tri-vision-billboard-advertising/", "Tri-vision billboards"), ("/neon-sign-advertising/", "Neon billboards")]),
    "led-billboard-advertising": ("Go deeper before you book", [("/guides/led-vs-static-billboard/", "LED vs static billboard"), ("/guides/led-billboard-artwork-specifications/", "LED artwork specifications"),
                                                                ("/guides/billboard-advertising-cost-bangladesh/", "How LED airtime is priced"), ("/led-screen-rental/", "Rent an LED wall for an event"), ("/static-billboards/", "Pair with a static billboard")]),
    "outdoor-advertising": ("More outdoor formats", [("/static-billboards/", "Billboard locations in Dhaka"), ("/expressway-billboard-advertising/", "Expressway billboards"), ("/tri-vision-billboard-advertising/", "Tri-vision billboards"),
                                                     ("/neon-sign-advertising/", "Neon sign billboards"), ("/light-box-advertising/", "Light box advertising"), ("/newspaper-insert-advertising/", "Newspaper inserts"), ("/guides/", "Outdoor advertising guides")]),
    "services": ("New and specialist services", [("/expressway-billboard-advertising/", "Expressway billboards"), ("/tri-vision-billboard-advertising/", "Tri-vision billboards"), ("/neon-sign-advertising/", "Neon sign billboards"),
                                                 ("/light-box-advertising/", "Light box advertising"), ("/event-management/", "Event management"), ("/led-screen-rental/", "LED screen rental"),
                                                 ("/store-opening-activation/", "Store opening activation"), ("/newspaper-insert-advertising/", "Newspaper inserts"), ("/large-format-printing/", "Large-format printing"), ("/industries/", "Plans by industry")]),
    "brand-activation": ("Plan the whole experience", [("/event-management/", "Event management & production"), ("/led-screen-rental/", "LED screen rental"), ("/store-opening-activation/", "Store opening activation"), ("/newspaper-insert-advertising/", "Newspaper inserts")]),
    "print-and-media": ("Print and distribution", [("/large-format-printing/", "Large-format printing & banners"), ("/newspaper-insert-advertising/", "Newspaper insert advertising"), ("/light-box-advertising/", "Light boxes")]),
    "outdoor-led-display-installation": ("Before you buy a screen", [("/guides/p4-vs-p5-outdoor-led-display/", "P4 vs P5 outdoor LED display"), ("/led-screen-rental/", "Rent instead of buying")]),
    "campaign-planning": ("Planning resources", [("/guides/how-to-book-a-billboard-in-dhaka/", "How to book a billboard"), ("/guides/billboard-advertising-cost-bangladesh/", "Billboard cost in Bangladesh"), ("/guides/best-billboard-locations-in-dhaka/", "Best locations by audience"), ("/industries/", "Plans by industry")]),
    "advertising-faq": ("Read the full guides", [("/guides/", "All guides"), ("/guides/billboard-advertising-cost-bangladesh/", "Billboard cost in Bangladesh"), ("/guides/outdoor-advertising-glossary/", "Outdoor advertising glossary")]),
    "mid-island-branding": ("Median runs you can book", [("/static-billboards/mirpur/mirpur-10-to-agargaon-mid-island/", "Mirpur-10 to Agargaon (50 panels)"), ("/static-billboards/malibagh-khilgaon-banasree/khilgaon-taltola-mid-island/", "Khilgaon Taltola (50 panels)"), ("/light-box-advertising/", "Light box panels")]),
}

OLD_SITE = "https://ahmedmasum2000000.github.io/dhaka-ad-website"
HEADER_RE = re.compile(r'<a class="skip".*?<nav id="mobile-menu".*?</nav>', re.S)
FOOTER_RE = re.compile(r'<footer class="site-footer.*?</footer>', re.S)
RAIL_RE = re.compile(r'<aside class="call-rail".*?</aside>', re.S)
FAQ_RE = re.compile(r'<details class="faq-item"><summary><span>(.*?)</span>.*?<div class="faq-answer"><p>(.*?)</p>', re.S)
TAG_RE = re.compile(r"<[^>]+>")
LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def upgrade_org(m):
    """Swap the older, minimal Organization node for the full agency entity."""
    data = json.loads(m.group(1))
    graph = data.get("@graph")
    if graph is not None:
        data["@graph"] = [ORG if isinstance(n, dict) and str(n.get("@id", "")).endswith("/#organization") else n for n in graph]
    elif data.get("@type") == "Organization":
        data = {"@context": "https://schema.org", **ORG}
    return f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


def pages():
    for d, _dirs, files in os.walk(ROOT):
        if "/." in d or "/scripts" in d or "/assets" in d:
            continue
        if "index.html" in files:
            yield os.path.join(d, "index.html")


def rel(p):
    r = os.path.relpath(os.path.dirname(p), ROOT)
    return "/" if r == "." else f"/{r}/"


def inject_section(s, key, title, items):
    marker = f'id="growth-{key}"'
    if marker in s:
        s = re.sub(rf'<section class="article-section" {marker}>.*?</section>', "", s, flags=re.S)
    block = f'<section class="article-section" {marker}><p class="eyebrow">KEEP EXPLORING</p><h2>{e(title)}</h2>{links_list(items)}</section>'
    for anchor in ('<div id="questions">', '<section class="article-section closing-call">', "</article>"):
        if anchor in s:
            return s.replace(anchor, block + anchor, 1)
    return s


def upgrade(p):
    with open(p, encoding="utf-8") as f:
        s = f.read()
    s = s.replace(OLD_SITE, SITE)
    if 'name="robots" content="noindex' in s:
        return s, False
    s = HEADER_RE.sub(lambda _m: header(), s, count=1)
    s = FOOTER_RE.sub(lambda _m: footer(), s, count=1)
    s = RAIL_RE.sub(lambda _m: call_rail(), s, count=1)
    s = re.sub(r"\?v=story-3", f"?v={VERSION}", s)
    if "growth.css" not in s:
        s = s.replace("</head>", f'<link rel="stylesheet" href="/dhaka-ad-website/growth.css?v={VERSION}"><script src="/dhaka-ad-website/growth.js?v={VERSION}" defer></script></head>', 1)
    path = rel(p)
    key = path.strip("/")
    if key.startswith("locations/"):
        area = key.split("/", 1)[1]
        zone = AREA_TO_ZONE.get(area)
        if zone:
            z = ZONES[zone]
            items = [(f"/static-billboards/{zone}/", f"All billboards in {z['short']}")] + [(f"/static-billboards/{zone}/{x[1]}/", x[2]) for x in SITES if x[3] == zone][:5]
            s = inject_section(s, "billboards", f"Add a billboard in {z['short']} to your screens", items)
    elif key.startswith("sites/"):
        area = key.split("/")[1]
        zone = AREA_TO_ZONE.get(area)
        if zone:
            s = inject_section(s, "billboards", "Pair this screen with a billboard nearby", [(f"/static-billboards/{zone}/", f"Billboards in {ZONES[zone]['short']}"), ("/guides/led-vs-static-billboard/", "LED vs static: when to combine")])
    elif key in EXTRA_LINKS:
        title, items = EXTRA_LINKS[key]
        s = inject_section(s, "links", title, items)
    s = LD_RE.sub(upgrade_org, s)
    if "FAQPage" not in s:
        qa = [(html.unescape(TAG_RE.sub("", q)).strip(), html.unescape(TAG_RE.sub("", a)).strip()) for q, a in FAQ_RE.findall(s)]
        if qa:
            data = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}
            s = s.replace("</head>", f'<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script></head>', 1)
    return s, True


def sitemap(indexable):
    def prio(path):
        if path == "/":
            return "1.0"
        depth = path.strip("/").count("/")
        return "0.9" if depth == 0 else "0.7" if depth == 1 else "0.6"
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>2026-10-16</lastmod><priority>{prio(p)}</priority></url>" for p in sorted(indexable, key=lambda x: (x.count("/"), x)))
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')


def llms():
    from data_guides import GUIDES
    from data_services import SERVICES
    lines = ["# Dhaka AD", "", "> 360° outdoor advertising agency in Dhaka, Bangladesh. Plans, books, produces and proves outdoor campaigns: LED billboards (56 screens in 10 cities), "
             f"{len(SITES)} static, expressway, tri-vision, neon and mid-island billboard positions across Dhaka, Dhaka Metro Rail in-coach screens (840 screens, ~550,000 daily commuters), "
             "Hazrat Shahjalal airport arrivals LED sign, events and LED wall rental, store opening activations, newspaper inserts, large-format printing, P4/P5 LED installation and digital marketing.", "",
             "Phone: +880 1840 860 284 · Email: info@dhakaad.com · Address: House 5, Flat 5(A), Road 13, DIT Project, Badda, Dhaka, Bangladesh", "",
             "Rates are not published because they change weekly with demand and season; they are given on request by phone.", "", "## Key facts",
             "- Static billboards in Dhaka are usually rented by the year; printing, installation, VAT, tax and AIT are quoted separately.",
             "- LED billboards are sold per minute of daily airtime per screen, typically with a 60-minute daily minimum; creative is usually MP4 at 1920×1080.",
             "- Metro rail in-coach screen campaigns run for 30 days; approved content is due about five days before airing.",
             "- The airport domestic arrivals LED sign (7' × 5') runs 7am–11pm and is rented yearly.",
             "- Static billboard artwork is due about 72 hours before installation.", "", "## Main pages",
             f"- [Home]({SITE}/)", f"- [Billboard locations in Dhaka]({SITE}/static-billboards/)", f"- [LED screens by city]({SITE}/locations/)", f"- [All services]({SITE}/services/)",
             f"- [Advertising FAQs]({SITE}/advertising-faq/)", f"- [Contact]({SITE}/contact/)", "", "## Billboard areas"]
    lines += [f"- [{v['name']}]({SITE}/static-billboards/{k}/): {v['audience']}" for k, v in ZONES.items()]
    lines += ["", "## Services"] + [f"- [{s['h1']}]({SITE}{s['path']})" for s in SERVICES]
    lines += [f"- [LED billboard advertising]({SITE}/led-billboard-advertising/)", f"- [Metro rail advertising]({SITE}/metro-rail-advertising/)", f"- [Airport advertising]({SITE}/airport-advertising/)"]
    lines += ["", "## Guides"] + [f"- [{g['h1']}]({SITE}{g['path']})" for g in GUIDES] + [f"- [Outdoor advertising glossary]({SITE}/guides/outdoor-advertising-glossary/)"]
    with open(os.path.join(ROOT, "llms.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")


def build():
    indexable = []
    for p in pages():
        s, ok = upgrade(p)
        with open(p, "w", encoding="utf-8") as f:
            f.write(s)
        if ok:
            indexable.append(rel(p))
    sitemap(indexable)
    llms()
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\n# AI answer engines are welcome to read and cite this site.\nUser-agent: GPTBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    print("upgraded", len(indexable), "indexable pages")
