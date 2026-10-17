"""Service, guide, glossary and industry pages."""
from common import PHONE_SHOW, abs_url, card, e, links_list, page, write
from data_guides import GLOSSARY, GUIDES, INDUSTRIES
from data_services import F, P, SERVICES, UL


def build_standard(d, crumb_parent, extra_graph=None):
    path = d["path"]
    crumbs = [("/", "Home"), crumb_parent, (path, d["h1"])]
    graph = list(extra_graph or [])
    if crumb_parent[0] == "/services/":
        graph.append({"@type": "Service", "name": d["h1"], "serviceType": d["fmt"].title(), "provider": {"@id": abs_url("/#organization")},
                      "areaServed": {"@type": "Country", "name": "Bangladesh"}, "url": abs_url(path)})
    if d.get("howto"):
        graph.append({"@type": "HowTo", "name": d["h1"], "step": [{"@type": "HowToStep", "position": i + 1, "text": s} for i, s in enumerate(d["howto"])]})
    if crumb_parent[0] == "/guides/":
        graph.append({"@type": "Article", "headline": d["h1"], "author": {"@id": abs_url("/#organization")}, "publisher": {"@id": abs_url("/#organization")},
                      "datePublished": "2026-10-16", "dateModified": "2026-10-16", "image": abs_url(d["hero"][0]), "mainEntityOfPage": abs_url(path)})
    sections = d["sections"]
    if d.get("howto"):
        sections = [("steps", "THE 7 STEPS", "The process at a glance", "<ol class='steps'>" + "".join(f"<li>{e(s)}</li>" for s in d["howto"]) + "</ol>")] + sections
    write(path, page(path, d["title"], d["desc"], d["hero"][0], graph, crumbs, f"DHAKA AD / {d['fmt']}", d["h1"], d["intro"], d["hero"][0], d["hero"][1],
                     sections, d.get("faqs"), related=d.get("related"), qa=d.get("qa"), gallery=d.get("gallery")))


def build_glossary():
    path = "/guides/outdoor-advertising-glossary/"
    terms = "".join(f'<div class="term" id="{e(t.split(" (")[0].lower().replace(" ", "-").replace("/", ""))}"><dt>{e(t)}</dt><dd>{e(d)}</dd></div>' for t, d in GLOSSARY)
    sections = [("terms", "A–Z", f"{len(GLOSSARY)} outdoor advertising terms, explained simply", f'<dl class="glossary">{terms}</dl>')]
    graph = [{"@type": "DefinedTermSet", "name": "Outdoor advertising glossary", "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSSARY]}]
    faqs = [("What does OOH mean in advertising?", GLOSSARY[0][1], None), ("What is DOOH?", GLOSSARY[1][1], None), ("What does pixel pitch mean?", GLOSSARY[15][1], ("/guides/p4-vs-p5-outdoor-led-display/", "P4 vs P5 explained"))]
    write(path, page(path, "Outdoor advertising glossary: OOH terms explained | Dhaka AD", "Plain-English definitions of outdoor advertising terms: OOH, DOOH, airtime, facing, tri-vision, pixel pitch, IP65, log summary, AIT and more.",
                     F("multi-format-building-advertising"), graph, [("/", "Home"), ("/guides/", "Guides"), (path, "Outdoor advertising glossary")], "DHAKA AD / GUIDE / GLOSSARY",
                     "Outdoor advertising glossary", P("<strong>Quotations are full of jargon. You should never sign something you do not fully understand.</strong> Here is every term you are likely to meet, in one sentence each."),
                     F("multi-format-building-advertising"), "Building with several advertising formats", sections, faqs,
                     related=[("/guides/", "All guides"), ("/guides/billboard-advertising-cost-bangladesh/", "Billboard cost guide"), ("/advertising-faq/", "Advertising FAQs")]))


def build_guides_hub():
    path = "/guides/"
    cards = '<div class="outdoor-grid">' + "".join(card(g["path"], g["hero"][0], g["hero"][1], g["h1"], g["desc"].split(".")[0] + ".", "Read the guide") for g in GUIDES) + \
            card("/guides/outdoor-advertising-glossary/", F("multi-format-building-advertising"), "Building with several advertising formats", "Outdoor advertising glossary", "Every term in a quotation, explained in one sentence.", "Read the glossary") + "</div>"
    faqs = [("How do I start an outdoor advertising campaign in Bangladesh?", "Define who you want to reach, where they travel and when you want to launch, then ask for a shortlist of available placements with photos and a written quotation. Dhaka AD does this in one call.", ("/guides/how-to-book-a-billboard-in-dhaka/", "How booking works")),
            ("What is the most effective outdoor advertising in Dhaka?", "The format that sits on your customer's daily route. For premium audiences that is often LED at Gulshan or expressway boards; for mass reach, metro screens and large static faces; for local outlets, inserts, banners and nearby boards.", ("/guides/best-billboard-locations-in-dhaka/", "Best locations by audience"))]
    write(path, page(path, "Outdoor advertising guides for Bangladesh | Dhaka AD", "Practical guides to billboard cost, LED vs static, booking, locations, artwork specifications and LED hardware in Bangladesh, from Dhaka AD.",
                     F("gulshan-circle-median-view"), [], [("/", "Home"), (path, "Guides")], "DHAKA AD / GUIDES", "Outdoor advertising guides for Bangladesh",
                     P("<strong>Spend an evening reading, and you will ask sharper questions than most media buyers.</strong> These guides answer what clients ask us every week: what it costs, which format, which location, which file."),
                     F("gulshan-circle-median-view"), "View across a Gulshan circle with LED screens", [("all-guides", "READ", "Every guide", cards)], faqs))


def build_industries():
    hub = "/industries/"
    for slug, name, pitch, plan, links, image in INDUSTRIES:
        path = f"/industries/{slug}/"
        sections = [
            ("challenge", "01 / THE CHALLENGE", f"What {name.lower()} brands are up against", P(pitch)),
            ("plan", "02 / THE PLAN", "A media mix that works for this sector", UL(plan)),
            ("where", "03 / WHERE", "Start with these placements", links_list(links)),
            ("next", "04 / NEXT", "Get a plan built for your brand", P(f"Tell us your goal, audience and launch date. We will come back with a shortlist, a mock-up and a clear quotation. Call {PHONE_SHOW}.")),
        ]
        faqs = [(f"What is the best outdoor advertising for {name.lower()} in Bangladesh?", f"{pitch} A typical mix: {', '.join(p.lower() for p in plan[:3])}.", links[0]),
                (f"Can you plan a national campaign for a {name.lower()} brand?", "Yes. We combine Dhaka placements with LED screens in Chattogram, Sylhet, Cox's Bazar, Rajshahi and other cities, under one plan and one invoice.", ("/locations/", "LED screens by city"))]
        write(path, page(path, f"Outdoor advertising for {name.lower()} in Bangladesh | Dhaka AD", f"Billboard, LED and activation plans for {name.lower()} brands in Bangladesh. {pitch[:90]}... Call {PHONE_SHOW}.",
                         image, [], [("/", "Home"), (hub, "Industries"), (path, name)], f"DHAKA AD / INDUSTRIES / {name.upper()}", f"Outdoor advertising for {name.lower()}",
                         P(f"<strong>{pitch.split('. ')[0]}.</strong> {'. '.join(pitch.split('. ')[1:])}"), image, f"Advertising placement for {name.lower()} brands", sections, faqs,
                         related=[(hub, "All industries"), ("/static-billboards/", "Billboard locations"), ("/guides/best-billboard-locations-in-dhaka/", "Best locations by audience")]))
    cards = '<div class="outdoor-grid">' + "".join(card(f"/industries/{s}/", img, n, n, p.split(". ")[0] + ".", "See the plan") for s, n, p, _, _, img in INDUSTRIES) + "</div>"
    write(hub, page(hub, "Outdoor advertising by industry in Bangladesh | Dhaka AD", "Outdoor advertising plans for real estate, retail, telecom and fintech, education, healthcare and travel brands in Bangladesh.",
                    F("traffic-approach-led-tower"), [], [("/", "Home"), (hub, "Industries")], "DHAKA AD / INDUSTRIES", "Outdoor advertising by industry",
                    P("<strong>A developer, a coaching centre and a bank should never get the same plan.</strong> Pick your sector to see where your customers travel and the mix we would start with."),
                    F("traffic-approach-led-tower"), "Traffic approaching a tower with LED screens", [("sectors", "SECTORS", "Choose your industry", cards)], None))


def build():
    for s in SERVICES:
        build_standard(s, ("/services/", "Services"))
    for g in GUIDES:
        build_standard(g, ("/guides/", "Guides"))
    build_glossary()
    build_guides_hub()
    build_industries()
    build_404()
    build_thank_you()


def build_404():
    """Friendly not-found page: keeps lost visitors one tap from the phone."""
    from common import ROOT, call_button, footer, head, header, call_rail, PHONE_SHOW, url
    import os
    links = links_list([("/static-billboards/", "Billboard locations in Dhaka"), ("/locations/", "LED screens by city"), ("/services/", "Every service"), ("/guides/", "Guides & costs"), ("/advertising-faq/", "Questions answered")])
    html = (head("Page not found | Dhaka AD", "This page has moved. Find billboards, LED screens and services, or call Dhaka AD.", "/404.html", "/assets/field/night-street-led-dhaka-1600.webp", [])
            .replace('content="index,follow,max-image-preview:large"', 'content="noindex,follow"')
            + '<body class="content-page">' + header()
            + f'<main id="main"><section class="page-hero section-pad"><p class="eyebrow">404 / WRONG TURN</p><h1>This page took a different road.</h1>'
            + f'<div class="page-intro"><div class="intro-copy"><p><strong>The billboard you were looking for is still out there.</strong> Pick a starting point below, or call and tell us what you need.</p>{links}</div>'
            + f'<div>{call_button("Call " + PHONE_SHOW)}<a class="text-link" href="{url("/")}">Back to the homepage <span aria-hidden="true">↗</span></a></div></div></section></main>'
            + footer() + call_rail() + "</body></html>")
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html)


def build_thank_you():
    """Where contact.php sends people after a callback request (noindex)."""
    from common import call_button, footer, head, header, call_rail, PHONE_SHOW, url
    path = "/thank-you/"
    links = links_list([("/static-billboards/", "Browse billboard locations"), ("/guides/billboard-advertising-cost-bangladesh/", "What affects the cost"), ("/guides/led-billboard-artwork-specifications/", "Get your artwork ready")])
    html = (head("Thank you | Dhaka AD", "Your callback request reached Dhaka AD. A planner will call you back shortly.", path, "/assets/field/night-street-led-dhaka-1600.webp", [])
            .replace('content="index,follow,max-image-preview:large"', 'content="noindex,follow"')
            + '<body class="content-page">' + header()
            + '<main id="main"><section class="page-hero section-pad"><p class="eyebrow">REQUEST RECEIVED</p><h1>Thank you. Your callback is in the queue.</h1>'
            + f'<div class="page-intro"><div class="intro-copy"><p><strong>A planner will call you back, usually the same working day.</strong> In a hurry? Call now and we can start straight away.</p>{links}</div>'
            + f'<div>{call_button("Call " + PHONE_SHOW)}<a class="text-link" href="{url("/")}">Back to the homepage <span aria-hidden="true">↗</span></a></div></div></section></main>'
            + footer() + call_rail() + "</body></html>")
    write(path, html)
