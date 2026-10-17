"""Static billboard hub, zone pages and individual site pages."""
from common import (PHONE, PHONE_SHOW, card, call_button, e, links_list, page, quick_answer, url, write, abs_url)
from data_static import FORMATS, SITES, ZONES

FORMAT_TIPS = {
    "static": "A printed static board carries one design for the whole term, so it rewards a single, confident idea: one image, your brand, five to seven words, and something people can act on later.",
    "expressway": "Expressway traffic reads you at speed and from a distance. Use a huge brand mark, one bold visual and no more than five words. Phone numbers and fine print disappear at 60 km/h.",
    "trivision": "A tri-vision board rotates three printed faces. The movement itself pulls attention. Book all three faces to own the position, or share it and hold one face at a premium address for less.",
    "neon": "Neon and lit boards work twice: by day as a large-format board and after dark as one of the few bright things on the road. Keep shapes simple so the lighting reads cleanly at night.",
    "midisland": "Median panels win by repetition. The same message appears again and again along the road, so even a two-second glance at each panel adds up to real recall by the end of the drive.",
    "lightbox": "Panels can be produced as reflective sticker or as an illuminated light box. Light boxes keep you visible after sunset, when this road is still busy with shoppers heading home.",
    "wall": "A building-wall face is seen from far away and for a long time. Treat it like a poster for the whole street: dramatic image, short line, unmistakable brand.",
}


def site_path(s):
    return f"/static-billboards/{s[3]}/{s[1]}/"


def site_img(s):
    return f"/assets/billboards/{s[1]}-1200.webp"


def zone_sites(zone):
    return [s for s in SITES if s[3] == zone]


def site_card(s):
    pg, slug, name, zone, size, sqft, facing, fmt, note = s
    return card(site_path(s), site_img(s), f"{name} billboard location", name, note, "See this placement", FORMATS[fmt][0])


def build_sites():
    for s in SITES:
        pg, slug, name, zone, size, sqft, facing, fmt, note = s
        z = ZONES[zone]
        fname, fpath = FORMATS[fmt]
        path = site_path(s)
        title = f"{name} billboard | {fname} in {z['short']}, Dhaka"
        if len(title) > 70:
            title = f"{name} | Billboard in Dhaka"
        desc = f"{fname} at {name}: {size}, about {sqft} sq ft, facing {facing}. {note} Call {PHONE_SHOW} for today's availability and rate."
        crumbs = [("/", "Home"), ("/static-billboards/", "Billboards in Dhaka"), (f"/static-billboards/{zone}/", z["short"]), (path, name)]
        rows = [("Location", name), ("Area", z["name"]), ("Format", fname), ("Size", size), ("Display area", f"About {sqft} sq ft"), ("Facing", facing),
                ("Typical term", "Usually booked by the year. Ask about shorter terms."), ("Today's rate", "Confirmed on a call. Rates move with demand.")]
        table = ('<div class="table-scroll" tabindex="0" role="region" aria-label="Placement details"><table><thead><tr><th scope="col">Detail</th><th scope="col">This placement</th></tr></thead><tbody>'
                 + "".join(f"<tr><td>{e(k)}</td><td>{e(v)}</td></tr>" for k, v in rows) + "</tbody></table></div>")
        others = [x for x in zone_sites(zone) if x[1] != slug]
        rel = [(site_path(x), x[2]) for x in others[:6]] + [(f"/locations/{k}/", t) for k, t in z["led_links"]] + [(f"/static-billboards/{zone}/", f"Every billboard in {z['short']}"), (fpath, f"How {fname.lower()}s work")]
        intro = (f"<p><strong>{e(note)}</strong> This {e(fname.lower())} measures {e(size)} (about {e(sqft)} sq ft) and faces {e(facing)}. "
                 f"It is one of {len(zone_sites(zone))} billboard positions we plan in {e(z['short'])}, and one of {len(SITES)} across Dhaka.</p>"
                 f"<p>The exact rate, free dates and production schedule change week to week, so we confirm them live. Call, name this location, and you will know within minutes whether it fits your dates.</p>")
        qa = quick_answer(f"{e(name)} is a {e(fname.lower())} in {e(z['short'])}, Dhaka, size {e(size)}, facing {e(facing)}. Book it through Dhaka AD on {PHONE_SHOW}.",
                          [("Size", size), ("Facing", facing), ("Format", fname)])
        sections = [
            ("at-a-glance", "01 / THE FACTS", "The placement at a glance", f"<p>Everything you need to shortlist this board. The two things that change weekly, availability and rate, we confirm on the call.</p>{table}"),
            ("who-sees-it", "02 / THE AUDIENCE", "Who will see your brand here?", f"<p>{e(z['story'])}</p><p><strong>Typical audience:</strong> {e(z['audience'])}.</p><p>{e(note)}</p>"),
            ("creative", "03 / THE CREATIVE", "Make this board impossible to ignore", f"<p>{e(FORMAT_TIPS[fmt])}</p><ul><li>Ask us for a mock-up of your artwork on this exact photograph before you print.</li><li>We confirm the final print size and file format with production, never from a photograph.</li><li>Approved artwork is needed about 72 hours before installation.</li></ul>"),
            ("booking", "04 / THE BOOKING", "How booking this placement works", "<ol class='steps'><li><strong>Call</strong> and name this location with your preferred start date.</li><li><strong>Get the quotation</strong> with media, printing and installation shown as separate lines, so you know exactly what you are paying for.</li><li><strong>Approve the mock-up</strong> and confirm the work order.</li><li><strong>Go live</strong> and receive installation photographs as proof.</li></ol><p>Government taxes and VAT are quoted separately and transparently. Payment is normally staged across the term.</p>"),
            ("nearby", "05 / ALSO NEARBY", f"More placements around {z['short']}", f"<p>Two or three faces on the same route build recall faster than one. These are the closest alternatives and companions.</p>{links_list(rel)}"),
        ]
        faqs = [
            (f"How big is the {name} billboard?", f"The board measures {size}, a display area of about {sqft} square feet, and it faces {facing}. We confirm the exact print size with production before you send artwork.", (f"/static-billboards/{zone}/", f"Compare {z['short']} sizes")),
            (f"How much does the {name} billboard cost?", f"The rate depends on the booking term, the season and current demand, so we quote it live rather than publishing a figure that may be out of date. Call {PHONE_SHOW} and you will have today's rate, available dates and a written quotation the same day.", ("/guides/billboard-advertising-cost-bangladesh/", "How billboard pricing works")),
            (f"Who sees the {name} billboard?", f"{z['audience']}. {note}", (f"/static-billboards/{zone}/", f"Explore {z['short']}")),
            ("Is printing and installation included?", "We quote media rent, printing and installation as separate lines so you can see each cost. We handle all three for you, and you receive photographs once the board is up.", ("/large-format-printing/", "See how we print")),
        ]
        html_text = page(path, title, desc, site_img(s), [{"@type": "Place", "name": f"{name} billboard", "address": {"@type": "PostalAddress", "addressLocality": "Dhaka", "addressCountry": "BD"}, "image": abs_url(site_img(s))}],
                         crumbs, f"DHAKA AD / {fname.upper()} / {z['short'].upper()}", f"{name}: {fname.lower()} in {z['short']}", intro, site_img(s),
                         f"{name} billboard placement photograph", sections, faqs, related=None, qa=qa,
                         closing=(f"Want {name} for your brand?", "Rates and free dates move every week. One call tells you whether this board fits your launch, and what the best alternative is if it does not."))
        write(path, html_text)


def build_zones():
    for zone, z in ZONES.items():
        sites = zone_sites(zone)
        path = f"/static-billboards/{zone}/"
        title = f"Billboard advertising in {z['short']}, Dhaka | {len(sites)} locations"
        desc = f"Compare {len(sites)} billboard locations in {z['name']} with photos, sizes and facing directions. {z['audience']}. Call {PHONE_SHOW} for today's availability."
        crumbs = [("/", "Home"), ("/static-billboards/", "Billboards in Dhaka"), (path, z["short"])]
        rows = "".join(f'<tr><td><a href="{url(site_path(s))}">{e(s[2])}</a></td><td>{e(FORMATS[s[7]][0])}</td><td>{e(s[4])}</td><td>{e(s[6])}</td></tr>' for s in sites)
        table = f'<div class="table-scroll" tabindex="0" role="region" aria-label="Billboards in {e(z["short"])}"><table><thead><tr><th scope="col">Location</th><th scope="col">Format</th><th scope="col">Size</th><th scope="col">Facing</th></tr></thead><tbody>{rows}</tbody></table></div>'
        grid = '<div class="outdoor-grid">' + "".join(site_card(s) for s in sites) + "</div>"
        other_zones = [(f"/static-billboards/{k}/", f"Billboards in {v['short']}") for k, v in ZONES.items() if k != zone]
        led = [(f"/locations/{k}/", t) for k, t in z["led_links"]]
        intro = (f"<p><strong>Where does your customer drive every day?</strong> If the answer is {e(z['short'])}, these {len(sites)} boards put your brand directly in their path.</p><p>{e(z['story'])}</p>")
        qa = quick_answer(f"Dhaka AD plans {len(sites)} billboard locations in {e(z['name'])}, including {e(', '.join(s[2] for s in sites[:3]))}. Availability and rates are confirmed on {PHONE_SHOW}.",
                          [("Locations", str(len(sites))), ("Audience", z["audience"].split(",")[0])])
        sections = [
            ("locations", "01 / EVERY PLACEMENT", f"All {len(sites)} billboard locations in {z['short']}", f"<p>Sizes and facing directions for every placement. Tap any name to see the photograph and full details.</p>{table}"),
            ("photos", "02 / SEE THEM", "See each location before you decide", grid),
            ("audience", "03 / THE AUDIENCE", f"Who you reach in {z['short']}", f"<p>{e(z['story'])}</p><p><strong>Typical audience:</strong> {e(z['audience'])}.</p>"),
            ("combine", "04 / AMPLIFY", "Combine boards for faster recall", f"<p>Your customer rarely sees one board once. Two faces on the same route, or a static board paired with an LED screen nearby, turn a passing glance into a memory. Ask us to build a route plan around your outlet or launch.</p>{links_list(led + [('/led-billboard-advertising/', 'Add LED screens to the mix'), ('/guides/best-billboard-locations-in-dhaka/', 'Best locations by audience')])}"),
            ("more-areas", "05 / OTHER AREAS", "Billboards in other parts of Dhaka", links_list(other_zones)),
        ]
        faqs = [
            (f"How many billboard locations are there in {z['short']}?", f"Dhaka AD currently plans {len(sites)} billboard positions in {z['name']}: {', '.join(s[2] for s in sites)}. Call to confirm which are free for your dates.", ("/static-billboards/", "See all Dhaka locations")),
            (f"Which billboard in {z['short']} is best for my brand?", f"It depends on the direction your customers travel and what you want them to do. Tell us your audience and goal, and we will shortlist the two or three faces that fit, with photographs.", ("/guides/best-billboard-locations-in-dhaka/", "Best locations by audience")),
            (f"What does a billboard in {z['short']} cost?", "Rates depend on size, position, term and demand, and they change through the year. We give you today's rate and dates on the call, then confirm everything in a written quotation.", ("/guides/billboard-advertising-cost-bangladesh/", "How pricing works")),
        ]
        write(path, page(path, title, desc, site_img(sites[0]), [], crumbs, f"DHAKA AD / BILLBOARDS / {z['short'].upper()}", f"Billboard advertising in {z['name']}",
                         intro, site_img(sites[0]), f"{sites[0][2]} billboard placement", sections, faqs, qa=qa,
                         closing=(f"Own your corner of {z['short']}.", "Tell us where your customers are. We will tell you which faces are free, what they cost this month and how fast you can go live.")))


def build_hub():
    path = "/static-billboards/"
    title = f"Billboard advertising in Dhaka | {len(SITES)} locations with photos"
    desc = f"Browse {len(SITES)} billboard locations in Dhaka: expressway, tri-vision, neon, mid-island and giant wall boards, with photos, sizes and facing. Call {PHONE_SHOW} for availability."
    crumbs = [("/", "Home"), (path, "Billboards in Dhaka")]
    chips = '<div class="zone-filter" role="group" aria-label="Filter by area"><button aria-pressed="true" data-zone="all">All areas</button>' + "".join(
        f'<button aria-pressed="false" data-zone="{k}">{e(v["short"])}</button>' for k, v in ZONES.items()) + "</div>"
    grid = '<div class="outdoor-grid zone-grid">' + "".join(f'<div data-zone-item="{s[3]}">{site_card(s)}</div>' for s in SITES) + "</div>"
    zone_links = [(f"/static-billboards/{k}/", f"{v['name']} ({len(zone_sites(k))})") for k, v in ZONES.items()]
    fmt_counts = {}
    for s in SITES:
        fmt_counts[s[7]] = fmt_counts.get(s[7], 0) + 1
    fmt_links = [(FORMATS[k][1], f"{FORMATS[k][0]} ({n})") for k, n in sorted(fmt_counts.items(), key=lambda x: -x[1])]
    intro = ("<p><strong>Every day, millions of people cross Dhaka on the same few roads. The question is whose name they see.</strong></p>"
             f"<p>Here are {len(SITES)} billboard locations we plan across Dhaka, from the Elevated Expressway and Purbachal 300 Feet to Gulistan's giant wall boards, Old Dhaka, Mirpur, Keraniganj and the Ashulia garment belt. Filter by area, open any placement for photos and sizes, then call to lock your dates.</p>")
    qa = quick_answer(f"Dhaka AD offers {len(SITES)} billboard locations across 10 Dhaka areas, plus 56 LED screens in 10 cities. Formats include static, expressway, tri-vision, neon, mid-island and building-wall boards. Rates are confirmed on {PHONE_SHOW}.",
                      [("Billboard locations", str(len(SITES))), ("Dhaka areas", "10"), ("Largest face", "9,500 sq ft")])
    sections = [
        ("browse", "01 / BROWSE", "Find a billboard on your customer's route", chips + grid),
        ("areas", "02 / BY AREA", "Billboards by area", links_list(zone_links)),
        ("formats", "03 / BY FORMAT", "Billboards by format", "<p>Each format suits a different job. Expressway faces build scale, tri-vision brings movement, neon owns the night and mid-island runs repeat your message dozens of times along one road.</p>" + links_list(fmt_links)),
        ("pricing", "04 / BEFORE YOU ASK", "What decides a billboard's price?", "<p>Size, position, which way it faces, how long you book it and how much demand there is that month. Printing and installation are separate lines. Because the market moves, we confirm rates live instead of printing a list that goes stale.</p>" + links_list([("/guides/billboard-advertising-cost-bangladesh/", "Read the full pricing guide"), ("/guides/how-to-book-a-billboard-in-dhaka/", "How booking works, step by step")])),
    ]
    faqs = [
        ("How many billboard locations does Dhaka AD have in Dhaka?", f"{len(SITES)} static, expressway, tri-vision, neon, mid-island and wall billboard positions across 10 Dhaka areas, plus 56 LED screens in Dhaka and nine other cities.", ("/locations/", "See LED screens too")),
        ("Which is the biggest billboard in Dhaka on your list?", "Gulistan Ramna Bhaban, with two wall faces totalling about 9,500 sq ft. Jolshiri Bus Stand on Purbachal 300 Feet (two 100 × 30 ft faces) and Amin Bazar (two 90 × 30 ft faces) follow.", ("/static-billboards/motijheel-old-dhaka/gulistan-ramna-bhaban/", "See Gulistan Ramna Bhaban")),
        ("Can I book a billboard for less than a year?", "Most static boards are booked by the year, but shorter terms are often possible depending on the site and season. Tell us your dates and we will tell you which placements can do it.", ("/guides/how-to-book-a-billboard-in-dhaka/", "How booking works")),
        ("How fast can my billboard go live?", "Once the work order and artwork are approved, a printed board typically goes up within days. Approved artwork is needed about 72 hours before installation.", ("/large-format-printing/", "Printing and installation")),
    ]
    write(path, page(path, title, desc, site_img(SITES[7]), [{"@type": "ItemList", "name": "Billboard locations in Dhaka", "numberOfItems": len(SITES),
                                                                "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": abs_url(site_path(s)), "name": s[2]} for i, s in enumerate(SITES)]}],
                     crumbs, "DHAKA AD / BILLBOARD LOCATIONS", f"Billboard advertising in Dhaka: {len(SITES)} locations", intro, site_img(SITES[7]),
                     "Elevated Expressway billboard at Chairman Bari, Banani", sections, faqs, qa=qa,
                     closing=("Found a board you like?", "Call and name it. You will know in minutes if it is free for your dates, what it costs this month and what the best nearby alternative is.")))


def build():
    build_sites()
    build_zones()
    build_hub()
