"""Homepage: a story told in the order a buyer thinks. Question -> problem -> proof -> choice -> plan -> call."""
import json

from common import (BASE, PHONE, PHONE_INTL, PHONE_SHOW, abs_url, call_button, call_rail, e, faq_schema, footer, head, header, img, url, write)
from data_static import SITES, ZONES

F = lambda s: f"/assets/field/{s}-1600.webp"  # noqa: E731
B = lambda s: f"/assets/billboards/{s}-1200.webp"  # noqa: E731

FINDER = [
    ("gulshan", "Gulshan, Banani & Mohakhali", 15, 4, "Corporate decision-makers, premium shoppers and airport traffic.",
     [("/locations/gulshan/", "10 LED screens in Gulshan"), ("/locations/mohakhali/", "SKS Tower & Mohakhali screens"), ("/static-billboards/gulshan-banani-mohakhali/", "Expressway & Banani billboards")]),
    ("dhanmondi", "Dhanmondi & New Market", 6, 4, "Students, families and shoppers ready to buy.",
     [("/locations/dhanmondi/", "6 LED screens incl. Science Lab"), ("/static-billboards/dhanmondi-new-market/", "New Market & Shimanto billboards")]),
    ("farmgate", "Farmgate, Karwan Bazar & Shahbagh", 4, 3, "Cross-city commuters, offices, university and hospital traffic.",
     [("/locations/farmgate/", "Bijoy Sarani LED screens"), ("/locations/karwan-bazar/", "Karwan Bazar screens"), ("/static-billboards/farmgate-shahbagh/", "Tri-vision & Bijoy Sarani billboards")]),
    ("mirpur", "Mirpur & Agargaon", 4, 4, "Dense residential families and metro passengers.",
     [("/locations/mirpur/", "Mirpur-10 & Mirpur-1 LED screens"), ("/static-billboards/mirpur/", "Mirpur billboards & 50-panel median run")]),
    ("oldDhaka", "Motijheel, Old Dhaka & Sadarghat", 3, 8, "Traders, bankers and launch passengers from the south.",
     [("/static-billboards/motijheel-old-dhaka/", "Gulistan giant walls & Sadarghat neon"), ("/locations/kamlapur/", "Kamlapur station screens")]),
    ("east", "Badda, Purbachal & Tejgaon", 2, 7, "New-town homeowners, property buyers and Gulshan–Badda commuters.",
     [("/static-billboards/badda-purbachal/", "Purbachal 300 Feet billboards"), ("/locations/tejgaon/", "Hatirjheel & Tejgaon screens")]),
    ("travel", "Airport, stations & expressways", 5, 4, "Travellers at the moment they arrive or depart.",
     [("/airport-domestic-arrival-advertising/", "Airport domestic arrivals sign"), ("/locations/airport/", "Airport entrance & station screens"), ("/expressway-billboard-advertising/", "Expressway billboards")]),
    ("outskirts", "Keraniganj, Savar & Ashulia", 0, 11, "Highway travellers and the industrial workforce.",
     [("/static-billboards/keraniganj/", "Padma Bridge expressway faces"), ("/static-billboards/savar-ashulia/", "Amin Bazar & Ashulia billboards")]),
    ("national", "Outside Dhaka", 20, 0, "Chattogram, Sylhet, Cox's Bazar, Rajshahi and 5 more cities.",
     [("/locations/sylhet/", "8 LED screens in Sylhet"), ("/locations/coxs-bazar/", "Cox's Bazar beach screens"), ("/locations/chattogram/", "Chattogram screens")]),
]

FORMATS = [
    ("/led-billboard-advertising/", F("gulshan-circle-led-cluster"), "LED billboards", "56 screens in 10 cities. Buy minutes, not months."),
    ("/static-billboards/", F("multi-format-building-advertising"), "Static billboards", f"{len(SITES)} faces across Dhaka, from 200 to 9,500 sq ft."),
    ("/expressway-billboard-advertising/", F("expressway-static-billboards"), "Expressway billboards", "Elevated Expressway, 300 Feet and the Padma road."),
    ("/neon-sign-advertising/", F("store-signage-night"), "Tri-vision & neon", "Movement by day, light by night."),
    ("/metro-rail-led-advertising/", F("metro-coach-screens"), "Metro train screens", "840 in-coach screens, ≈550,000 riders a day."),
    ("/airport-advertising/", F("airport-terminal-led-screen"), "Airport advertising", "Meet travellers at arrivals and the terminal."),
    ("/mid-island-branding/", "/assets/outdoor/mirpur-reflective-mid-island.webp", "Mid-island & reflective", "Your message, repeated every few metres."),
    ("/event-management/", F("concert-stage-crowd"), "Events & LED walls", "Stage, screens, light, sound and live cameras."),
    ("/store-opening-activation/", F("ribbon-cutting-opening"), "Store openings", "Open with a crowd, not a quiet shutter."),
    ("/newspaper-insert-advertising/", F("newspaper-insert-leaflet"), "Newspaper inserts", "Your leaflet inside the morning paper."),
    ("/large-format-printing/", F("large-format-printing"), "Printing & banners", "Printed today, installed overnight."),
    ("/outdoor-led-display-installation/", F("led-cabinet-panel"), "LED screen installation", "Own a P4 or P5 screen, with structure and warranty."),
]

PROOF = [
    (F("night-street-led-dhaka"), "LED screen above a packed Dhaka street at night"),
    (F("airport-terminal-led-arrivals"), "LED screen at Hazrat Shahjalal airport terminal"),
    (F("tower-facade-led-rain"), "LED screens on a tower façade in the rain"),
    (F("stage-led-wall-live"), "Live band stage with LED wall"),
    (F("opening-day-crowd"), "Opening-day crowd at a branded backdrop"),
    (F("police-plaza-led-night"), "Police Plaza LED screen at night"),
    (F("expressway-static-billboards"), "Billboards along the elevated expressway"),
    (F("newspaper-insert-handling"), "Leaflets being inserted into newspapers"),
    (F("waterfront-stage-night"), "Waterfront stage reflected at night"),
]

FAQ_GROUPS = [
    ("Start here", [
        ("What does a 360° outdoor advertising agency do?", "It plans, books, produces and proves every outdoor format through one team: LED and static billboards, expressway, tri-vision and neon boards, metro and airport advertising, median branding, vehicle branding, events, activations, newspaper inserts, printing and digital support. You brief once and get one plan, one quotation and one point of contact.", ("/services/", "See every service")),
        ("Which advertising agency in Dhaka handles billboards, LED screens and events together?", "Dhaka AD does. We plan 44 billboard positions across Dhaka, 56 LED screens in 10 cities, metro and airport advertising, and we build events, activations and print, so a whole campaign runs through one team.", ("/about/", "About Dhaka AD")),
        ("What happens on the first call?", "We ask three things: who you want to reach, where, and when. Then we tell you which placements are free, what they cost this month and what we would combine. You get a written shortlist and quotation, usually the same day.", ("/contact/", "Prepare your call")),
        ("Is there a minimum budget?", "No fixed minimum. A campaign can start with a single LED screen for a few days or one billboard on the right road. Tell us your budget and we will show you the strongest option within it.", ("/campaign-planning/", "Campaign planning")),
    ]),
    ("Costs & rates", [
        ("How much does billboard advertising cost in Bangladesh?", "It depends on the format. Static billboards are usually rented by the year, priced by position and size. LED billboards are sold per minute of daily airtime. Metro screens are priced per minute for 30 days. Printing, installation, VAT and AIT are usually extra. Call for today's rates on specific sites.", ("/guides/billboard-advertising-cost-bangladesh/", "Read the pricing guide")),
        ("How is LED billboard advertising priced?", "As airtime: a cost per minute per screen, for a minimum number of minutes per day (often 60), across the dates you book. Premium junctions cost more per minute.", ("/led-billboard-advertising/", "LED billboards")),
        ("Why don't you publish a price list?", "Because rates and availability change every week. A printed list would be wrong by the time you read it. A two-minute call gives you this week's real numbers for the exact sites you want.", None),
        ("Are VAT, printing and installation included?", "Our quotations show media, printing, installation and taxes as separate lines, so you see every cost before you approve anything.", ("/guides/how-to-book-a-billboard-in-dhaka/", "How booking works")),
    ]),
    ("Billboards", [
        ("How many billboard locations can I choose from in Dhaka?", f"{len(SITES)} billboard positions across 10 Dhaka areas, plus 56 LED screens in Dhaka and nine other cities. Every location has its own page with a photograph, size and facing.", ("/static-billboards/", "Browse billboard locations")),
        ("Where are the best billboard locations in Dhaka?", "Where your customers travel. Corporate audiences: Gulshan, Banani and the Elevated Expressway. Students: Dhanmondi and Shahbagh. Families: Mirpur and Malibagh. Traders: Gulistan and Old Dhaka. Travellers: the airport, stations, Sadarghat and the Padma Bridge expressway.", ("/guides/best-billboard-locations-in-dhaka/", "Best locations by audience")),
        ("Can I advertise on the Dhaka Elevated Expressway?", "Yes. We offer faces at the Chairman Bari crossing (125' × 40', lit) and near Banani–Kakoli, plus Purbachal 300 Feet and the Dhaka–Mawa–Bhanga expressway.", ("/expressway-billboard-advertising/", "Expressway billboards")),
        ("What is the biggest billboard you offer?", "Gulistan Ramna Bhaban, with two wall faces totalling about 9,500 sq ft. Jolshiri Bus Stand (two 100' × 30' faces) and Amin Bazar (two 90' × 30' faces) follow.", ("/static-billboards/motijheel-old-dhaka/", "Motijheel & Old Dhaka")),
    ]),
    ("LED screens", [
        ("Where are your LED billboard screens?", "56 screens: Gulshan, Banani, Mohakhali, Dhanmondi, Science Lab, Farmgate, Karwan Bazar, Tejgaon, Mirpur, Agargaon, the airport, Kamlapur and Sadarghat in Dhaka, plus Chattogram, Cox's Bazar, Sylhet, Rajshahi, Cumilla, Rangpur, Bogura, Narayanganj and Feni.", ("/locations/", "LED screens by city")),
        ("What file do I need for an LED billboard?", "Usually an MP4 at 1920 × 1080, though portrait and smaller screens exist. We confirm the exact resolution for each screen before you export.", ("/guides/led-billboard-artwork-specifications/", "Artwork specifications")),
        ("How do I know my LED ad actually played?", "You receive a log summary showing when your advert ran on each screen.", ("/our-work/", "Reporting & proof")),
        ("Can you install a permanent LED screen for my building?", "Yes. We supply and install P4 and P5 outdoor LED displays with steel structure, controller and a one-year warranty, typically within about 30 days.", ("/outdoor-led-display-installation/", "LED installation")),
    ]),
    ("Metro & airport", [
        ("Can I advertise inside Dhaka Metro Rail trains?", "Yes. In-coach screens run across 840 screens on around 14 trains and 84 coaches, about 16 hours a day, reaching roughly 550,000 commuters daily. Campaigns usually run for 30 days.", ("/metro-rail-led-advertising/", "Metro train screens")),
        ("How early must metro content be submitted?", "Approved content is needed about five days before the airing date.", ("/guides/led-billboard-artwork-specifications/", "File deadlines")),
        ("Can I advertise at Dhaka airport?", "Yes. An LED sign in the domestic arrivals luggage-belt area at Hazrat Shahjalal International Airport runs 7am to 11pm and is rented by the year. Airport entrance and railway station screens are also available.", ("/airport-domestic-arrival-advertising/", "Airport arrivals sign")),
    ]),
    ("Events & activation", [
        ("Do you manage events in Dhaka?", "Yes: stage and truss, LED walls, lighting, sound, live cameras and the control desk, for corporate nights, concerts, launches and celebrations.", ("/event-management/", "Event management")),
        ("Can I rent an LED wall for one day?", "Yes. We supply the wall, support structure, processor and an operator for the event.", ("/led-screen-rental/", "LED screen rental")),
        ("Can you launch a new store or branch?", "Yes. Street banners and newspaper inserts before the day, a branded backdrop and ribbon-cutting on the day, signage and billboards after.", ("/store-opening-activation/", "Store opening activation")),
        ("Do you do newspaper insert advertising?", "Yes. We print your leaflet and insert it into morning newspapers delivered in the areas you choose.", ("/newspaper-insert-advertising/", "Newspaper inserts")),
    ]),
    ("Booking & proof", [
        ("How do I book a billboard in Dhaka?", "Share your audience, area and dates; pick from a shortlist with photos; approve a quotation and mock-up; send artwork about 72 hours before installation; receive installation photos.", ("/guides/how-to-book-a-billboard-in-dhaka/", "The 7 steps")),
        ("How fast can my campaign go live?", "LED campaigns can start within days of approval. Printed boards usually go up within days once artwork is approved. Peak seasons fill early, so call as soon as you have a date.", None),
        ("Can I see my ad on the location before paying?", "Yes. Ask for a mock-up of your artwork on the real location photograph before you approve production.", ("/our-work/", "See our work")),
        ("What proof do I receive?", "Installation photographs for printed formats and a log summary for LED screens, plus event photography where relevant.", None),
    ]),
    ("Digital & AI search", [
        ("Can outdoor and digital advertising work together?", "Yes. Outdoor builds awareness on the street; search, social and your website catch the people it made curious. We plan both with the same message.", ("/digital-marketing/", "Digital marketing")),
        ("Can an agency guarantee a Google AI Overview or ChatGPT mention?", "No one can guarantee it. Search and AI platforms choose their own answers. Clear, accurate, well-structured information about your business is what gives you the best chance.", ("/digital-marketing/", "Search & content")),
    ]),
]


def hero():
    return f'''<section class="portal" id="home" aria-label="Dhaka AD outdoor advertising">
<div class="portal-stage">
{img("/assets/outdoor/dhaka-city-user-hero.webp", "Dhaka street intersection with LED billboards and city traffic", cls="portal-photo", lazy=False, priority=True)}
<div class="photo-tone" aria-hidden="true"></div><div class="photo-veil" aria-hidden="true"></div>
<div class="shutter shutter-left" aria-hidden="true"><span class="panel-grid"></span></div><div class="shutter shutter-right" aria-hidden="true"><span class="panel-grid"></span></div>
<div class="hero-question"><p class="eyebrow">360° OUTDOOR ADVERTISING AGENCY IN DHAKA, BANGLADESH</p>
<h1>How many customers passed your business today <em>without ever seeing your name?</em></h1>
<p class="question-lede">Billboards, LED screens, metro, airport, events and print. Planned, booked and proved by one team, on one call.</p></div>
<div class="portal-top micro"><span><i class="dot amber"></i> {len(SITES)} billboards · 56 LED screens · 10 cities</span><span class="hero-edition">DHAKA, BANGLADESH <span class="local-time"></span></span></div>
<div class="portal-title" aria-hidden="true"><span class="title-left">DHAKA</span><span class="title-right">AD<span class="title-period">.</span></span></div>
<div class="portal-intro"><div>{call_button("Call " + PHONE_SHOW + " for a free shortlist", "hero-call")}<p class="hero-call-note">Free shortlist · This week's rates · No obligation</p></div><a class="text-link" href="#problem">Why most ads go unseen <span>↓</span></a></div>
<div class="portal-scene" aria-hidden="true"><p class="micro">THE RIGHT ROAD. THE RIGHT SIDE. THE RIGHT SIZE.</p><h2>BE THE NAME<br>THEY REMEMBER.</h2><a class="text-link" href="tel:{PHONE}" tabindex="-1" data-call>Call {PHONE_SHOW} <span>↗</span></a></div>
<span class="traveller traveller-amber" aria-hidden="true"></span><span class="traveller traveller-teal" aria-hidden="true"></span>
<div class="portal-bottom"><a class="scroll-cue" href="#problem"><span class="scroll-icon" aria-hidden="true">↓</span><span class="micro">SCROLL. SEE WHERE YOU COULD BE.</span></a><span class="micro portal-caption">STRATEGY → PLACEMENT → PROOF<br><span>Dhaka, Bangladesh · Field photography</span></span><span class="micro story-cue">ONE CALL. EVERY FORMAT.</span></div>
<div class="hero-progress" aria-hidden="true"><span></span></div>
</div></section>'''


def problem():
    cards = [("01", "The wrong side of the road", "A great board facing away from your customers is just expensive scenery. Direction, height and the speed of traffic decide whether anyone reads it."),
             ("02", "Ten suppliers, ten excuses", "Site owner, printer, installer, screen operator, event crew. When something slips at 8pm, nobody owns it but you."),
             ("03", "Paid, but did it run?", "No photographs, no screen log, no proof. You are left hoping your money was well spent.")]
    c = "".join(f'<article class="pain-card reveal"><span class="micro amber-text">{n}</span><h3>{t}</h3><p>{p}</p></article>' for n, t, p in cards)
    return (f'<section class="pain section-pad" id="problem"><div class="section-heading"><p class="eyebrow"><span>01 / THE PROBLEM</span> <i class="dot amber"></i></p><span class="micro">WHY MOST OUTDOOR ADS DISAPPEAR</span></div>'
            f'<div class="pain-head reveal"><h2>Dhaka sees thousands of ads a day.<br><em>It remembers a handful.</em></h2><p>Your customer\'s commute is a wall of noise: shop signs, banners, screens and traffic. Most brands pay to become part of that wall. A few are placed where the eye actually lands, on the right road, facing the right way, at the right size. That difference is not luck. It is planning.</p></div>'
            f'<div class="pain-grid">{c}</div><p class="pain-bridge reveal">There is a simpler way: <strong>one team, one number, proof at every step.</strong> <a class="text-link" href="#proof">See the network <span>↓</span></a></p></section>')


def stats():
    items = [("56", "", "LED screens in 10 cities"), (str(len(SITES)), "", "billboard faces across Dhaka"), ("840", "", "in-coach metro screens"),
             ("550", "K", "daily metro commuters (approx.)"), ("9,500", "", "sq ft: our largest single site"), ("1", "", "call to plan all of it")]
    s = "".join(f'<div class="stat reveal"><strong><span data-count="{n.replace(",", "")}">{n}</span>{suf}</strong><span>{e(lbl)}</span></div>' for n, suf, lbl in items)
    return (f'<section class="stats section-pad" id="proof" aria-label="Dhaka AD network in numbers"><p class="eyebrow"><span>02 / THE NETWORK</span> <i class="dot teal"></i></p>'
            f'<h2 class="reveal">Big enough to cover the country.<br><em>Small enough to answer the phone.</em></h2><div class="stat-grid">{s}</div>'
            f'<p class="small-note">Network figures from current Dhaka AD placement and media proposals. Availability is confirmed for your dates.</p></section>')


def bab():
    before = ["Weeks chasing site owners and printers", "Guessing from old, blurry photographs", "Separate quotes that never add up", "Hoping the ad actually ran"]
    after = ["A shortlist of free placements in one call", "Your artwork mocked up on the real location", "One quotation, every cost on its own line", "Installation photos or a screen log as proof"]
    li = lambda xs, cls: "".join(f'<li class="{cls}">{e(x)}</li>' for x in xs)  # noqa: E731
    return (f'<section class="bab section-pad"><p class="eyebrow"><span>03 / BEFORE &amp; AFTER</span> <i class="dot amber"></i></p><h2 class="reveal">Same budget.<br><em>A completely different result.</em></h2>'
            f'<div class="bab-grid"><div class="bab-col bab-before reveal"><p class="micro">BEFORE: DOING IT ALONE</p><ul>{li(before, "x")}</ul></div>'
            f'<div class="bab-col bab-after reveal"><p class="micro">AFTER: ONE CALL TO DHAKA AD</p><ul>{li(after, "ok")}</ul></div></div>'
            f'<div class="bab-bridge reveal"><p><strong>The bridge between the two is a two-minute phone call.</strong> You stay in control of every decision. We do the chasing.</p>{call_button("Call " + PHONE_SHOW)}</div></section>')


def finder():
    data = {k: {"name": n, "led": led, "boards": b, "who": who, "links": [[url(p), t] for p, t in links]} for k, n, led, b, who, links in FINDER}
    chips = "".join(f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}" data-area="{k}">{e(n)}</button>' for i, (k, n, *_r) in enumerate(FINDER))
    first = FINDER[0]
    links = "".join(f'<a href="{url(p)}"><span>{e(t)}</span><span aria-hidden="true">↗</span></a>' for p, t in first[5])
    return (f'<section class="finder section-pad" id="finder"><div class="section-heading"><p class="eyebrow"><span>04 / YOUR MOVE</span> <i class="dot teal"></i></p><span class="micro">TAP AN AREA. SEE WHAT IS THERE.</span></div>'
            f'<div class="finder-layout"><div><h2 class="reveal">Where do your<br><em>customers move?</em></h2><p class="finder-lede">Pick the part of the country that matters to you. You will see what we can put there, right now.</p>'
            f'<div class="finder-chips" role="group" aria-label="Choose an area">{chips}</div></div>'
            f'<div class="finder-result" aria-live="polite"><p class="micro amber-text">IN THIS AREA</p><h3 data-f="name">{e(first[1])}</h3><p data-f="who">{e(first[4])}</p>'
            f'<div class="finder-counts"><div><strong data-f="led">{first[2]}</strong><span>LED screens</span></div><div><strong data-f="boards">{first[3]}</strong><span>billboard faces</span></div></div>'
            f'<div class="directory-links" data-f="links">{links}</div>'
            f'<a class="button call-button finder-call" href="tel:{PHONE}" data-call>Check this area\'s availability · {PHONE_SHOW} <span aria-hidden="true">↗</span></a></div></div>'
            f'<script type="application/json" id="finder-data">{json.dumps(data)}</script></section>')


def formats():
    cards = "".join(
        f'<a class="fmt-card reveal" href="{url(p)}">{img(i, t, sizes="(max-width:760px) 100vw, 25vw")}<span class="fmt-copy"><strong>{e(t)}</strong><span>{e(d)}</span></span><span class="fmt-arrow" aria-hidden="true">↗</span></a>'
        for p, i, t, d in FORMATS)
    return (f'<section class="formats360 section-pad" id="services"><div class="section-heading"><p class="eyebrow"><span>05 / 360° SERVICE</span> <i class="dot amber"></i></p><span class="micro">EVERYTHING OUTDOOR. ONE NUMBER.</span></div>'
            f'<div class="services-head reveal"><h2>Every format your customer passes.<br><span class="muted">One team that runs them all.</span></h2><p>Mix them, or start with one.<br>Everything is planned, produced and proved in-house.</p></div>'
            f'<div class="fmt-grid">{cards}</div>'
            '<div class="all-services"><p class="eyebrow">FIND EVERYTHING IN ONE PLACE</p><div class="directory-links">'
            + "".join(f'<a href="{url(p)}"><span>{t}</span><span aria-hidden="true">↗</span></a>' for p, t in [
                ("/billboard-advertising/", "Billboard advertising in Dhaka"), ("/led-billboard-advertising/", "LED billboard advertising"), ("/metro-rail-advertising/", "Metro rail advertising"),
                ("/airport-advertising/", "Airport advertising"), ("/neon-sign-advertising/", "Neon sign billboards"), ("/light-box-advertising/", "Light box advertising"),
                ("/bus-branding/", "Bus branding"), ("/car-branding/", "Car and fleet branding"), ("/brand-activation/", "Brand activation"), ("/led-screen-rental/", "LED screen rental"),
                ("/print-and-media/", "Print and media buying"), ("/digital-marketing/", "Digital marketing"), ("/industries/", "Plans by industry"), ("/outdoor-advertising/", "The outdoor formats guide")])
            + "</div></div></section>")


def deck():
    cards = [("Gulshan Circle", "LED / URBAN INTERSECTION", "/assets/work-led-billboards-gulshan-intersection-1200.webp", "LED advertising screens at a busy Gulshan intersection", "DHAKA / LED ADVERTISING", "Gulshan<br>Circle."),
             ("Airport terminal", "LED / HAZRAT SHAHJALAL", F("airport-terminal-led-screen"), "LED screen above the Hazrat Shahjalal airport terminal entrance", "AIRPORT / TRANSIT", "First<br>impressions."),
             ("Elevated Expressway", "STATIC / 125' × 40'", B("elevated-expressway-chairman-bari-banani"), "Elevated Expressway billboard at Chairman Bari", "BANANI / EXPRESSWAY", "Above the<br>everyday."),
             ("Mohakhali / SKS Tower", "LED / FLYOVER VIEW", "/assets/sks-tower-flyover-view-mohakhali-640.webp", "SKS Tower LED screens facing the Mohakhali flyover", "MOHAKHALI / LED", "Seen from<br>the flyover."),
             ("Sadarghat", "NEON / 90' × 30'", B("sadarghat-launch-ghat-neon"), "Neon billboard at Sadarghat launch ghat", "OLD DHAKA / NEON", "Welcome<br>to Dhaka.")]
    arts = "".join(f'<article class="location-card" data-name="{e(n)}" data-category="{e(c)}">{img(s, a)}<div class="card-top micro"><span>DHAKA AD / LOCATION STUDY</span><span>{i + 1:02d}</span></div>'
                   f'<div class="card-caption"><span class="micro">{e(m)}</span><h3>{h}</h3><span class="card-arrow" aria-hidden="true">↗</span></div></article>' for i, (n, c, s, a, m, h) in enumerate(cards))
    dots = "".join(f'<button aria-label="Show {e(n)}" aria-pressed="{"true" if i == 0 else "false"}"></button>' for i, (n, *_r) in enumerate(cards))
    return f'''<section class="locations section-pad" id="locations"><div class="section-heading"><p class="eyebrow"><span>06 / ON THE GROUND</span> <i class="dot amber"></i></p><span class="micro">REAL PLACES YOUR CUSTOMERS PASS</span></div>
<div class="locations-layout"><div class="locations-copy reveal"><h2>Your customer's day.<br><span class="muted">Your brand in it.</span></h2><p>A commute. A flight home. A crossing they wait at every evening. Swipe through a few of the places your message could live, then open the full directory.</p><p class="small-note">Original location photography. Availability confirmed for your dates.</p>
<div class="button-row">{call_button("Call about a placement")}<a class="text-link" href="{url('/static-billboards/')}">All {len(SITES)} billboards <span>↗</span></a><a class="text-link" href="{url('/locations/')}">All 56 LED screens <span>↗</span></a></div>
<div class="deck-readout"><span class="micro amber-text">IN FOCUS <span id="deck-count">01 / {len(cards):02d}</span></span><h3 id="deck-name">{cards[0][0]}</h3><p id="deck-category" class="micro">{cards[0][1]}</p></div></div>
<div class="deck-side"><div class="deck" tabindex="0" role="region" aria-label="Advertising location deck. Use left and right arrow keys to explore.">{arts}</div>
<div class="deck-controls"><span class="micro deck-hint">DRAG A CARD. DISCOVER A PLACE.</span><div class="deck-dots" role="group" aria-label="Choose a location">{dots}</div><div class="deck-arrows"><button id="deck-prev" aria-label="Previous location">←</button><button id="deck-next" aria-label="Next location">→</button></div></div><p id="deck-status" class="sr-only" aria-live="polite">Location 1 of {len(cards)}: {cards[0][0]}</p></div></div></section>'''


def proof():
    figs = "".join(f'<figure class="mosaic-{i} reveal">{img(s, a, sizes="(max-width:760px) 100vw, 33vw")}<figcaption>{e(a)}</figcaption></figure>' for i, (s, a) in enumerate(PROOF))
    return (f'<section class="field-proof section-pad" id="work"><div class="section-heading"><p class="eyebrow"><span>07 / THE PROOF</span> <i class="dot teal"></i></p><span class="micro">OUR CREWS. OUR PHOTOGRAPHS.</span></div>'
            f'<div class="outdoor-heading"><h2 class="reveal">Don\'t take our word for it.<br><em>Look at the street.</em></h2><div><p>Screens we schedule, boards we install, stages we build and openings we run. Every photograph here was taken by our own team on the job.</p>'
            f'<a class="text-link" href="{url("/our-work/")}">See more work <span>↗</span></a></div></div><div class="mosaic">{figs}</div></section>')


def process():
    rows = [("01", "Listen.", "Your audience, goal, areas and dates. Five minutes on the phone.", "A SHARED BRIEF"), ("02", "Shortlist.", "Free placements with photos, sizes, facing and this week's rates.", "A PLAN YOU CAN COMPARE"),
            ("03", "Preview.", "Your artwork mocked up on the real location before you pay for production.", "NO SURPRISES"), ("04", "Go live.", "Printing, installation, scheduling or the full event build.", "YOUR BRAND IN THE CITY"),
            ("05", "Prove it.", "Installation photographs, screen log summaries and event photography.", "EVIDENCE YOU CAN CHECK")]
    r = "".join(f'<div class="process-row" role="row"><h3 role="cell"><span class="micro amber-text">{n}</span> {h}</h3><p role="cell">{p}</p><span role="cell" class="micro">{o}</span></div>' for n, h, p, o in rows)
    return (f'<section class="process section-pad" id="process"><div class="section-heading"><p class="eyebrow"><span>08 / HOW IT HAPPENS</span> <i class="dot amber"></i></p><span class="micro">FROM FIRST CALL TO FINAL PROOF</span></div>'
            f'<div class="process-heading reveal"><h2>You decide.<br><span class="muted">We do the legwork.</span></h2><a class="text-link" href="{url("/guides/how-to-book-a-billboard-in-dhaka/")}">The booking process in detail <span>↗</span></a></div>'
            f'<div class="process-table" role="table" aria-label="Our campaign process"><div class="process-row table-head micro" role="row"><span role="columnheader">THE STEP</span><span role="columnheader">WHAT HAPPENS</span><span role="columnheader">WHAT YOU GET</span></div>{r}</div></section>')


def ratecard():
    rows = [("LED billboard", "Gulshan Circle-1", "Per minute / day"), ("Static billboard", "Elevated Expressway", "12 months"), ("Metro train screens", "840 screens", "30 days"),
            ("Airport arrivals sign", "Hazrat Shahjalal", "12 months"), ("Tri-vision", "Shahbagh", "12 months"), ("LED screen rental", "Your event", "Per day")]
    r = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td><span class="blur" aria-hidden="true">৳ ••,•••</span><span class="sr-only">Rate given on request</span></td></tr>' for a, b, c in rows)
    return (f'<section class="ratecard section-pad" id="rates"><div class="ratecard-layout"><div><p class="eyebrow"><span>09 / THE RATE CARD</span> <i class="dot amber"></i></p><h2 class="reveal">Rates change every week.<br><em>Get this week\'s on a call.</em></h2>'
            f'<p>We do not publish prices because they would be wrong by next Friday. Seasons, demand and open dates move them constantly. Call and you get the real number for the real site, plus what is worth pairing it with.</p>'
            f'<a class="text-link" href="{url("/guides/billboard-advertising-cost-bangladesh/")}">What decides the price? <span>↗</span></a></div>'
            f'<div class="ratecard-box"><div class="table-scroll"><table><thead><tr><th scope="col">Format</th><th scope="col">Example</th><th scope="col">Term</th><th scope="col">This week</th></tr></thead><tbody>{r}</tbody></table></div>'
            f'<div class="ratecard-unlock">{call_button("Unlock today’s rates · " + PHONE_SHOW)}<span class="micro">TWO MINUTES · NO OBLIGATION</span></div></div></div></section>')


def guides():
    g = [("/guides/billboard-advertising-cost-bangladesh/", F("gulshan-circle-led-cluster"), "How much does billboard advertising cost in Bangladesh?"),
         ("/guides/led-vs-static-billboard/", F("tower-facade-led-rain"), "LED billboard vs static billboard: which should you choose?"),
         ("/guides/best-billboard-locations-in-dhaka/", F("gulshan-intersection-wide"), "The best billboard locations in Dhaka, by audience")]
    c = "".join(f'<a class="guide-card reveal" href="{url(p)}">{img(i, t, sizes="(max-width:760px) 100vw, 33vw")}<span class="micro amber-text">GUIDE</span><strong>{e(t)}</strong><span class="text-link">Read <span aria-hidden="true">↗</span></span></a>' for p, i, t in g)
    return (f'<section class="guides-teaser section-pad"><div class="section-heading"><p class="eyebrow"><span>10 / BEFORE YOU DECIDE</span> <i class="dot teal"></i></p><span class="micro">SHARPER QUESTIONS, BETTER CAMPAIGNS</span></div>'
            f'<div class="services-head reveal"><h2>Read for five minutes.<br><span class="muted">Ask like a media buyer.</span></h2><a class="text-link" href="{url("/guides/")}">All guides <span>↗</span></a></div><div class="guide-grid">{c}</div></section>')


def faq():
    tabs = '<button aria-pressed="true" data-faq-filter="all">All questions</button>' + "".join(f'<button aria-pressed="false" data-faq-filter="{i}">{e(n)}</button>' for i, (n, _) in enumerate(FAQ_GROUPS))
    groups = ""
    for i, (name, items) in enumerate(FAQ_GROUPS):
        its = ""
        for q, a, link in items:
            nxt = f'<a class="text-link" href="{url(link[0])}">{e(link[1])} <span aria-hidden="true">↗</span></a>' if link else ""
            its += (f'<details class="faq-item"><summary><span>{e(q)}</span><i aria-hidden="true">+</i></summary><div class="faq-answer"><p>{e(a)}</p>'
                    f'<div class="faq-next">{nxt}<a class="faq-call" href="tel:{PHONE}" data-call>Your dates change the answer. Ask us · {PHONE_SHOW} ↗</a></div></div></details>')
        groups += f'<div class="faq-group" data-faq-group="{i}"><section class="faq-block" id="home-{i}"><p class="eyebrow">{len(items)} QUESTIONS</p><h2>{e(name)}</h2>{its}</section></div>'
    return (f'<section class="home-faq section-pad" id="faqs"><p class="eyebrow">11 / YOUR QUESTIONS, ANSWERED STRAIGHT</p><h2>Know more.<br><em>Decide with confidence.</em></h2>'
            f'<p class="faq-intro">The practical answers first. Search, or pick a topic. When an answer depends on your dates or budget, the fastest route is a short call.</p>'
            f'<div class="faq-tools"><label class="faq-search"><span class="sr-only">Search the questions</span><input type="search" placeholder="Search: price, metro, airport, LED file, events…" autocomplete="off" data-faq-search></label>'
            f'<span class="micro faq-count" data-faq-count aria-live="polite">{sum(len(x[1]) for x in FAQ_GROUPS)} answers</span></div>'
            f'<div class="faq-filters" role="group" aria-label="Choose a question topic">{tabs}</div>{groups}'
            f'<div class="faq-empty" hidden><p>No written answer for that yet. Ask us directly: it takes a minute.</p>{call_button("Call " + PHONE_SHOW)}</div>'
            f'<a class="text-link" href="{url("/advertising-faq/")}">Explore every advertising question <span>↗</span></a></section>')


def close():
    return (f'<section class="close" id="contact"><div class="section-pad close-inner"><div class="section-heading"><p class="eyebrow"><span>12 / YOUR NEXT MOVE</span> <i class="dot teal"></i></p><span class="micro">DHAKA AD / LET\'S MAKE A MARK.</span></div>'
            f'<div class="close-content reveal"><h2>Your customers passed by today.<br><em>Tomorrow, let them see you.</em></h2><div><p>Your audience. Your area. Your dates.<br>Three answers. One call. A real plan by tonight.</p>'
            f'<div class="button-row">{call_button("Call " + PHONE_INTL)}<a class="text-link" href="https://wa.me/8801840860284" rel="noopener">Or WhatsApp us <span>↗</span></a></div></div></div></div>'
            f'<div class="end-wordmark" aria-hidden="true">DHAKA AD<span>.</span></div></section>')


def build():
    path = "/"
    title = "Outdoor Advertising Agency in Dhaka, Bangladesh | Billboards & LED | Dhaka AD"
    desc = f"360° outdoor advertising agency in Dhaka: {len(SITES)} billboards, 56 LED screens in 10 cities, metro, airport, expressway, events and print. One call, free shortlist: {PHONE_SHOW}."
    all_faqs = [(q, a) for _, items in FAQ_GROUPS for q, a, _l in items]
    graph = [{"@type": "WebSite", "@id": abs_url("/#website"), "name": "Dhaka AD", "url": abs_url("/"), "inLanguage": "en-GB", "publisher": {"@id": abs_url("/#organization")}},
             {"@type": "WebPage", "@id": abs_url("/#page"), "url": abs_url("/"), "name": title, "description": desc, "isPartOf": {"@id": abs_url("/#website")}, "about": {"@id": abs_url("/#organization")},
              "primaryImageOfPage": {"@type": "ImageObject", "url": abs_url("/assets/outdoor/dhaka-city-user-hero.webp")}, "dateModified": "2026-10-16"},
             {"@type": "OfferCatalog", "name": "Outdoor advertising services in Bangladesh", "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "url": abs_url(p), "provider": {"@id": abs_url("/#organization")}}} for p, _i, t, _d in FORMATS]},
             faq_schema(all_faqs)]
    preload = f'<link rel="preload" href="{BASE}/assets/syne-800.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="{BASE}/assets/outdoor/dhaka-city-user-hero.webp" as="image">'
    html = (head(title, desc, path, "/assets/outdoor/dhaka-city-user-hero.webp", graph, preload).replace(f'<script src="{BASE}/content.js', f'<script src="{BASE}/app.js?v=growth-1" defer></script><script src="{BASE}/content.js')
            + '<body class="home">' + header() + '<main id="main">' + hero() + problem() + stats() + bab() + finder() + formats() + deck() + proof() + process() + ratecard() + guides() + faq() + close()
            + "</main>" + footer() + call_rail()
            + '<div class="call-nudge" role="dialog" aria-live="polite" aria-label="Talk to a planner" hidden><button class="nudge-close" aria-label="Dismiss">×</button><p class="micro amber-text">YOU\'RE CLEARLY PLANNING SOMETHING</p>'
            + f'<p><strong>Most of these answers depend on your dates.</strong> Get yours in two minutes.</p>{call_button("Call " + PHONE_SHOW)}</div>'
            + '<noscript><style>.deck{display:flex;gap:20px;overflow-x:auto;aspect-ratio:auto}.location-card{position:relative;flex:0 0 90%;aspect-ratio:1}.deck-controls{display:none}.portal-scene a{pointer-events:auto}</style></noscript></body></html>')
    write(path, html)
