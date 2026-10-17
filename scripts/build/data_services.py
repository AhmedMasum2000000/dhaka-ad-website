"""New service pages. Copy follows PAS / AIDA: name the problem, sharpen it, show the way out, ask for the call."""
from common import PHONE_SHOW, links_list, quick_answer


def P(*paras):
    return "".join(f"<p>{p}</p>" for p in paras)


def UL(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def OL(items):
    return "<ol class='steps'>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def F(slug):
    return f"/assets/field/{slug}-1600.webp"


def B(slug):
    return f"/assets/billboards/{slug}-1200.webp"


SERVICES = [
    dict(
        path="/expressway-billboard-advertising/", fmt="EXPRESSWAY BILLBOARDS",
        title="Expressway billboard advertising in Dhaka | Dhaka AD",
        desc=f"Billboards beside the Dhaka Elevated Expressway, Purbachal 300 Feet and the Dhaka–Mawa–Bhanga expressway. Giant faces, photos and sizes. Call {PHONE_SHOW}.",
        h1="Expressway billboard advertising in Dhaka",
        intro=P("<strong>The fastest-growing roads in Bangladesh are also the hardest to ignore.</strong> Every car on the Elevated Expressway, every bus heading for the Padma Bridge, every buyer driving out to Purbachal passes the same handful of giant faces.",
                "Put your brand on one of them and you are seen at a scale ordinary street boards cannot match: 125-foot lit faces, 100-foot double-sided boards, both directions of the Dhaka–Bhanga road. We shortlist the right face, print it, install it and send you the proof."),
        qa=quick_answer("Expressway billboards in Dhaka sit beside the Dhaka Elevated Expressway (Banani, Kakoli), Purbachal 300 Feet (Jolshiri, Kuril, Kanchan Bridge) and the Dhaka–Mawa–Bhanga expressway (Keraniganj). Faces range from 600 to 6,000 sq ft and are usually booked by the year.",
                        [("Corridors", "3"), ("Largest face", "125' × 40'"), ("Typical term", "12 months")]),
        hero=(B("elevated-expressway-chairman-bari-banani"), "Elevated Expressway billboard at Chairman Bari, Banani"),
        sections=[
            ("why", "01 / THE PROBLEM", "Street-level ads get lost in Dhaka's clutter", P("At a busy junction your board competes with shop signs, banners, wires and traffic. On an expressway the view opens up: fewer competing messages, long sight lines and drivers looking ahead, not down.", "That is why the brands that need scale fast, property developers, telecoms, banks, automotive and FMCG launches, fight for expressway faces first.")),
            ("corridors", "02 / WHERE", "Three expressway corridors, one call", UL(["<strong>Dhaka Elevated Expressway</strong>: Chairman Bari crossing (125' × 40', lit) and Banani–Kakoli (two stacked faces). <a href='/dhaka-ad-website/static-billboards/gulshan-banani-mohakhali/'>See Banani & Mohakhali</a>",
                                                                               "<strong>Purbachal 300 Feet</strong>: Jolshiri Bus Stand (two 100' × 30' faces), Kuril Bishwa Road, Kanchan Bridge and the Jolshiri entry. <a href='/dhaka-ad-website/static-billboards/badda-purbachal/'>See Badda & Purbachal</a>",
                                                                               "<strong>Dhaka–Mawa–Bhanga Expressway</strong>: Abdullahpur and Rajendrapur in Keraniganj, both directions toward the Padma Bridge and Dhaka. <a href='/dhaka-ad-website/static-billboards/keraniganj/'>See Keraniganj</a>"])),
            ("creative", "03 / THE CREATIVE", "Design for 60 km/h", P("Expressway viewers have two or three seconds. Brand big, one striking image, five words or fewer. A phone number rarely survives the speed; a memorable name or web address does.") + UL(["One idea per face, not three.", "High contrast colours that hold up in haze and dusk.", "Ask for a mock-up on the real photograph before printing."])),
            ("how", "04 / THE PROCESS", "From call to installed in days", OL(["Tell us your audience and launch date.", "Get a shortlist of free faces with photographs.", "Approve the quotation: media, printing and installation shown separately.", "Send artwork 72 hours before installation.", "Receive installation photographs as proof."])),
        ],
        faqs=[
            ("Where are the expressway billboards in Dhaka?", "Beside the Dhaka Elevated Expressway at Chairman Bari and Banani–Kakoli, along Purbachal 300 Feet at Jolshiri, Kuril and Kanchan Bridge, and on the Dhaka–Mawa–Bhanga expressway at Abdullahpur and Rajendrapur in Keraniganj.", ("/static-billboards/", "Browse all billboard locations")),
            ("How big are expressway billboards?", "From about 600 sq ft up to 6,000 sq ft. The Chairman Bari face is 125' × 40' and lit; Jolshiri Bus Stand has two 100' × 30' faces.", None),
            ("How much does an expressway billboard cost in Bangladesh?", "Expressway faces are premium positions usually rented by the year, with printing and installation quoted separately. The rate depends on the face, the term and current demand, so we confirm it live on a call.", ("/guides/billboard-advertising-cost-bangladesh/", "How billboard pricing works")),
            ("Are expressway billboards illuminated?", "Some are. The Chairman Bari face is a lit board, and neon faces are available at Hasnabad in Keraniganj. Ask which faces are lit when you call.", ("/neon-sign-advertising/", "Neon and lit boards")),
        ],
        gallery=[(F("expressway-static-billboards"), "Static billboards along the elevated expressway"), (F("expressway-billboard-close"), "Expressway billboard face seen from the deck"), (F("airport-road-led-billboard"), "Large LED billboard on the airport road")],
        related=[("/static-billboards/", "All billboard locations in Dhaka"), ("/billboard-advertising/", "Billboard advertising guide"), ("/led-billboard-advertising/", "LED billboard advertising"), ("/guides/led-vs-static-billboard/", "LED vs static billboard")],
    ),
    dict(
        path="/tri-vision-billboard-advertising/", fmt="TRI-VISION BILLBOARDS",
        title="Tri-vision billboard advertising in Dhaka | Dhaka AD",
        desc=f"Rotating tri-vision billboards at Shahbagh, Paribagh and Motijheel. Three faces, movement that catches the eye. Photos, sizes and booking. Call {PHONE_SHOW}.",
        h1="Tri-vision billboard advertising in Dhaka",
        intro=P("<strong>Still billboards blur into the background. Moving ones do not.</strong> A tri-vision board turns on its own, flipping between three printed faces, and that small movement is enough to pull every eye at the crossing.",
                "We offer tri-vision positions at the Tennis Club in Shahbagh, Paribagh and Jibon Bima Tower in Motijheel. Own all three faces for total presence, or take one face at a premium address for a fraction of a full board."),
        qa=quick_answer("A tri-vision billboard is a rotating board made of triangular slats that shows three different printed faces in turn. In Dhaka, Dhaka AD offers 20' × 10' tri-vision boards at Shahbagh Tennis Club, Paribagh and Jibon Bima Tower (Motijheel).",
                        [("Faces per board", "3"), ("Board size", "20' × 10'"), ("Locations", "3")]),
        hero=(B("paribagh-tri-vision"), "Tri-vision billboard at Paribagh, Dhaka"),
        sections=[
            ("how", "01 / HOW IT WORKS", "Three messages, one premium position", P("Triangular slats rotate together so the board changes face every few seconds. You can tell a short story across three faces, show three products, or share the board with two other advertisers and hold one face for less.")),
            ("where", "02 / WHERE", "Tri-vision locations in Dhaka", UL(["<a href='/dhaka-ad-website/static-billboards/farmgate-shahbagh/tennis-club-shahbagh-tri-vision/'>Tennis Club, Shahbagh</a>: facing Motsho Bhaban.", "<a href='/dhaka-ad-website/static-billboards/farmgate-shahbagh/paribagh-tri-vision/'>Paribagh</a>: facing Bangla Motor.", "<a href='/dhaka-ad-website/static-billboards/motijheel-old-dhaka/jibon-bima-tower-stadium-gate-tri-vision/'>Jibon Bima Tower, Stadium Gate 3</a>: facing Motijheel and Dainik Bangla."])),
            ("creative", "03 / THE CREATIVE", "Write for the turn", P("Each face is seen for a few seconds before it rotates. Make every face complete on its own, then make them stronger together: a teaser, a reveal, a call to action.")),
        ],
        faqs=[
            ("What is a tri-vision billboard?", "A rotating billboard whose triangular slats turn together to show three different printed faces in sequence. The movement attracts attention that a static board cannot.", None),
            ("Where are tri-vision billboards in Dhaka?", "Dhaka AD offers tri-vision boards at the Tennis Club in Shahbagh, at Paribagh facing Bangla Motor, and at Jibon Bima Tower near Stadium Gate 3 in Motijheel.", ("/static-billboards/farmgate-shahbagh/", "See Farmgate & Shahbagh")),
            ("Can I book only one face of a tri-vision board?", "Often, yes. Sharing a board is a cost-effective way into a premium junction. Booking all three faces gives you the position to yourself.", None),
        ],
        gallery=[(B("tennis-club-shahbagh-tri-vision"), "Tri-vision board at Tennis Club, Shahbagh"), (B("jibon-bima-tower-stadium-gate-tri-vision"), "Tri-vision board at Jibon Bima Tower, Motijheel")],
        related=[("/static-billboards/", "All billboard locations"), ("/neon-sign-advertising/", "Neon sign billboards"), ("/guides/led-vs-static-billboard/", "LED vs static billboard")],
    ),
    dict(
        path="/neon-sign-advertising/", fmt="NEON & LIT BILLBOARDS",
        title="Neon sign & illuminated billboard advertising in Dhaka | Dhaka AD",
        desc=f"Neon and illuminated billboards at Sadarghat, Hasnabad and Bosila Bridge, plus shop signage. Be visible after dark. Photos and sizes. Call {PHONE_SHOW}.",
        h1="Neon sign and illuminated billboard advertising",
        intro=P("<strong>Half of Dhaka's traffic happens after sunset. Most billboards switch off with the daylight.</strong> A neon or illuminated board does the opposite: at night it becomes one of the brightest things on the road.",
                "We plan neon faces at the Sadarghat launch terminal, Hasnabad on the road to Mawa and Bosila Bridge, and we build illuminated shop signage and light boxes for outlets that need to be found at night."),
        qa=quick_answer("Neon and illuminated billboards stay visible after dark. Dhaka AD offers neon faces at Sadarghat Launch Ghat (90' × 30'), Hasnabad in Keraniganj (two faces) and Bosila Bridge, and produces illuminated outlet signage.",
                        [("Neon faces", "3 sites"), ("Largest", "90' × 30'"), ("Also", "Shop signage")]),
        hero=(F("store-signage-night"), "Illuminated outlet signage at night"),
        sections=[
            ("why", "01 / WHY LIGHT", "Own the night shift", P("Evening commuters, launch passengers, late shoppers and long-distance buses all travel in the dark. A lit board keeps working for them while unlit neighbours disappear.")),
            ("where", "02 / WHERE", "Neon billboard locations", UL(["<a href='/dhaka-ad-website/static-billboards/motijheel-old-dhaka/sadarghat-launch-ghat-neon/'>Sadarghat Launch Ghat</a>: 90' × 30', greeting passengers from the south.", "<a href='/dhaka-ad-website/static-billboards/keraniganj/hasnabad-keraniganj-neon/'>Hasnabad, Keraniganj</a>: two faces, toward Dhaka and toward Mawa.", "<a href='/dhaka-ad-website/static-billboards/mohammadpur/bosila-bridge-mohammadpur/'>Bosila Bridge</a>: printed or neon."])),
            ("signage", "03 / FOR OUTLETS", "Illuminated signage that gets you found", P("For shops, showrooms and branches we design, fabricate and install illuminated fascia signs and light boxes, then hand them over with the wiring checked.") + links_list([("/light-box-advertising/", "Light box advertising"), ("/store-opening-activation/", "Store opening activation")])),
        ],
        faqs=[
            ("Where can I put a neon billboard in Dhaka?", "Dhaka AD offers neon faces at Sadarghat Launch Ghat, Hasnabad in Keraniganj and Bosila Bridge. We confirm current availability on the call.", ("/static-billboards/", "Browse all locations")),
            ("Is a neon billboard more expensive than a printed one?", "It usually costs more because of the fabrication and power, but it works day and night. We quote both options where a site allows, so you can compare.", ("/guides/billboard-advertising-cost-bangladesh/", "How pricing works")),
            ("Do you make illuminated signs for shops?", "Yes. We design, fabricate and install illuminated fascia signs and light boxes for outlets, usually as part of a store opening.", ("/store-opening-activation/", "Store opening activation")),
        ],
        gallery=[(B("sadarghat-launch-ghat-neon"), "Neon billboard at Sadarghat Launch Ghat"), (B("hasnabad-keraniganj-neon"), "Neon billboard at Hasnabad, Keraniganj"), (F("night-street-led-dhaka"), "Bright advertising on a Dhaka street at night")],
        related=[("/light-box-advertising/", "Light box advertising"), ("/static-billboards/", "All billboard locations"), ("/led-billboard-advertising/", "LED billboard advertising")],
    ),
    dict(
        path="/light-box-advertising/", fmt="LIGHT BOX ADVERTISING",
        title="Light box advertising & branding in Dhaka | Dhaka AD",
        desc=f"Backlit light boxes for roads, malls and outlets in Dhaka, including the Banasree corridor. Design, print, fabricate and install. Call {PHONE_SHOW}.",
        h1="Light box advertising and branding in Dhaka",
        intro=P("<strong>A printed poster fades into the wall. A lit one glows off it.</strong> Light boxes are backlit frames that make your artwork bright, sharp and readable from early morning until the shutters close.",
                "We run roadside light box corridors, such as fifteen 8' × 15' panels from Banasree Ideal School to Maradia Bazar, and we build indoor and outlet light boxes for retail, showrooms and branches."),
        qa=quick_answer("A light box is an illuminated frame with printed backlit film. Dhaka AD produces roadside light box runs (e.g. 15 panels on the Banasree corridor) and indoor or outlet light boxes, handling design, printing, fabrication and installation.",
                        [("Roadside run", "15 × 8' × 15'"), ("Also", "Indoor & outlet"), ("Alternative", "Reflective sticker")]),
        hero=(F("indoor-lightbox-display"), "Backlit display at a retail launch"),
        sections=[
            ("formats", "01 / FORMATS", "Light boxes for every setting", UL(["<strong>Roadside light box runs</strong>: repeated illuminated panels along one road.", "<strong>Outlet fascia and pylon boxes</strong>: your shop's name, lit.", "<strong>Indoor and mall light boxes</strong>: product heroes where people already shop.", "<strong>Reflective sticker panels</strong>: a lower-cost alternative that glows in headlights."])),
            ("banasree", "02 / FEATURED", "The Banasree corridor", P("Fifteen large panels from Banasree Ideal School to Maradia Bazar, facing Rampura and Hatirjheel, produced either as reflective sticker or as illuminated light boxes. <a href='/dhaka-ad-website/static-billboards/malibagh-khilgaon-banasree/banasree-ideal-school-to-maradia-bazar/'>See the corridor</a>.")),
            ("build", "03 / THE BUILD", "Printed, fabricated, installed", P("We print backlit film on large-format machines, build frames to size, wire and install, then send you photographs. One team, one invoice.")),
        ],
        faqs=[
            ("What is light box advertising?", "Advertising printed on translucent backlit film and mounted in an illuminated frame, so it stays bright and readable day and night.", None),
            ("Light box or reflective sticker?", "Light boxes glow on their own and look premium after dark. Reflective sticker costs less and lights up in vehicle headlights. We quote both where the site allows.", ("/reflective-mid-island-branding/", "Reflective median panels")),
            ("Do you make light boxes for shops?", "Yes, as fascia signs, pylon boxes and indoor displays, designed, fabricated and installed by our team.", ("/store-opening-activation/", "Store opening activation")),
        ],
        gallery=[(B("banasree-ideal-school-to-maradia-bazar"), "Banasree corridor light box panels"), (F("store-signage-night"), "Illuminated outlet signage at night")],
        related=[("/neon-sign-advertising/", "Neon sign billboards"), ("/mid-island-branding/", "Mid-island branding"), ("/large-format-printing/", "Large-format printing")],
    ),
    dict(
        path="/newspaper-insert-advertising/", fmt="NEWSPAPER INSERTS",
        title="Newspaper insert & leaflet advertising in Bangladesh | Dhaka AD",
        desc=f"Put your leaflet inside daily newspapers delivered to homes and offices in your target area. Printing, area selection and insertion handled. Call {PHONE_SHOW}.",
        h1="Newspaper insert and leaflet advertising",
        intro=P("<strong>A newspaper ad shares a page with twenty others. An insert falls into the reader's lap.</strong> Newspaper inserts put your printed leaflet inside the morning paper, delivered to the homes and offices you choose.",
                "We print your leaflet, coordinate with distributors in the areas you want, and our team inserts it paper by paper before the morning delivery round. It is one of the most direct ways to reach households in a specific neighbourhood or city."),
        qa=quick_answer("Newspaper insert advertising places a printed leaflet inside daily newspapers before home and office delivery. Dhaka AD prints the leaflets, selects distribution areas and handles insertion, ideal for store openings, offers and local launches.",
                        [("Best for", "Openings & offers"), ("Targeting", "By area"), ("Includes", "Print + insertion")]),
        hero=(F("newspaper-insert-leaflet"), "Printed leaflets ready for newspaper insertion"),
        sections=[
            ("why", "01 / WHY INSERTS", "Into the hands of the household", P("Inserts are physical, local and kept. People read them at the breakfast table, pass them around and pin them up. For a new outlet, a sale or a service area, that is hard to beat.")),
            ("how", "02 / HOW IT WORKS", "From print to doorstep", OL(["Choose the areas and newspapers that reach your customers.", "We design or adapt your leaflet and print it.", "Our team inserts each leaflet before the morning delivery round.", "You receive photographs from the insertion as proof."])),
            ("pair", "03 / AMPLIFY", "Pair it with outdoor", P("Launching a store? Combine an insert in the surrounding area with a street banner and a billboard on the main approach. The same message, three times, in one week.") + links_list([("/store-opening-activation/", "Store opening activation"), ("/large-format-printing/", "Banners and printing")])),
        ],
        faqs=[
            ("What is newspaper insert advertising?", "A printed leaflet or flyer slipped inside daily newspapers before they are delivered, so it reaches readers' homes and offices with the morning paper.", None),
            ("Can I target a specific area of Dhaka?", "Yes. Inserts are planned by distribution area, so you can focus on the neighbourhoods around your outlet or service zone.", None),
            ("Do you print the leaflets?", "Yes. We can design, print and insert, or insert leaflets you have already printed.", ("/large-format-printing/", "Our printing")),
        ],
        gallery=[(F("newspaper-insert-handling"), "Team inserting leaflets into newspapers"), (F("newspaper-bundle-insert"), "Newspaper bundles with inserted leaflets")],
        related=[("/print-and-media/", "Print and media buying"), ("/store-opening-activation/", "Store opening activation"), ("/digital-marketing/", "Digital marketing")],
    ),
    dict(
        path="/event-management/", fmt="EVENTS & PRODUCTION",
        title="Event management company in Dhaka: stage, LED wall, lights | Dhaka AD",
        desc=f"Corporate events, concerts, launches and celebrations in Dhaka: stage and truss, LED walls, lighting, sound, live camera and control. One team. Call {PHONE_SHOW}.",
        h1="Event management and production in Dhaka",
        intro=P("<strong>Your guests will forget the speeches. They will remember how the night felt.</strong> That feeling is built from a hundred technical decisions: the stage height, the LED wall behind it, the lights on the beat, the camera feed on the big screen.",
                "We build events end to end: stage and truss, LED video walls, moving-head lighting, sound, live cameras and the control desk that runs it all. Corporate nights, New Year shows, concerts by the pool, launches and conferences, in Dhaka and beyond."),
        qa=quick_answer("Dhaka AD produces events end to end: stage and truss construction, LED video walls, moving-head and wash lighting, sound, live multi-camera and vision mixing, plus branding and printing. Tell us the date, venue and guest count to get a plan.",
                        [("Builds", "Stage · LED · Light · Sound"), ("Live", "Camera & vision mixing"), ("Scope", "Dhaka & beyond")]),
        hero=(F("new-year-stage-led"), "Lit stage with LED wall at a celebration night"),
        sections=[
            ("problem", "01 / THE RISK", "One weak supplier can sink the night", P("Separate vendors for the stage, screens, lights and sound means four schedules, four crews and nobody owning the moment when something goes wrong at 8pm. Guests do not see vendors. They see your brand.")),
            ("what", "02 / WHAT WE BUILD", "Everything the stage needs", UL(["<strong>Stage and truss</strong>: platforms, ground support, lighting rigs and backdrop frames.", "<strong>LED video walls</strong>: modular screens sized to the stage. <a href='/dhaka-ad-website/led-screen-rental/'>LED screen rental</a>", "<strong>Lighting</strong>: moving heads, beams, washes and effects programmed to the show.", "<strong>Sound</strong>: PA, monitors and engineers.", "<strong>Live camera and control</strong>: multi-camera capture, vision mixing and screen feeds.", "<strong>Branding</strong>: printed backdrops, stage skirts, signage and photo walls."])),
            ("how", "03 / THE PROCESS", "How a show comes together", OL(["Brief: date, venue, guests, run of show.", "Design: stage layout, screen size, lighting plan.", "Quote: one clear budget for the whole production.", "Build: our crew installs and tests on site.", "Show: our technicians run it live.", "Strike: we clear the venue on schedule."])),
        ],
        faqs=[
            ("What does an event management company in Dhaka provide?", "Typically stage and truss, LED screens, lighting, sound, branding and on-site crew. Dhaka AD also provides live multi-camera production and the control desk, so one team owns the whole show.", None),
            ("Can you rent an LED wall for my event?", "Yes. We supply modular LED video walls sized for the stage, with the processor, operator and content playback.", ("/led-screen-rental/", "LED screen rental")),
            ("How far ahead should I book?", "As early as possible, especially for December, Eid and New Year dates. Call with your date and venue and we will confirm crew and equipment availability.", None),
            ("Do you work outside Dhaka?", "Yes. We have built shows at resorts and venues outside the city. Travel and logistics are included in the plan.", None),
        ],
        gallery=[(F("stage-led-wall-live"), "Band stage with LED wall behind"), (F("concert-stage-crowd"), "Concert stage with lighting and crowd"), (F("dj-stage-led-crowd"), "DJ stage with LED screens and lasers"),
                 (F("waterfront-stage-night"), "Waterfront stage reflected in a pool at night"), (F("event-control-room"), "Vision mixing and control desk"), (F("night-truss-build"), "Crew building truss at night"),
                 (F("broadcast-camera-stage"), "Broadcast camera facing the stage"), (F("event-dance-floor-lights"), "Lit dance floor under truss lighting"), (F("stage-red-lights"), "Stage washed in red light")],
        related=[("/led-screen-rental/", "LED screen rental"), ("/brand-activation/", "Brand activation"), ("/store-opening-activation/", "Store opening activation"), ("/our-work/", "Our work")],
    ),
    dict(
        path="/led-screen-rental/", fmt="LED SCREEN RENTAL",
        title="LED screen & video wall rental in Dhaka for events | Dhaka AD",
        desc=f"Rent indoor and outdoor LED video walls in Dhaka for concerts, conferences and launches, with truss, processor, operator and content playback. Call {PHONE_SHOW}.",
        h1="LED screen and video wall rental in Dhaka",
        intro=P("<strong>From the back row, your speaker is a dot. On an LED wall, they are the whole room.</strong> A bright, seamless video wall makes every guest feel close to the stage, and it carries your brand all night.",
                "We rent modular LED walls for indoor and outdoor events, built to the size your stage needs, mounted on truss or ground stacks, with a processor, operator and playback. Pair it with our cameras and the room sees every moment live."),
        qa=quick_answer("Dhaka AD rents modular indoor and outdoor LED video walls for events, sized to the stage, with truss or ground support, video processor, operator and content playback, and optional live camera feeds.",
                        [("Indoor & outdoor", "Yes"), ("Includes", "Operator & processor"), ("Add-on", "Live cameras")]),
        hero=(F("event-led-wall-build"), "LED wall being assembled for an outdoor event"),
        sections=[
            ("what", "01 / WHAT YOU GET", "A complete screen, not just panels", UL(["LED cabinets built to your stage size.", "Truss or ground-stack support, rigged by our crew.", "Video processor and playback laptop.", "A technician on site for the whole event.", "Optional live camera feed and vision mixing."])),
            ("size", "02 / RIGHT SIZE", "How big should the screen be?", P("Size follows the furthest guest. As a rule of thumb, the image should be readable from the back row; for most ballrooms that means several metres wide. Tell us the room and the guest count and we will recommend the size and pixel pitch.") + links_list([("/guides/p4-vs-p5-outdoor-led-display/", "Understand pixel pitch")])),
            ("permanent", "03 / NEED IT PERMANENT?", "Buy instead of rent", P("For showrooms, malls and building façades we supply and install permanent P4 and P5 outdoor displays with structure and warranty.") + links_list([("/outdoor-led-display-installation/", "P4 & P5 LED installation")])),
        ],
        faqs=[
            ("Can I rent an LED screen for one day in Dhaka?", "Yes. Most event rentals are for a single day or a few days, including set-up and dismantling. Call with your date and venue.", None),
            ("Is an operator included with LED screen rental?", "Yes. A technician sets up the wall, runs playback and stays on site for the event.", None),
            ("Do you have outdoor LED screens for events?", "Yes. Outdoor-rated cabinets are bright enough for daylight and protected against weather.", None),
        ],
        gallery=[(F("stage-led-truss-build"), "LED wall and truss under construction"), (F("new-year-stage-led"), "LED wall at a celebration night"), (F("led-stage-green"), "LED stage lit in green")],
        related=[("/event-management/", "Event management"), ("/outdoor-led-display-installation/", "Permanent LED installation"), ("/brand-activation/", "Brand activation")],
    ),
    dict(
        path="/store-opening-activation/", fmt="STORE OPENING ACTIVATION",
        title="Store opening & outlet launch activation in Bangladesh | Dhaka AD",
        desc=f"Launch a new outlet with a crowd: backdrop and ribbon-cutting, street banners, newspaper inserts, signage, lights and media. Planned by one team. Call {PHONE_SHOW}.",
        h1="Store opening and outlet launch activation",
        intro=P("<strong>An outlet that opens quietly spends its first year being discovered.</strong> One that opens with a moment, a crowd at the ribbon, cameras, banners up and down the street and a leaflet in every nearby home, starts on day one with a queue.",
                "We plan the whole launch: branded backdrop and ribbon-cutting, street banners, illuminated signage, newspaper inserts across the catchment, lighting and the photographs you will share for weeks."),
        qa=quick_answer("A store opening activation combines a branded launch event (backdrop, ribbon-cutting, guests, photography) with local awareness: street banners, newspaper inserts, signage and nearby billboards. Dhaka AD plans and delivers all of it.",
                        [("Launch day", "Backdrop · ribbon · media"), ("Week before", "Banners · inserts"), ("After", "Signage · billboards")]),
        hero=(F("ribbon-cutting-opening"), "Ribbon-cutting at an outlet opening"),
        sections=[
            ("plan", "01 / THE PLAN", "Build anticipation, then deliver the moment", OL(["<strong>Week before</strong>: street banners on the approaches and leaflets inside local newspapers.", "<strong>Launch day</strong>: branded backdrop, ribbon-cutting, guest management, lighting and photography.", "<strong>After</strong>: illuminated signage and a billboard on the main road keep the outlet top of mind."])),
            ("pieces", "02 / THE PIECES", "Everything we handle", UL(["Branded backdrops and photo walls.", "Street banners printed and installed overnight.", "Newspaper inserts across the catchment.", "Illuminated fascia and light boxes.", "Moving-head lights and sound for the evening.", "Photography and video."]) + links_list([("/newspaper-insert-advertising/", "Newspaper inserts"), ("/large-format-printing/", "Banners and printing"), ("/neon-sign-advertising/", "Illuminated signage")])),
        ],
        faqs=[
            ("What should a store opening activation include?", "Pre-launch awareness (street banners, newspaper inserts), a launch moment (backdrop, ribbon, guests, photography) and lasting visibility (signage and a nearby billboard). We plan the mix around your budget and catchment.", None),
            ("Can you run openings outside Dhaka?", "Yes. We have delivered outlet launches outside Dhaka, including Cox's Bazar, with banners installed overnight and the launch event on site.", None),
            ("How early should I start planning?", "Two to three weeks before opening gives time for printing, permissions and inserts. Call as soon as you have a date.", None),
        ],
        gallery=[(F("outlet-launch-backdrop"), "Branded backdrop at an outlet launch"), (F("opening-day-crowd"), "Crowd at an opening day ribbon-cutting"), (F("street-banner-night"), "Street banner installed overnight"), (F("street-banner-install"), "Crew installing a street banner")],
        related=[("/brand-activation/", "Brand activation"), ("/event-management/", "Event management"), ("/newspaper-insert-advertising/", "Newspaper inserts")],
    ),
    dict(
        path="/large-format-printing/", fmt="LARGE-FORMAT PRINTING",
        title="Large-format printing, PVC & street banners in Dhaka | Dhaka AD",
        desc=f"Billboard skins, PVC and flex banners, backdrops, backlit film and leaflets, printed and installed by one team in Dhaka. Fast turnarounds. Call {PHONE_SHOW}.",
        h1="Large-format printing, billboard skins and street banners",
        intro=P("<strong>A great design printed badly is a bad ad.</strong> Colour that shifts, seams that show and banners that sag undo weeks of creative work.",
                "We print billboard skins, PVC and flex banners, backdrops, backlit film and leaflets on large-format machines, then our crew installs them, often overnight, so your campaign is up when the city wakes."),
        qa=quick_answer("Dhaka AD prints billboard skins, PVC/flex banners, backdrops, backlit light box film and leaflets, and installs them. Static billboard printing is quoted separately from the media rent so you can compare.",
                        [("Prints", "Skins · banners · film"), ("Installs", "Yes, often overnight"), ("Proof", "Photos")]),
        hero=(F("large-format-printing"), "Large-format printer producing a banner"),
        sections=[
            ("what", "01 / WHAT WE PRINT", "From billboard skins to leaflets", UL(["Billboard and wall skins in PVC and flex.", "Street and festoon banners.", "Event backdrops and stage skirts.", "Backlit film for light boxes.", "Leaflets and inserts."])),
            ("install", "02 / INSTALLATION", "Printed today, up tonight", P("Our crews install banners and skins with ladders and safety gear at night, when roads are quiet, then send photographs so you can see the result before your customers do.")),
        ],
        faqs=[
            ("Is billboard printing included in the rent?", "Usually not. Media rent, printing and installation are separate lines in our quotations so you can see each cost.", ("/guides/billboard-advertising-cost-bangladesh/", "How billboard pricing works")),
            ("How quickly can you print a banner?", "Simple banners can often be printed and installed within a day or two of artwork approval. Large skins take a little longer.", None),
        ],
        gallery=[(F("printed-banner-output"), "Printed banner coming off the machine"), (F("street-banner-night"), "Street banner installed at night"), (F("street-banner-install"), "Crew installing a banner")],
        related=[("/print-and-media/", "Print and media buying"), ("/static-billboards/", "Billboard locations"), ("/store-opening-activation/", "Store opening activation")],
    ),
]
