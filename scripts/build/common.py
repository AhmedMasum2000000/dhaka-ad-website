"""Shared templates for generated Dhaka AD pages.

Run scripts/build/build.py from the repository root (needs Pillow for image sizes).
"""
import html
import json
import os

BASE = "/dhaka-ad-website"
SITE = "https://dhakaad.com"  # canonical domain; the GitHub Pages copy points here
PHONE = "+8801840860284"
PHONE_SHOW = "01840 860 284"
PHONE_INTL = "+880 1840 860 284"
VERSION = "cine-1"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

e = html.escape


def url(path):
    return BASE + path


def abs_url(path):
    return SITE + path


_size_cache = {}


def img_size(src):
    """Return (w, h) of an image under the repo given its site path (/assets/...)."""
    if src in _size_cache:
        return _size_cache[src]
    from PIL import Image
    p = os.path.join(ROOT, src.lstrip("/"))
    with Image.open(p) as im:
        _size_cache[src] = im.size
    return im.size


def img(src, alt, cls="", lazy=True, sizes=None, priority=False):
    w, h = img_size(src)
    attrs = [f'src="{url(src)}"', f'alt="{e(alt)}"', f'width="{w}"', f'height="{h}"']
    if cls:
        attrs.append(f'class="{cls}"')
    if priority:
        attrs.append('fetchpriority="high"')
    elif lazy:
        attrs.append('loading="lazy" decoding="async"')
    small = src.replace("-1600.webp", "-800.webp").replace("-1200.webp", "-640.webp")
    if small != src and os.path.exists(os.path.join(ROOT, small.lstrip("/"))):
        sw, _ = img_size(small)
        attrs.append(f'srcset="{url(small)} {sw}w, {url(src)} {w}w"')
        attrs.append(f'sizes="{sizes or "(max-width:760px) 100vw, 50vw"}"')
    return "<img " + " ".join(attrs) + ">"


def call_button(label=None, extra=""):
    label = label or f"Call {PHONE_SHOW}"
    return f'<a class="button call-button{(" " + extra) if extra else ""}" href="tel:{PHONE}" data-call>{label} <span aria-hidden="true">↗</span></a>'


ORG = {
    "@type": ["Organization", "ProfessionalService"],
    "@id": abs_url("/#organization"),
    "name": "Dhaka AD",
    "alternateName": "Dhaka AD Outdoor Advertising",
    "description": "360° outdoor advertising agency in Dhaka, Bangladesh: LED billboards, static billboards, expressway, tri-vision and neon boards, metro rail and airport advertising, events, activations, printing and digital marketing.",
    "url": abs_url("/"),
    "logo": abs_url("/assets/dhaka-ad-wordmark-512.png"),
    "image": abs_url("/assets/field/night-street-led-dhaka-1600.webp"),
    "telephone": PHONE_INTL,
    "email": "info@dhakaad.com",
    "address": {"@type": "PostalAddress", "streetAddress": "House 5, Flat 5(A), Road 13, DIT Project, Badda", "addressLocality": "Dhaka", "addressRegion": "Dhaka Division", "addressCountry": "BD"},
    "areaServed": [{"@type": "City", "name": c} for c in ["Dhaka", "Chattogram", "Sylhet", "Cox's Bazar", "Rajshahi", "Cumilla", "Rangpur", "Bogura", "Narayanganj", "Feni"]] + [{"@type": "Country", "name": "Bangladesh"}],
    "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_INTL, "contactType": "sales", "areaServed": "BD", "availableLanguage": ["en", "bn"]},
    "knowsAbout": ["Outdoor advertising", "LED billboard advertising", "Billboard advertising", "Metro rail advertising", "Airport advertising", "Tri-vision billboards", "Neon signs", "Brand activation", "Event management", "LED screen rental", "Newspaper insert advertising", "Large-format printing", "Outdoor LED display installation", "Digital marketing"],
}

NAV = [("/outdoor-advertising/", "Formats"), ("/static-billboards/", "Billboards"), ("/locations/", "LED screens"), ("/event-management/", "Events"), ("/guides/", "Guides")]

MOBILE = [("/outdoor-advertising/", "All outdoor formats"), ("/static-billboards/", "Billboards in Dhaka"), ("/locations/", "LED screens by city"), ("/event-management/", "Events & activation"),
          ("/services/", "Every service"), ("/guides/", "Guides & costs"), ("/advertising-faq/", "Questions answered"), ("/about/", "The agency"), ("/contact/", "Contact")]

FOOT_SERVICES = [
    ("/led-billboard-advertising/", "LED billboard advertising"), ("/billboard-advertising/", "Billboard advertising"), ("/expressway-billboard-advertising/", "Expressway billboards"),
    ("/tri-vision-billboard-advertising/", "Tri-vision billboards"), ("/neon-sign-advertising/", "Neon sign billboards"), ("/light-box-advertising/", "Light box advertising"),
    ("/metro-rail-advertising/", "Metro rail advertising"), ("/airport-advertising/", "Airport advertising"), ("/mid-island-branding/", "Mid-island branding"),
    ("/reflective-mid-island-branding/", "Reflective median panels"), ("/bus-branding/", "Bus branding"), ("/car-branding/", "Car & fleet branding"),
    ("/event-management/", "Event management"), ("/led-screen-rental/", "LED screen rental"), ("/store-opening-activation/", "Store opening activation"),
    ("/brand-activation/", "Brand activation"), ("/newspaper-insert-advertising/", "Newspaper inserts"), ("/large-format-printing/", "Large-format printing"),
    ("/outdoor-led-display-installation/", "P4 & P5 LED installation"), ("/digital-marketing/", "Digital marketing"),
]
FOOT_CITIES = [("/locations/", "All LED locations"), ("/locations/gulshan/", "Gulshan LED screens"), ("/locations/dhanmondi/", "Dhanmondi LED screens"), ("/locations/mohakhali/", "Mohakhali LED screens"),
               ("/locations/mirpur/", "Mirpur LED screens"), ("/locations/chattogram/", "Chattogram"), ("/locations/sylhet/", "Sylhet"), ("/locations/coxs-bazar/", "Cox's Bazar"), ("/locations/rajshahi/", "Rajshahi")]
FOOT_GUIDES = [("/guides/", "All guides"), ("/guides/billboard-advertising-cost-bangladesh/", "Billboard cost in Bangladesh"), ("/guides/led-vs-static-billboard/", "LED vs static billboard"),
               ("/guides/how-to-book-a-billboard-in-dhaka/", "How to book a billboard"), ("/guides/best-billboard-locations-in-dhaka/", "Best billboard locations"),
               ("/guides/led-billboard-artwork-specifications/", "LED artwork specifications"), ("/guides/p4-vs-p5-outdoor-led-display/", "P4 vs P5 LED display"),
               ("/guides/outdoor-advertising-glossary/", "Outdoor advertising glossary"), ("/industries/", "Advertising by industry"), ("/advertising-faq/", "Advertising FAQs")]


def header():
    links = "".join(f'<a href="{url(p)}">{t}</a>' for p, t in NAV)
    mobile = "".join(f'<a href="{url(p)}">{t} <span>{i + 1:02d}</span></a>' for i, (p, t) in enumerate(MOBILE))
    return (f'<a class="skip" href="#main">Skip to content</a><header class="nav"><a class="brand" href="{BASE}/" aria-label="Dhaka AD home">DHAKA AD<span>.</span></a>'
            f'<nav class="desktop-links" aria-label="Main navigation">{links}</nav><a class="nav-cta primary-call" href="tel:{PHONE}" data-call>Call {PHONE_SHOW} <span aria-hidden="true">↗</span></a>'
            f'<button class="menu-toggle" aria-expanded="false" aria-controls="mobile-menu">Menu <span aria-hidden="true">+</span></button></header>'
            f'<nav id="mobile-menu" class="mobile-menu" aria-label="Mobile navigation" hidden>{mobile}<a class="mobile-call" href="tel:{PHONE}" data-call>Call {PHONE_SHOW} <span>↗</span></a></nav>')


def footer():
    from data_static import ZONES
    zones = [("/static-billboards/", "All billboard locations")] + [(f"/static-billboards/{k}/", f"Billboards in {v['short']}") for k, v in ZONES.items()]

    def col(title, items):
        return f'<div><p class="eyebrow">{title}</p>' + "".join(f'<a href="{url(p)}">{e(t)}</a>' for p, t in items) + "</div>"

    return (f'<footer class="site-footer mega-footer section-pad"><div class="footer-lead"><a class="brand" href="{BASE}/">DHAKA AD<span>.</span></a>'
            f'<p>Every outdoor format in Bangladesh, planned, booked and proved by one team. One call gets you a real shortlist.</p>{call_button("Call " + PHONE_INTL)}'
            f'<address>House 5, Flat 5(A), Road 13<br>DIT Project, Badda, Dhaka</address><a href="mailto:info@dhakaad.com">info@dhakaad.com</a>'
            f'<a href="{url("/about/")}">About Dhaka AD</a><a href="{url("/our-work/")}">Our work</a><a href="{url("/contact/")}">Contact</a><span class="micro">© 2026 DHAKA AD</span></div>'
            + col("Services", FOOT_SERVICES) + col("Billboards in Dhaka", zones) + col("LED screens", FOOT_CITIES) + col("Guides", FOOT_GUIDES) + "</footer>")


def call_rail():
    return (f'<aside class="call-rail" aria-label="Call Dhaka AD"><span><strong>Rates and availability change every week.</strong>'
            f'<small>Get today\'s shortlist, dates and rates in one call.</small></span>{call_button("Call " + PHONE_SHOW)}</aside>')


def head(title, desc, path, og_image, graph, extra_head=""):
    data = {"@context": "https://schema.org", "@graph": [ORG] + graph}
    return (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="theme-color" content="#0a0c0e"><title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="robots" content="index,follow,max-image-preview:large">'
            f'<link rel="canonical" href="{abs_url(path)}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}">'
            f'<meta property="og:type" content="website"><meta property="og:url" content="{abs_url(path)}"><meta property="og:image" content="{abs_url(og_image)}"><meta property="og:locale" content="en_GB">'
            f'<meta name="twitter:card" content="summary_large_image"><meta name="geo.region" content="BD-13"><meta name="geo.placename" content="Dhaka">'
            f'<link rel="icon" href="{BASE}/favicon.ico?v=red-wordmark-2"><link rel="icon" type="image/png" href="{BASE}/assets/dhaka-ad-favicon-red.png?v=2" sizes="32x32">'
            f'<link rel="apple-touch-icon" href="{BASE}/assets/apple-touch-icon.png?v=2">'
            f'<link rel="stylesheet" href="{BASE}/style.css?v={VERSION}"><link rel="stylesheet" href="{BASE}/content.css?v={VERSION}"><link rel="stylesheet" href="{BASE}/growth.css?v={VERSION}">'
            f'{extra_head}<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'
            f'<script src="{BASE}/content.js?v={VERSION}" defer></script><script src="{BASE}/growth.js?v={VERSION}" defer></script></head>')


def breadcrumb_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": abs_url(p)} for i, (p, n) in enumerate(crumbs)]}


def webpage_schema(path, title, desc, image, kind="WebPage"):
    return {"@type": kind, "@id": abs_url(path) + "#page", "url": abs_url(path), "name": title, "description": desc, "inLanguage": "en-GB",
            "isPartOf": {"@type": "WebSite", "@id": abs_url("/#website"), "name": "Dhaka AD", "url": abs_url("/")},
            "primaryImageOfPage": {"@type": "ImageObject", "url": abs_url(image)}, "publisher": {"@id": abs_url("/#organization")},
            "dateModified": "2026-10-16"}


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a, *_ in faqs]}


def faq_items(faqs, default_link=("/contact/", "Plan your campaign")):
    out = []
    for f in faqs:
        q, a = f[0], f[1]
        link = f[2] if len(f) > 2 and f[2] else default_link
        out.append(f'<details class="faq-item"><summary><span>{e(q)}</span><i aria-hidden="true">+</i></summary><div class="faq-answer"><p>{e(a)}</p>'
                   f'<div class="faq-next"><a class="text-link" href="{url(link[0])}">{e(link[1])} <span aria-hidden="true">↗</span></a>'
                   f'<a class="faq-call" href="tel:{PHONE}" data-call>Still deciding? Ask us directly · {PHONE_SHOW} ↗</a></div></div></details>')
    return "".join(out)


def faq_section(faqs, title="Questions buyers ask before they call", default_link=("/contact/", "Plan your campaign")):
    return (f'<div id="questions"><section class="faq-block" id="faq"><p class="eyebrow">QUICK, STRAIGHT ANSWERS</p><h2>{e(title)}</h2>'
            f'{faq_items(faqs, default_link)}</section></div>')


def crumbs_html(crumbs):
    parts = []
    for i, (p, n) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<span aria-current="page">{e(n)}</span>')
        else:
            parts.append(f'<a href="{url(p)}">{e(n)}</a>')
    return '<nav class="breadcrumbs" aria-label="Breadcrumb">' + "<span>/</span>".join(parts) + "</nav>"


def quick_answer(text, facts=None):
    fx = ""
    if facts:
        fx = '<dl class="qa-facts">' + "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in facts) + "</dl>"
    return f'<aside class="quick-answer" aria-label="Quick answer"><p class="eyebrow"><i class="dot amber"></i> QUICK ANSWER</p><p>{text}</p>{fx}</aside>'


def card(href, image, alt, title, text, cta="Explore", tag=None):
    t = f'<span class="card-tag">{e(tag)}</span>' if tag else ""
    return (f'<article class="outdoor-card"><a class="outdoor-image" href="{url(href)}">{img(image, alt, sizes="(max-width:760px) 100vw, 33vw")}{t}<span aria-hidden="true">↗</span></a>'
            f'<div class="outdoor-card-copy"><h3><a href="{url(href)}">{e(title)}</a></h3><p>{e(text)}</p><a class="text-link" href="{url(href)}">{e(cta)} <span aria-hidden="true">↗</span></a></div></article>')


def links_list(items):
    return '<div class="directory-links">' + "".join(f'<a href="{url(p)}"><span>{e(t)}</span><span aria-hidden="true">↗</span></a>' for p, t in items) + "</div>"


def page(path, title, desc, og_image, graph, crumbs, eyebrow, h1, intro_html, hero_image, hero_alt, sections, faqs=None, faq_title=None,
         related=None, closing=None, qa=None, gallery=None, body_class="content-page"):
    """Standard editorial page. sections: list of (id, eyebrow, h2, inner_html)."""
    graph = list(graph) + [webpage_schema(path, title, desc, hero_image), breadcrumb_schema(crumbs)]
    if faqs:
        graph.append(faq_schema(faqs))
    toc = "".join(f'<a href="#{sid}">{e(h2)}</a>' for sid, _, h2, _ in sections)
    if faqs:
        toc += '<a href="#questions">Questions answered</a>'
    body_sections = "".join(f'<section class="article-section" id="{sid}"><p class="eyebrow">{e(eb)}</p><h2>{e(h2)}</h2>{inner}</section>' for sid, eb, h2, inner in sections)
    gal = ""
    if gallery:
        gal = ('<section class="article-section field-strip"><p class="eyebrow">FROM THE FIELD</p><h2>Real work. Real streets.</h2><div class="field-grid">'
               + "".join(f'<figure>{img(s, a, sizes="(max-width:760px) 100vw, 33vw")}<figcaption>{e(a)}</figcaption></figure>' for s, a in gallery) + "</div></section>")
    rel = ""
    if related:
        rel = f'<section class="article-section"><p class="eyebrow">KEEP EXPLORING</p><h2>Compare before you commit</h2>{links_list(related)}</section>'
    closing = closing or ("Your audience. Your area. Your dates.", "Three answers are all we need. You get a shortlist of real placements, current availability and a clear quotation, usually the same day.")
    close = (f'<section class="article-section closing-call"><p class="eyebrow">THE NEXT MOVE IS YOURS</p><h2>{e(closing[0])}</h2><p>{e(closing[1])}</p>'
             f'<div class="button-row">{call_button("Call " + PHONE_INTL)}<a class="text-link" href="https://wa.me/8801840860284" rel="noopener">Prefer WhatsApp? <span aria-hidden="true">↗</span></a></div></section>')
    faq_html = faq_section(faqs, faq_title or "Questions buyers ask before they call") if faqs else ""
    hero_photo = f'<figure class="page-photo">{img(hero_image, hero_alt, lazy=False, priority=True, sizes="100vw")}<figcaption>{e(hero_alt.upper())}</figcaption></figure>' if hero_image else ""
    return (head(title, desc, path, hero_image, graph) + f'<body class="{body_class}">' + header() +
            f'<main id="main"><section class="page-hero section-pad">{crumbs_html(crumbs)}<p class="eyebrow">{e(eyebrow)}</p><h1>{e(h1)}</h1>'
            f'<div class="page-intro"><div class="intro-copy">{intro_html}</div><div>{call_button("Call " + PHONE_INTL)}<span class="small-note">Free shortlist · Live availability · No obligation</span>{qa or ""}</div></div>{hero_photo}</section>'
            f'<div class="reading-layout section-pad"><aside class="reading-nav"><p class="eyebrow">ON THIS PAGE</p>{toc}<a class="text-link" href="tel:{PHONE}" data-call>Talk to a planner <span aria-hidden="true">↗</span></a></aside>'
            f'<article class="reading-body">{body_sections}{gal}{faq_html}{rel}{close}</article></div></main>' + footer() + call_rail() + "</body></html>")


def write(path, html_text):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_text)
    return out
