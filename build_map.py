import json

with open("trail_coords.json") as f:
    trail_coords = json.load(f)

T = "https://commons.wikimedia.org/w/thumb.php?w=600&f="

rifugios = [
    {
        "name": "Ca' Del Sole Venezia",
        "lat": 45.4375, "lon": 12.3358,
        "elev": "5 m", "type": "city-hotel",
        "vibe": "Your Venice base before/after the trek. Central location in San Marco district.",
        "rating": 3, "price": "~€100-160/night",
        "url": "https://ca-del-sol-venezia.venetohotelsweb.com/en/",
        "on_av1": False, "category": "City Hotel",
        "photo": f"{T}Canal_Grande_Chiesa_della_Salute_e_Dogana_dal_ponte_dell_Accademia.jpg"
    },
    {
        "name": "Hotel Toblacherhof",
        "lat": 46.7312, "lon": 12.2218,
        "elev": "1,243 m", "type": "city-hotel",
        "vibe": "3-star family hotel in Dobbiaco. Spa, sauna, great breakfast. 20 min from Lago di Braies. Perfect night-before base.",
        "rating": 4, "price": "~€158+/night",
        "url": "https://www.toblacherhof.com/en/",
        "on_av1": False, "category": "City Hotel",
        "photo": f"{T}Toblach_-_Dobbiaco.JPG"
    },
    {
        "name": "Rifugio Auronzo",
        "lat": 46.6095, "lon": 12.2938,
        "elev": "2,320 m", "type": "rifugio",
        "vibe": "The gateway. Right at Tre Cime trailhead. Road access, busier by day, magical at night. Sunrise at Tre Cime.",
        "rating": 4, "price": "€90-100 dorm / €220-240 double",
        "url": "https://rifugioauronzo.it/en/booking-room/",
        "on_av1": False, "category": "Tre Cime Side Trip",
        "photo": f"{T}Rifugio_Auronzo_Tre_Cime_2.JPG"
    },
    {
        "name": "Rifugio Locatelli (Drei Zinnen)",
        "lat": 46.6189, "lon": 12.3097,
        "elev": "2,405 m", "type": "rifugio",
        "vibe": "THE postcard. Beneath the three most famous peaks in the Dolomites. 10,000 booking requests/year. Cash only.",
        "rating": 5, "price": "~€85-95 half-board",
        "url": "https://www.dreizinnenhuette.com/rifugio-locatelli.php",
        "on_av1": False, "category": "Tre Cime Side Trip",
        "photo": f"{T}Tre_cime_-_rifugio_Locatelli.jpg"
    },
    {
        "name": "Hotel Prato Piazza (Plätzwiese)",
        "lat": 46.6590, "lon": 12.1380,
        "elev": "2,000 m", "type": "hotel",
        "vibe": "The meadow dream. Wide alpine meadow, panoramic views. More hotel than hut. Comfort at the start of the trek.",
        "rating": 4, "price": "~€90-120 half-board",
        "url": "https://www.pratopiazza.com/",
        "on_av1": True, "category": "AV1 Stage 1 Area",
        "photo": f"{T}Prato_Piazza.jpg"
    },
    {
        "name": "Rifugio Biella",
        "lat": 46.6530, "lon": 12.0920,
        "elev": "2,327 m", "type": "rifugio",
        "vibe": "The minimalist. First AV1 overnight from Lago di Braies. Basic dorms, functional. Gets the job done.",
        "rating": 2, "price": "~€55-65 half-board",
        "url": "",
        "on_av1": True, "category": "AV1 Stage 1",
        "photo": f"{T}Croda_del_Becco_and_Rifugio_Biella_202008.jpg"
    },
    {
        "name": "Rifugio Sennes",
        "lat": 46.6380, "lon": 12.0590,
        "elev": "2,126 m", "type": "rifugio",
        "vibe": "The plateau gem. Wide-open alpine plateau. Hearty South Tyrolean food, homemade strudel, local wine.",
        "rating": 4, "price": "~€70-85 half-board",
        "url": "https://www.sennes.com/en/",
        "on_av1": True, "category": "AV1 Stage 1-2",
        "photo": f"{T}Rifugio_Munt_Sennes_03.JPG"
    },
    {
        "name": "Rifugio Fodara Vedla",
        "lat": 46.6270, "lon": 12.0480,
        "elev": "1,980 m", "type": "rifugio",
        "vibe": "Family-run gem on the Sennes plateau. 12 rooms, garden-fresh salads, handmade pasta. Traditional South Tyrolean warmth.",
        "rating": 4, "price": "€83+ half-board",
        "url": "https://www.fodara.it/en",
        "on_av1": True, "category": "AV1 Stage 1-2",
        "photo": f"{T}Rifugio_Fodara_Vedla.jpg"
    },
    {
        "name": "Rifugio Pederü",
        "lat": 46.6180, "lon": 12.0280,
        "elev": "1,548 m", "type": "rifugio",
        "vibe": "The launch pad. Family-run alpine guesthouse, classic South Tyrolean wood. Lower elevation = warmer. Day 1 base.",
        "rating": 3, "price": "~€70-85 half-board",
        "url": "https://www.pederue.it/en",
        "on_av1": True, "category": "AV1 Stage 2 Start",
        "photo": f"{T}Fodara_Vella_-_panoramio.jpg"
    },
    {
        "name": "Rifugio Lavarella (Berghütte)",
        "lat": 46.6130, "lon": 12.0520,
        "elev": "2,042 m", "type": "rifugio",
        "vibe": "The cozy upgrade. Family-run, sauna, microbrewery(!), comfortable rooms. South Tyrolean warmth on the Fanes plateau.",
        "rating": 4, "price": "~€80-100 half-board",
        "url": "https://lavarella.it/en/book-online",
        "on_av1": True, "category": "AV1 Stage 2",
        "photo": f"{T}L%27ambiente_attorno_al_rifugio_Fanes.jpg"
    },
    {
        "name": "Rifugio Fanes",
        "lat": 46.5990, "lon": 12.0470,
        "elev": "2,060 m", "type": "rifugio",
        "vibe": "The all-rounder. Alpine plateau, dorms to premium doubles w/ private bath. Accepts cards. Mountain hotel vibes.",
        "rating": 4, "price": "€80-135 depending on room",
        "url": "https://www.rifugiofanes.com/en/rates-request/prices-conditions",
        "on_av1": True, "category": "AV1 Stage 2 End",
        "photo": f"{T}L%27ambiente_attorno_al_rifugio_Fanes.jpg"
    },
    {
        "name": "Rifugio Scotoni",
        "lat": 46.5720, "lon": 12.0120,
        "elev": "1,985 m", "type": "rifugio",
        "vibe": "The foodie stop. 50+ years old. Indoor barbecue, 400+ label wine list. Eat like a king at altitude.",
        "rating": 4, "price": "~€75-90 half-board",
        "url": "https://www.scotoni.it/en/how-to-reach-us/from-fanes-dolomites",
        "on_av1": True, "category": "AV1 Stage 3",
        "photo": f"{T}Lagozoi_Scotoni_Hutte_%282040m%29_-_panoramio.jpg"
    },
    {
        "name": "Rifugio Lagazuoi",
        "lat": 46.5279, "lon": 12.0081,
        "elev": "2,752 m", "type": "rifugio",
        "vibe": "THE CROWN JEWEL. Highest rifugio in the Dolomites. 360° panorama. Finnish sauna. Legendary sunrises. Cable car access.",
        "rating": 5, "price": "€80 dorm / €125+ double + €35 dinner",
        "url": "https://rifugiolagazuoi.com/index_en.php",
        "on_av1": True, "category": "AV1 Stage 3 End",
        "photo": f"{T}Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"
    },
    {
        "name": "Rifugio Col Gallina",
        "lat": 46.5220, "lon": 12.0060,
        "elev": "2,055 m", "type": "rifugio",
        "vibe": "At Falzarego Pass, center of Lagazuoi/5 Torri/Giau area. Double rooms w/ private bath, WiFi. Solid AV1 stop.",
        "rating": 3, "price": "~€75-90 half-board",
        "url": "https://www.rifugiocolgallina.com/en/",
        "on_av1": True, "category": "AV1 Stage 3-4",
        "photo": f"{T}Passo_di_Falzarego.jpg"
    },
    {
        "name": "Rifugio Giussani",
        "lat": 46.5380, "lon": 12.0530,
        "elev": "2,580 m", "type": "rifugio",
        "vibe": "The high camp. Beneath the Tofane peaks. Via ferrata base. Slightly off AV1 proper — worth the detour.",
        "rating": 3, "price": "€73 (€58.50 Alpine Club)",
        "url": "https://www.rifugiogiussani.com/en/accommodation-rates/",
        "on_av1": False, "category": "Detour: Tofane",
        "photo": f"{T}Rifugio_Camillo_Giussani.jpg"
    },
    {
        "name": "Rifugio Cinque Torri (5 Torri)",
        "lat": 46.5120, "lon": 12.0350,
        "elev": "2,137 m", "type": "rifugio",
        "vibe": "The rock garden. Surrounded by otherworldly Cinque Torri towers. Great for climbers. Shuttle in summer.",
        "rating": 3, "price": "~€70-80 half-board",
        "url": "https://rifugio5torri.it/en/5-torri.html",
        "on_av1": True, "category": "AV1 Stage 4",
        "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"
    },
    {
        "name": "Rifugio Averau",
        "lat": 46.5100, "lon": 12.0280,
        "elev": "2,413 m", "type": "rifugio",
        "vibe": "The balcony. Cinque Torri views, great terrace, good food. Solid mid-route stop with character.",
        "rating": 4, "price": "~€75-90 half-board",
        "url": "https://www.rifugioaverau.it/",
        "on_av1": True, "category": "AV1 Stage 4",
        "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"
    },
    {
        "name": "Rifugio Nuvolau",
        "lat": 46.5010, "lon": 12.0420,
        "elev": "2,575 m", "type": "rifugio",
        "vibe": "THE OG. Oldest rifugio in the Dolomites (1883). Summit perch, floating above clouds. No showers. Pure mountain soul.",
        "rating": 5, "price": "~€70-80 half-board",
        "url": "https://rifugionuvolau.it/en/",
        "on_av1": True, "category": "AV1 Stage 4 End",
        "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"
    },
    {
        "name": "Rifugio Croda da Lago (Palmieri)",
        "lat": 46.4950, "lon": 12.0780,
        "elev": "2,046 m", "type": "rifugio",
        "vibe": "The hidden lake. Turquoise Lago Federa, barrel sauna, buffet breakfast. Golden larches in September. A painting.",
        "rating": 5, "price": "€73 (€58.50 CAI/DAV)",
        "url": "https://www.crodadalago.it/en/prices-and-stay/",
        "on_av1": False, "category": "Detour: Lago Federa",
        "photo": f"{T}Rifugio_palmieri.jpg"
    },
    {
        "name": "Rifugio Fedare",
        "lat": 46.4780, "lon": 12.0530,
        "elev": "2,000 m", "type": "rifugio",
        "vibe": "The pass stop. Scenic Giau Pass, road accessible. Waypoint more than destination.",
        "rating": 3, "price": "€80 half-board",
        "url": "https://valfiorentinadolomiti.it/en/Rifugio-Fedare-Passo-Giau/The_rooms/Room-prices.html",
        "on_av1": True, "category": "AV1 Variant: Giau",
        "photo": f"{T}Ra_Gusela%2C_view_from_Passo_Giau.jpg"
    },
    {
        "name": "Rifugio Città di Fiume",
        "lat": 46.4350, "lon": 12.0680,
        "elev": "1,918 m", "type": "rifugio",
        "vibe": "The Pelmo basecamp. Foot of massive Pelmo monolith. Meadow dining. Small (20 beds), intimate.",
        "rating": 3, "price": "~€65-75 half-board",
        "url": "https://rifugiocittadifiume.it/?lang=en",
        "on_av1": True, "category": "AV1 Stage 5",
        "photo": f"{T}Rifugio_citta_di_fiume.JPG"
    },
    {
        "name": "Rifugio Alpino Aquileia",
        "lat": 46.4280, "lon": 12.0450,
        "elev": "1,583 m", "type": "rifugio",
        "vibe": "Family-run, 25 beds. Homemade pasta, dumplings, game dishes. Slight detour from AV1 but worth it.",
        "rating": 3, "price": "~€65-75 half-board",
        "url": "https://www.rifugioaquileia.it/",
        "on_av1": False, "category": "Detour: Near Pelmo",
        "photo": f"{T}Rifugio_citta_di_fiume.JPG"
    },
    {
        "name": "Rifugio Passo Staulanza",
        "lat": 46.4080, "lon": 12.0580,
        "elev": "1,783 m", "type": "rifugio",
        "vibe": "The comfort stop. Road-accessible, 13 rooms all en-suite. More hotel than hut. Real shower, proper bed.",
        "rating": 3, "price": "~€70-85 half-board",
        "url": "https://www.staulanza.it/prenotazioni.php?lang=en",
        "on_av1": True, "category": "AV1 Stage 5-6",
        "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"
    },
    {
        "name": "Rifugio Coldai (Sonino al Coldai)",
        "lat": 46.3780, "lon": 12.0530,
        "elev": "2,135 m", "type": "rifugio",
        "vibe": "The wild card. 93 beds, better availability. Lago Coldai + Civetta views. Quieter than Tissi, arguably as beautiful.",
        "rating": 4, "price": "~€65-75 half-board",
        "url": "https://rifugiocoldai.com/index_en.php",
        "on_av1": True, "category": "AV1 Stage 6",
        "photo": f"{T}Rifugio_Coldai.jpg"
    },
    {
        "name": "Rifugio Tissi",
        "lat": 46.3650, "lon": 12.0480,
        "elev": "2,250 m", "type": "rifugio",
        "vibe": "THE SUNSET KING. Civetta's 1,000m wall turns blood-red at sunset. Most dramatic view on any AV route. Small, intimate.",
        "rating": 5, "price": "~€65-75 half-board",
        "url": "",
        "on_av1": True, "category": "AV1 Stage 7",
        "photo": f"{T}Monte_Civetta.jpg"
    },
    {
        "name": "Rifugio Vazzoler",
        "lat": 46.3520, "lon": 12.0350,
        "elev": "1,714 m", "type": "rifugio",
        "vibe": "The lowkey legend. Beneath Civetta. Cash only, €30 deposit. Old-school authentic rifugio vibe.",
        "rating": 3, "price": "~€60-70 half-board",
        "url": "https://rifugiovazzoler.com/Booking/index_en.php",
        "on_av1": True, "category": "AV1 Stage 7-8",
        "photo": f"{T}IMG_0058_Rif._Mario_Vazzoler.JPG"
    },
    {
        "name": "Rifugio Carestiato",
        "lat": 46.3380, "lon": 12.0180,
        "elev": "2,760 m", "type": "rifugio",
        "vibe": "The high point. Near Marmolada glacier area. Online booking, deposit required.",
        "rating": 3, "price": "~€65-75 half-board",
        "url": "https://www.rifugiocarestiato.com/Booking/index_en.php",
        "on_av1": True, "category": "AV1 Stage 8",
        "photo": f"{T}Monte_Civetta.jpg"
    },
    {
        "name": "Rifugio Sommariva al Pramperet",
        "lat": 46.3050, "lon": 12.1080,
        "elev": "1,857 m", "type": "rifugio",
        "vibe": "The time capsule. Built 1923. 25 beds, 6-8 person rooms. Deep in Val Pramper — 100 years back in time.",
        "rating": 3, "price": "~€55-65 half-board",
        "url": "https://www.rifugiosommarivaalpramperet.it/rifugio.asp",
        "on_av1": True, "category": "AV1 Stage 9",
        "photo": f"{T}Am_Rifugio_Pramperet.JPG"
    },
    {
        "name": "Rifugio Pian de Fontana",
        "lat": 46.2650, "lon": 12.1580,
        "elev": "1,632 m", "type": "rifugio",
        "vibe": "The chef's table. Legendary food (manager Gavino). Remote Bellunesi Dolomites. Almost no tourists.",
        "rating": 4, "price": "~€55-65 half-board",
        "url": "",
        "on_av1": True, "category": "AV1 Stage 10",
        "photo": f"{T}National_Park_of_the_Belluno_Dolomites.jpg"
    },
    {
        "name": "Tenuta Contarini",
        "lat": 45.8830, "lon": 11.7220,
        "elev": "120 m", "type": "city-hotel",
        "vibe": "17-room country hotel in Brenta Valley. Garden setting. Good post-trek wind-down before Venice.",
        "rating": 3, "price": "~€80-120/night",
        "url": "https://www.contarini.it/en",
        "on_av1": False, "category": "Post-Trek Hotel",
        "photo": f"{T}Bassano_del_Grappa_120508_01.jpg"
    },
    {
        "name": "Rifugio Re Alberto (Garlhutte)",
        "lat": 46.4430, "lon": 11.6080,
        "elev": "2,621 m", "type": "rifugio",
        "vibe": "The adventure pick. Steel ladder access (light via ferrata). Secluded, far from crowds. WhatsApp booking only.",
        "rating": 4, "price": "~€60-70 half-board",
        "url": "",
        "on_av1": False, "category": "Off-Route: Rosengarten",
        "photo": f"{T}Torri_del_Vajolet%2C_rifugio_Re_Alberto.jpg"
    },
]

attractions = [
    # ── LAKES ──
    {"name": "Lago di Braies (Pragser Wildsee)", "lat": 46.6940, "lon": 12.0855, "desc": "AV1 starting point. Iconic emerald-green lake surrounded by cliffs. One of the most photographed spots in the Dolomites. Wooden boathouse.", "photo": f"{T}Pragser_Wildsee_-_Lago_di_Braies_04.jpg"},
    {"name": "Lago Federa", "lat": 46.4960, "lon": 12.0800, "desc": "Hidden turquoise alpine lake at 2,046m. Surrounded by larches that turn gold in September. Feels like a painting.", "photo": f"{T}Rifugio_palmieri.jpg"},
    {"name": "Lago Coldai", "lat": 46.3800, "lon": 12.0560, "desc": "Small alpine lake at 2,143m reflecting Monte Civetta. One of the most serene spots on AV1.", "photo": f"{T}Rifugio_Coldai.jpg"},
    {"name": "Lago di Limo", "lat": 46.6100, "lon": 12.0550, "desc": "Floating peat-bog lake on the Fanes plateau. Unique ecosystem — the ground literally bounces when you walk near it.", "photo": f"{T}L%27ambiente_attorno_al_rifugio_Fanes.jpg"},
    {"name": "Lé Vërt (Green Lake)", "lat": 46.6150, "lon": 12.0540, "desc": "Small emerald lake near Rifugio Lavarella. Vivid green color from mineral deposits. Peaceful morning spot.", "photo": f"{T}L%27ambiente_attorno_al_rifugio_Fanes.jpg"},
    {"name": "Lago di Dobbiaco", "lat": 46.7250, "lon": 12.2050, "desc": "Scenic lake near Dobbiaco with easy walking paths. Good warm-up hike the day before AV1. Birdwatching area.", "photo": f"{T}Toblach_-_Dobbiaco.JPG"},
    {"name": "Lago di Alleghe", "lat": 46.4050, "lon": 12.0200, "desc": "Lake formed by a 1771 landslide at the foot of Civetta. Charming village on the shore. Possible resupply point.", "photo": f"{T}Monte_Civetta.jpg"},

    # ── MAJOR PEAKS & WALLS ──
    {"name": "Tre Cime di Lavaredo", "lat": 46.6187, "lon": 12.3015, "desc": "The three most iconic peaks in the Dolomites. UNESCO World Heritage. The circuit hike is a must-do.", "photo": f"{T}Tre_Cime_di_Lavaredo_2012_2.jpg"},
    {"name": "Tofane Peaks", "lat": 46.5450, "lon": 12.0650, "desc": "Three massive peaks (3,244m) towering over Cortina. Via ferrata paradise. Visible from most of the AV1 mid-section.", "photo": f"{T}Tofana.jpg"},
    {"name": "Monte Pelmo", "lat": 46.4250, "lon": 12.0850, "desc": "Massive isolated monolith (3,168m). Called 'the throne of God'. Dominates the skyline for days on AV1.", "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"},
    {"name": "Monte Civetta (North Wall)", "lat": 46.3700, "lon": 12.0500, "desc": "1,000m vertical north wall — one of the biggest rock faces in the Alps. Turns blood-red at sunset.", "photo": f"{T}Monte_Civetta.jpg"},
    {"name": "Marmolada (View Point)", "lat": 46.4350, "lon": 11.8600, "desc": "Queen of the Dolomites (3,343m). Highest peak with the last glacier. Visible from Lagazuoi.", "photo": f"{T}Marmolada%2C_Italy.jpg"},
    {"name": "Croda del Becco (Seekofel)", "lat": 46.6580, "lon": 12.0950, "desc": "Striking 2,810m peak above Rifugio Biella. Its red-tinged dolomite glows at sunrise. Dominates the Braies skyline.", "photo": f"{T}Croda_del_Becco_and_Rifugio_Biella_202008.jpg"},
    {"name": "Croda Rossa d'Ampezzo", "lat": 46.6350, "lon": 12.1200, "desc": "Red Mountain (3,146m). Named for its distinctive red-orange rock. Visible throughout the Fanes-Sennes area.", "photo": f"{T}Prato_Piazza.jpg"},
    {"name": "Monte Schiara", "lat": 46.2200, "lon": 12.1300, "desc": "Final major peak on AV1 (2,565m). Dramatic spire visible on the last stages. The Gusela del Vescovà needle is iconic.", "photo": f"{T}Am_Rifugio_Pramperet.JPG"},
    {"name": "Cima Cunturines", "lat": 46.5900, "lon": 12.0100, "desc": "3,064m peak with the world's highest bear cave (Conturines Cave). 50,000-year-old bear fossils found inside.", "photo": f"{T}Rifugio_Munt_Sennes_03.JPG"},

    # ── ROCK FORMATIONS ──
    {"name": "Cinque Torri", "lat": 46.5150, "lon": 12.0400, "desc": "Five dramatic rock towers rising from alpine meadows. World-class climbing. Open-air WWI museum at the base.", "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"},
    {"name": "Torre Grande (Cinque Torri)", "lat": 46.5140, "lon": 12.0420, "desc": "The tallest of the five towers. Classic multi-pitch climbing routes. Stunning from every angle.", "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"},
    {"name": "Torri del Vajolet", "lat": 46.4450, "lon": 11.6100, "desc": "Three needle-like towers in the Rosengarten. Among the most dramatic rock spires in the Alps. Near Rifugio Re Alberto.", "photo": f"{T}Torri_del_Vajolet%2C_rifugio_Re_Alberto.jpg"},

    # ── PASSES ──
    {"name": "Passo Falzarego", "lat": 46.5200, "lon": 12.0080, "desc": "Major Dolomite pass at 2,105m. Lagazuoi cable car base. WWI tunnel museum. Crossroads of AV1.", "photo": f"{T}Passo_di_Falzarego.jpg"},
    {"name": "Passo Giau", "lat": 46.4840, "lon": 12.0520, "desc": "Stunning mountain pass at 2,236m. Famous cycling climb. Sweeping views of Nuvolau, Pelmo, and Civetta.", "photo": f"{T}Ra_Gusela%2C_view_from_Passo_Giau.jpg"},
    {"name": "Passo Staulanza", "lat": 46.4100, "lon": 12.0600, "desc": "Mountain pass at 1,766m between Pelmo and Civetta. Road-accessible resupply point. Gateway to the Civetta group.", "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"},
    {"name": "Forcella Lavaredo", "lat": 46.6160, "lon": 12.3050, "desc": "The saddle between Tre Cime and the main ridge. Dramatic viewpoint where you first see the three towers head-on.", "photo": f"{T}Tre_Cime_di_Lavaredo_2012_2.jpg"},
    {"name": "Forcella del Lago", "lat": 46.4980, "lon": 12.0700, "desc": "High saddle at 2,486m with views down to Lago Federa. The moment you crest and see the lake is unforgettable.", "photo": f"{T}Rifugio_palmieri.jpg"},

    # ── WWI HISTORY ──
    {"name": "Lagazuoi WWI Tunnels", "lat": 46.5290, "lon": 12.0070, "desc": "1km of restored WWI mine tunnels inside Piccolo Lagazuoi. Free open-air museum. Headlamp required. Incredible history.", "photo": f"{T}Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"},
    {"name": "Martini Ledge (WWI)", "lat": 46.5285, "lon": 12.0065, "desc": "Historic military ledge where Italian soldiers were stationed. Wooden huts you can visit. Panoramic views + deep history.", "photo": f"{T}Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"},
    {"name": "Cinque Torri WWI Open Air Museum", "lat": 46.5130, "lon": 12.0380, "desc": "Restored WWI trenches and fortifications among the towers. Free to visit. Info boards explain the Austrian-Italian front.", "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"},

    # ── WATERFALLS & GORGES ──
    {"name": "Fanes Waterfall (Cascate di Fanes)", "lat": 46.6050, "lon": 12.0350, "desc": "Beautiful cascading waterfall in the Fanes valley. Passed on the approach from Pederü to Fanes plateau.", "photo": f"{T}Gola_di_Fanes_2008.JPG"},
    {"name": "Gola di Fanes (Fanes Gorge)", "lat": 46.6030, "lon": 12.0330, "desc": "Narrow limestone gorge carved by the Fanes stream. Dramatic rock walls tower overhead. Feels like entering another world.", "photo": f"{T}Gola_di_Fanes_2008.JPG"},
    {"name": "Cascata di Pisciadu", "lat": 46.5250, "lon": 11.8300, "desc": "Spectacular 30m waterfall near Passo Gardena. Accessible via short via ferrata. One of the most photogenic falls in the Dolomites.", "photo": f"{T}Marmolada%2C_Italy.jpg"},

    # ── TOWNS & VILLAGES ──
    {"name": "Cortina d'Ampezzo", "lat": 46.5369, "lon": 12.1356, "desc": "Queen of the Dolomites. Glamorous alpine town, 2026 Winter Olympics host. Corso Italia shopping street, basilica, great restaurants. Resupply point.", "photo": f"{T}Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"},
    {"name": "Belluno (AV1 Finish)", "lat": 46.1413, "lon": 12.2170, "desc": "Historic city at the AV1 finish. Beautiful Piazza dei Martiri, Palazzo dei Rettori, gelato. Train back to Venice from here.", "photo": f"{T}Bassano_del_Grappa_120508_01.jpg"},
    {"name": "San Vigilio di Marebbe", "lat": 46.6980, "lon": 11.9330, "desc": "Charming Ladin village near AV1 start. Gateway to Fanes-Sennes-Braies park. Good restaurants, authentic culture.", "photo": f"{T}Toblach_-_Dobbiaco.JPG"},
    {"name": "Selva di Cadore", "lat": 46.4400, "lon": 12.0350, "desc": "Small village near Monte Pelmo. Possible resupply stop. Local cheese and salumi shops.", "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"},
    {"name": "Forno di Zoldo", "lat": 46.3500, "lon": 12.1100, "desc": "Valley town between Civetta and Bellunesi stages. Ice cream capital of Italy — many gelato dynasties started here.", "photo": f"{T}Monte_Civetta.jpg"},

    # ── CABLE CARS & LIFTS ──
    {"name": "Lagazuoi Cable Car", "lat": 46.5210, "lon": 12.0070, "desc": "Cable car from Falzarego Pass to Rifugio Lagazuoi summit (2,752m). Skip the climb or use as bail-out option. Runs every 15 min.", "photo": f"{T}Passo_di_Falzarego.jpg"},
    {"name": "Freccia nel Cielo (Arrow in the Sky)", "lat": 46.5400, "lon": 12.1300, "desc": "Cortina's famous cable car to Tofana di Mezzo (3,244m). Highest viewpoint accessible without climbing. Mind-blowing panorama.", "photo": f"{T}Tofana.jpg"},

    # ── NATURE & WILDLIFE ──
    {"name": "Fanes-Sennes-Braies Natural Park", "lat": 46.6300, "lon": 12.0500, "desc": "South Tyrol's largest protected area (25,680 ha). UNESCO World Heritage. Home to chamois, marmots, ibex, and golden eagles.", "photo": f"{T}Rifugio_Fodara_Vedla.jpg"},
    {"name": "Marmots' Parliament", "lat": 46.6200, "lon": 12.0600, "desc": "Rock formation on the Fanes plateau where, according to Ladin legend, marmots sheltered the last people of the Kingdom of Fanes.", "photo": f"{T}L%27ambiente_attorno_al_rifugio_Fanes.jpg"},
    {"name": "Conturines Cave (Bear Cave)", "lat": 46.5850, "lon": 12.0050, "desc": "World's highest bear cave at 2,800m on Cima Cunturines. 50,000-year-old Ladin bear fossils discovered in 1987. Not accessible but viewable.", "photo": f"{T}Rifugio_Munt_Sennes_03.JPG"},
    {"name": "Dolomiti Bellunesi National Park", "lat": 46.2500, "lon": 12.1000, "desc": "Wild, remote national park on AV1's final stages. Far fewer tourists. Chamois, deer, golden eagles. True wilderness.", "photo": f"{T}Am_Rifugio_Pramperet.JPG"},

    # ── VIEWPOINTS ──
    {"name": "Piccolo Lagazuoi Summit", "lat": 46.5300, "lon": 12.0075, "desc": "2,778m summit just above the rifugio. 5-min walk for the best sunrise/sunset viewpoint on the entire AV1. 360° panorama.", "photo": f"{T}Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"},
    {"name": "Monte Nuvolau Summit", "lat": 46.5020, "lon": 12.0430, "desc": "2,574m summit with the oldest rifugio perched on top. 360° views of Cortina basin, Marmolada, Tofane, Pelmo, Civetta.", "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"},
    {"name": "Cappella Lago di Braies", "lat": 46.6950, "lon": 12.0870, "desc": "Small chapel on the shore of Lago di Braies. Charming photo spot on the lake loop trail. 10 min from the trailhead.", "photo": f"{T}Pragser_Wildsee_-_Lago_di_Braies_04.jpg"},

    # ── ADDITIONAL LAKES ──
    {"name": "Lago di Sorapis", "lat": 46.5206, "lon": 12.2233, "desc": "Stunning turquoise glacial lake at 1,925m, famous for milky-blue color from suspended dolomite powder. 2-hour hike from Passo Tre Croci.", "photo": f"{T}Lago_di_Sorapis.jpg"},
    {"name": "Lago di Misurina", "lat": 46.5819, "lon": 12.2539, "desc": "Largest natural lake in Cadore at 1,754m. Panoramic views of Tre Cime and Cristallo. Known for exceptionally pure air.", "photo": f"{T}Lago_di_misurina.jpg"},
    {"name": "Lago di Limides", "lat": 46.5115, "lon": 12.0231, "desc": "Small reflective lake near Falzarego, famous for mirroring Tofane and Lagazuoi at sunset. 20-min walk from Col Gallina.", "photo": f"{T}Dolomity_-_Lago_di_Limides_02.jpg"},
    {"name": "Lago di Valparola", "lat": 46.5389, "lon": 11.9794, "desc": "Alpine lake at 2,164m below Passo Valparola, framed by Fanes peaks. Easy access from the pass road.", "photo": f"{T}Valparolapass.jpg"},
    {"name": "Lago d'Antorno", "lat": 46.5950, "lon": 12.2654, "desc": "Picturesque lake at 1,866m on the road to Tre Cime. Classic reflections of the Cadini di Misurina spires.", "photo": f"{T}Lago_d%27Antorno_e_Cadini_di_Misurina.jpg"},
    {"name": "Lago di Mosigo", "lat": 46.4530, "lon": 12.2100, "desc": "Small lake in San Vito di Cadore with a famous reflection of Monte Antelao, the 'King of the Dolomites'.", "photo": f"{T}Antelao_Lago_di_Mosigo.jpg"},

    # ── ADDITIONAL PEAKS ──
    {"name": "Monte Antelao", "lat": 46.4525, "lon": 12.2606, "desc": "At 3,264m, the 'King of the Dolomites' and highest peak in the eastern Dolomites. Massive pyramid dominates the skyline south of Cortina.", "photo": f"{T}Monte_Antelao_6.jpg"},
    {"name": "Croda da Lago", "lat": 46.4830, "lon": 12.1000, "desc": "Dramatic mountain group east of Passo Giau. Cima d'Ambrizzola reaches 2,715m. AV1 passes along its base near Lago Federa.", "photo": f"{T}Croda_da_Lago_Lastoi_de_Formin.jpg"},
    {"name": "Monte Averau", "lat": 46.5011, "lon": 12.0373, "desc": "Highest peak of the Nuvolau Group at 2,649m. 360° views from Civetta to Marmolada. Short via ferrata from Rifugio Averau.", "photo": f"{T}Fort_Tre_Sassi_und_Averau_%28Valparolapass%29.jpg"},
    {"name": "Sass de Stria", "lat": 46.5211, "lon": 11.9969, "desc": "The 2,477m 'Witch's Rock' above Falzarego, riddled with WWI tunnels. Summit views of the entire Falzarego battlefield.", "photo": f"{T}Sass_de_Stria_Falzarego_Lagazuoi.jpg"},
    {"name": "Col di Lana", "lat": 46.4967, "lon": 11.9592, "desc": "The 2,462m 'Blood Hill' of WWI. Italian forces detonated a massive mine in 1916. Summit cross and crater mark the explosion.", "photo": f"{T}Ccol_di_Lana_Sief.jpg"},
    {"name": "Punta Sorapiss", "lat": 46.5069, "lon": 12.2117, "desc": "At 3,205m, highest peak of the Sorapiss Group. North face holds remnants of the Sorapiss glacier. Visible from much of AV1.", "photo": f"{T}Sorapiss_von_Tondi_de_Faloria.jpg"},
    {"name": "Monte Cristallo", "lat": 46.5750, "lon": 12.2000, "desc": "Majestic 3,221m massif NE of Cortina with four summits over 3,000m. Long serrated ridge visible from Misurina to Cortina.", "photo": f"{T}Monte-Cristallo_Forcella-Staunies_3239a.jpg"},
    {"name": "Becco di Mezzodì", "lat": 46.4603, "lon": 12.0808, "desc": "The 2,603m 'Midday Peak' — sun sits directly above it at noon from Cortina. Striking spire above Lago Federa.", "photo": f"{T}Becco_di_Mezzod%C3%AC.jpg"},
    {"name": "Piz Boè", "lat": 46.5089, "lon": 11.8281, "desc": "Highest summit of the Sella Group at 3,152m. One of the easiest 3,000m peaks in the Dolomites. Reachable from Sass Pordoi cable car.", "photo": f"{T}Sella_group_with_Piz_Bo%C3%A8.jpg"},
    {"name": "Ra Gusela", "lat": 46.4907, "lon": 12.0508, "desc": "Slender 2,595m rock needle above Passo Giau, meaning 'the spindle' in Ladin. Short via ferrata to summit with Pelmo/Civetta views.", "photo": f"{T}Ra_Gusela%2C_view_from_Passo_Giau.jpg"},
    {"name": "Monte Rite", "lat": 46.3844, "lon": 12.2581, "desc": "Isolated 2,183m summit hosting Reinhold Messner's 'Museum in the Clouds' in a restored WWI fort. 360° panoramic terrace.", "photo": f"{T}Monte_Rite.jpg"},
    {"name": "Sass de Mura", "lat": 46.1636, "lon": 11.9253, "desc": "Highest peak of the Cimonega Group at 2,547m in Dolomiti Bellunesi. Remote, wild summit near AV1's southern end.", "photo": f"{T}National_Park_of_the_Belluno_Dolomites.jpg"},
    {"name": "Cadini di Misurina", "lat": 46.5900, "lon": 12.2800, "desc": "Spectacular group of jagged spires and towers east of Tre Cime. Over 20 individual peaks. Best viewed from Lago d'Antorno.", "photo": f"{T}Lago_d%27Antorno_e_Cadini_di_Misurina.jpg"},
    {"name": "Lastoi de Formin", "lat": 46.4750, "lon": 12.0950, "desc": "Dramatic flat-topped plateau at 2,657m near Croda da Lago. Contains dinosaur footprints from 210 million years ago.", "photo": f"{T}Croda_da_Lago_Lastoi_de_Formin.jpg"},

    # ── ADDITIONAL PASSES ──
    {"name": "Passo Tre Croci", "lat": 46.5572, "lon": 12.2002, "desc": "Alpine pass at 1,809m connecting Cortina with Misurina. Named after three crosses. Start of the Sorapis lake hike.", "photo": f"{T}Monte-Cristallo_Forcella-Staunies_3239a.jpg"},
    {"name": "Passo Valparola", "lat": 46.5433, "lon": 11.9736, "desc": "Historic 2,168m pass between Cortina and Alta Badia. Site of WWI 'Yellow Line'. Home to Forte Tre Sassi museum.", "photo": f"{T}Valparolapass.jpg"},
    {"name": "Passo Duran", "lat": 46.3250, "lon": 12.0958, "desc": "Mountain pass at 1,601m connecting Agordo with Val di Zoldo. Small church at summit. Used in the Giro d'Italia.", "photo": f"{T}Monte_Civetta.jpg"},
    {"name": "Passo Cibiana", "lat": 46.3742, "lon": 12.2589, "desc": "Pass at 1,530m connecting Val Boite with Val di Zoldo. Gateway to Monte Rite and Messner's Mountain Museum.", "photo": f"{T}Monte_Rite.jpg"},
    {"name": "Forcella Ambrizzola", "lat": 46.4750, "lon": 12.0900, "desc": "Scenic 2,277m saddle on AV1 between Passo Giau and Croda da Lago. Panoramic views of Pelmo, Civetta, and Antelao.", "photo": f"{T}Rifugio_palmieri.jpg"},
    {"name": "Passo Pordoi", "lat": 46.4878, "lon": 11.8125, "desc": "Highest paved pass in the Dolomites at 2,239m. Gateway to the Sella Group. Cable car to Sass Pordoi. Giro d'Italia legend.", "photo": f"{T}Sella_group_with_Piz_Bo%C3%A8.jpg"},
    {"name": "Passo Gardena", "lat": 46.5333, "lon": 11.8083, "desc": "Pass at 2,121m connecting Val Gardena with Val Badia. Dramatic views of the Sella massif. Major Sella Ronda ski circuit point.", "photo": f"{T}Sella_group_with_Piz_Bo%C3%A8.jpg"},

    # ── CHURCHES & HISTORIC ──
    {"name": "Basilica Santi Filippo e Giacomo", "lat": 46.5374, "lon": 12.1364, "desc": "Baroque basilica in Cortina d'Ampezzo, built 1769-1775. Landmark 73m bell tower visible from across the valley. 3,078-pipe organ.", "photo": f"{T}Cortina_d%27Ampezzo_-_church.jpg"},
    {"name": "Chiesa di Santa Fosca", "lat": 46.4440, "lon": 12.0280, "desc": "13th-century Gothic-Alpine church in Selva di Cadore. Onion-dome bell tower, 15th-century frescoes. Oldest religious center in Val Fiorentina.", "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"},
    {"name": "Forte Tre Sassi", "lat": 46.5350, "lon": 11.9800, "desc": "Austro-Hungarian fortress built 1897-1901 at Passo Valparola. Now a WWI museum with 2,000+ artifacts including weapons and recreated trenches.", "photo": f"{T}Fort_Tre_Sassi_und_Averau_%28Valparolapass%29.jpg"},
    {"name": "Villaggio ENI (Borca di Cadore)", "lat": 46.4380, "lon": 12.2100, "desc": "Modernist holiday village designed by Gellner and Carlo Scarpa in the 1950s-60s. Remarkable mid-century architecture in the mountains.", "photo": f"{T}Monte_Antelao_6.jpg"},

    # ── VIA FERRATAS ──
    {"name": "Via Ferrata Averau", "lat": 46.5020, "lon": 12.0380, "desc": "Grade A/B via ferrata on Monte Averau (2,649m). 30-min equipped section. Summit views of all major Dolomite peaks.", "photo": f"{T}Rifugio-Nuvolau_2972_a.jpg"},
    {"name": "Via Ferrata Ra Gusela", "lat": 46.4945, "lon": 12.0523, "desc": "Easy Grade A via ferrata up the slender Ra Gusela needle (2,595m) above Passo Giau. Short but exposed, spectacular views.", "photo": f"{T}Ra_Gusela%2C_view_from_Passo_Giau.jpg"},
    {"name": "Via Ferrata degli Alleghesi", "lat": 46.3832, "lon": 12.0598, "desc": "Long demanding via ferrata to Monte Civetta summit (3,220m). One of the classic Dolomite ferratas, 6-8 hours.", "photo": f"{T}Monte_Civetta.jpg"},
    {"name": "Via Ferrata Strobel (Punta Anna)", "lat": 46.5430, "lon": 12.0700, "desc": "Classic via ferrata on Tofana di Mezzo. Grade C, exposed, with stunning views into the Cortina basin. 3-4 hours.", "photo": f"{T}Tofana.jpg"},

    # ── ADDITIONAL TOWNS & VILLAGES ──
    {"name": "Arabba", "lat": 46.4969, "lon": 11.8742, "desc": "Ladin village at 1,602m in the Fodom Valley. Major ski resort on the Sella Ronda circuit. Gateway to Marmolada and Passo Pordoi.", "photo": f"{T}Marmolada%2C_Italy.jpg"},
    {"name": "Alleghe", "lat": 46.4073, "lon": 12.0253, "desc": "Picturesque village at the foot of Civetta, beside a lake formed from a 1771 landslide. Cable car to Civetta hiking trails.", "photo": f"{T}Monte_Civetta.jpg"},
    {"name": "Agordo", "lat": 46.2820, "lon": 12.0361, "desc": "Elegant mountain town at 611m with arcaded streets. Historic HQ of Luxottica, the world's largest eyewear company.", "photo": f"{T}Am_Rifugio_Pramperet.JPG"},
    {"name": "La Villa (Alta Badia)", "lat": 46.5894, "lon": 11.9006, "desc": "Ladin village at 1,433m in Val Badia. Surrounded by Dolomite peaks. Home to the Gran Risa World Cup ski slope.", "photo": f"{T}Valparolapass.jpg"},
    {"name": "San Vito di Cadore", "lat": 46.4500, "lon": 12.2170, "desc": "Charming village at 1,011m south of Cortina beneath Monte Antelao. Quieter alternative base for the central Dolomites.", "photo": f"{T}Monte_Antelao_6.jpg"},
    {"name": "Pieve di Cadore", "lat": 46.4330, "lon": 12.3670, "desc": "Historic capital of Cadore at 878m. Birthplace of Renaissance painter Titian. Museum dedicated to the artist, medieval castle.", "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"},
    {"name": "Cibiana di Cadore", "lat": 46.3830, "lon": 12.2830, "desc": "The 'Village of Murals' — 50+ large frescoes on building facades depicting local trades and legends. Open-air art gallery since 1980.", "photo": f"{T}Monte_Rite.jpg"},

    # ── MUSEUMS ──
    {"name": "MMM Dolomites (Messner Museum)", "lat": 46.3844, "lon": 12.2581, "desc": "Reinhold Messner's 'Museum in the Clouds' at 2,181m in a restored WWI fort on Monte Rite. Dedicated to Dolomite geology.", "photo": f"{T}Monte_Rite.jpg"},
    {"name": "Museo Vittorino Cazzetta", "lat": 46.4420, "lon": 12.0350, "desc": "Museum in Selva di Cadore housing the 7,000-year-old 'Mondeval Man' burial and dinosaur footprints from the Dolomites.", "photo": f"{T}Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg"},

    # ── GEOLOGICAL / ARCHAEOLOGICAL ──
    {"name": "Mondeval Archaeological Site", "lat": 46.4600, "lon": 12.0800, "desc": "Mesolithic site at 2,150m where a 7,000-year-old hunter's burial was found in 1985. One of the most important prehistoric alpine sites.", "photo": f"{T}Rifugio_citta_di_fiume.JPG"},
    {"name": "Dinosaur Footprints (Lastoi de Formin)", "lat": 46.4740, "lon": 12.0960, "desc": "210-million-year-old dinosaur trackways preserved in dolomite rock on the Lastoi de Formin plateau. Visible from the trail.", "photo": f"{T}Croda_da_Lago_Lastoi_de_Formin.jpg"},

    # ── CABLE CARS ──
    {"name": "Sass Pordoi Cable Car", "lat": 46.4888, "lon": 11.8015, "desc": "Cable car ascending 700m in 4 minutes to the 2,950m Sass Pordoi plateau. Gateway to Piz Boè and the lunar Sella landscape.", "photo": f"{T}Sella_group_with_Piz_Bo%C3%A8.jpg"},
    {"name": "Alleghe-Piani di Pezzè Gondola", "lat": 46.4054, "lon": 12.0234, "desc": "Gondola from Alleghe to 1,470m. Gateway to Civetta ski area and summer trails toward Rifugio Coldai.", "photo": f"{T}Monte_Civetta.jpg"},
    {"name": "Faloria Cable Car (Cortina)", "lat": 46.5350, "lon": 12.1500, "desc": "Cable car from Cortina to 2,123m Rifugio Faloria. Panoramic views of Cortina basin, Tofane, Cristallo, and Sorapiss.", "photo": f"{T}Monte-Cristallo_Forcella-Staunies_3239a.jpg"},

    # ── TRAIL JUNCTIONS & MEADOWS ──
    {"name": "AV1-AV3 Junction (Forcella Lagazuoi)", "lat": 46.5250, "lon": 12.0050, "desc": "Where Alta Via 1 meets Alta Via 3 at 2,573m. Strategic crossroads of Dolomite high routes.", "photo": f"{T}Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"},
    {"name": "Alpe di Fanes Grande", "lat": 46.6100, "lon": 12.0200, "desc": "Broad alpine pasture at 2,100m. Setting of Ladin legends about the Kingdom of Fanes. Surrounded by pale dolomite towers.", "photo": f"{T}L%27ambiente_attorno_al_rifugio_Fanes.jpg"},
    {"name": "Armentara Meadows", "lat": 46.6200, "lon": 11.8800, "desc": "UNESCO-protected wildflower meadows near La Villa. Some of the most biodiverse alpine meadows in Europe. Stunning in June.", "photo": f"{T}Prato_Piazza.jpg"},
    {"name": "Pian de Loa Meadow", "lat": 46.5100, "lon": 12.0500, "desc": "Scenic alpine meadow between Cinque Torri and Passo Giau. Carpeted with wildflowers in summer, framed by Averau and Nuvolau.", "photo": f"{T}Ra_Gusela%2C_view_from_Passo_Giau.jpg"},
    {"name": "Val Corpassa", "lat": 46.3450, "lon": 12.0400, "desc": "Wild valley beneath Civetta's Torre Venezia and Torre Trieste. Alpine botanical garden near Rifugio Vazzoler. Remote and dramatic.", "photo": f"{T}IMG_0058_Rif._Mario_Vazzoler.JPG"},
]

star_map = {5: "★★★★★", 4: "★★★★☆", 3: "★★★☆☆", 2: "★★☆☆☆", 1: "★☆☆☆☆"}

def get_marker_color(r):
    if r["type"] == "city-hotel":
        return "#607D8B"
    rating = r["rating"]
    if rating == 5: return "#FFD700"
    elif rating == 4: return "#4CAF50"
    elif rating == 3: return "#2196F3"
    else: return "#9E9E9E"

def get_marker_size(r):
    if r["rating"] == 5: return 12
    elif r["rating"] == 4: return 10
    else: return 8

markers_js = ""
for r in rifugios:
    color = get_marker_color(r)
    size = get_marker_size(r)
    stars = star_map[r["rating"]]
    on_trail = "On AV1" if r["on_av1"] else "Off-trail / Detour"
    photo = r.get("photo", "")
    link_html = f'<a href=\\"{r["url"]}\\" target=\\"_blank\\" style=\\"color:#1a73e8;\\">Book / Website →</a>' if r["url"] else "Contact directly"

    img_html = f'<img src=\\"{photo}\\" style=\\"width:100%;height:160px;object-fit:cover;border-radius:8px 8px 0 0;margin:-14px -14px 10px -14px;width:calc(100% + 28px);\\" onerror=\\"this.parentElement.querySelector(&apos;img&apos;).style.display=&apos;none&apos;\\" />' if photo else ""

    popup = f"""<div style=\\"width:300px;font-family:system-ui,-apple-system,sans-serif;\\">{img_html}<h3 style=\\"margin:0 0 4px 0;font-size:16px;color:#1a1a1a;\\">{r['name']}</h3><div style=\\"font-size:18px;margin-bottom:6px;\\">{stars}</div><div style=\\"display:flex;gap:8px;margin-bottom:8px;flex-wrap:wrap;\\"><span style=\\"background:#e8f5e9;color:#2e7d32;padding:2px 8px;border-radius:12px;font-size:11px;\\">{r['elev']}</span><span style=\\"background:{'#fff3e0' if r['on_av1'] else '#fce4ec'};color:{'#e65100' if r['on_av1'] else '#c62828'};padding:2px 8px;border-radius:12px;font-size:11px;\\">{on_trail}</span><span style=\\"background:#e3f2fd;color:#1565c0;padding:2px 8px;border-radius:12px;font-size:11px;\\">{r['category']}</span></div><p style=\\"margin:0 0 8px 0;font-size:13px;color:#444;line-height:1.4;\\">{r['vibe']}</p><div style=\\"background:#f5f5f5;padding:8px;border-radius:6px;margin-bottom:8px;\\"><div style=\\"font-size:12px;color:#666;\\">Price (half-board pp/night)</div><div style=\\"font-size:14px;font-weight:600;color:#1a1a1a;\\">{r['price']}</div></div><div style=\\"text-align:center;\\">{link_html}</div></div>"""

    markers_js += f"""
        L.circleMarker([{r['lat']}, {r['lon']}], {{
            radius: {size}, fillColor: '{color}', color: '#fff', weight: 2, opacity: 1, fillOpacity: 0.9
        }}).addTo(map).bindPopup("{popup}", {{maxWidth: 320}});
    """

# Attraction markers
attractions_js = ""
for a in attractions:
    popup = f"""<div style=\\"width:300px;font-family:system-ui,-apple-system,sans-serif;\\"><img src=\\"{a['photo']}\\" style=\\"width:100%;height:160px;object-fit:cover;border-radius:8px 8px 0 0;margin:-14px -14px 10px -14px;width:calc(100% + 28px);\\" onerror=\\"this.style.display=&apos;none&apos;\\" /><h3 style=\\"margin:0 0 6px 0;font-size:16px;color:#1a1a1a;\\">{a['name']}</h3><span style=\\"background:#fff3e0;color:#e65100;padding:2px 8px;border-radius:12px;font-size:11px;\\">Attraction / Landmark</span><p style=\\"margin:8px 0 0 0;font-size:13px;color:#444;line-height:1.4;\\">{a['desc']}</p></div>"""

    attractions_js += f"""
        L.circleMarker([{a['lat']}, {a['lon']}], {{
            radius: 4, fillColor: '#FF6B35', color: '#fff', weight: 1, opacity: 1, fillOpacity: 0.85
        }}).addTo(map).bindPopup("{popup}", {{maxWidth: 320}});
    """

# Detour routes
detours = [
    {"name": "Tre Cime Circuit", "desc": "Iconic loop beneath the three towers. 2-3 hrs from Auronzo.", "coords": [[46.6095, 12.2938], [46.6140, 12.3020], [46.6189, 12.3097], [46.6230, 12.3000], [46.6095, 12.2938]], "color": "#FF6B35"},
    {"name": "Lago Federa / Croda da Lago Detour", "desc": "Stunning turquoise lake detour from Cortina side. 2-3 hr hike.", "coords": [[46.5010, 12.0420], [46.4980, 12.0600], [46.4950, 12.0780]], "color": "#2196F3"},
    {"name": "Tofane / Giussani Detour", "desc": "Via ferrata country. Dramatic Tofane peaks. Side trip from Falzarego.", "coords": [[46.5279, 12.0081], [46.5330, 12.0300], [46.5380, 12.0530]], "color": "#9C27B0"},
]

detours_js = ""
for d in detours:
    coords_str = json.dumps(d["coords"])
    detours_js += f"""
        L.polyline({coords_str}, {{color: '{d["color"]}', weight: 3, dashArray: '8, 8', opacity: 0.8}}).addTo(map).bindPopup('<div style="font-family:system-ui;"><b>{d["name"]}</b><br><span style="font-size:13px;color:#555;">{d["desc"]}</span></div>');
    """

trail_json = json.dumps(trail_coords)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alta Via 1 — Interactive Trail Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: system-ui, -apple-system, sans-serif; background: #1a1a2e; }}
        #map {{ width: 100%; height: 100vh; }}
        .info-panel {{
            position: absolute; top: 16px; left: 16px; z-index: 1000;
            background: rgba(26, 26, 46, 0.95); backdrop-filter: blur(10px);
            border-radius: 12px; padding: 20px; color: #fff; max-width: 340px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }}
        .info-panel h1 {{ font-size: 20px; margin-bottom: 4px; }}
        .info-panel .subtitle {{ font-size: 13px; color: #aaa; margin-bottom: 16px; }}
        .legend-item {{ display: flex; align-items: center; gap: 10px; margin-bottom: 8px; font-size: 13px; }}
        .legend-dot {{ width: 14px; height: 14px; border-radius: 50%; border: 2px solid #fff; flex-shrink: 0; }}
        .legend-line {{ width: 30px; height: 3px; flex-shrink: 0; border-radius: 2px; }}
        .legend-line.dashed {{ background: repeating-linear-gradient(90deg, var(--c) 0, var(--c) 6px, transparent 6px, transparent 12px); height: 3px; }}
        .stats {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 16px; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.1); }}
        .stat {{ text-align: center; }}
        .stat-val {{ font-size: 18px; font-weight: 700; color: #FFD700; }}
        .stat-label {{ font-size: 11px; color: #888; margin-top: 2px; }}
        .collapse-btn {{
            position: absolute; top: 8px; right: 12px; background: none; border: none;
            color: #888; font-size: 18px; cursor: pointer; padding: 4px;
        }}
        .collapse-btn:hover {{ color: #fff; }}
        .info-panel.collapsed {{ max-width: 180px; padding: 12px 16px; }}
        .info-panel.collapsed .collapsible {{ display: none; }}
    </style>
</head>
<body>
    <div id="map"></div>
    <div class="info-panel" id="infoPanel">
        <button class="collapse-btn" onclick="togglePanel()">−</button>
        <h1>Alta Via 1</h1>
        <div class="subtitle">Dolomites Hut-to-Hut Trail Map</div>
        <div class="collapsible">
            <div class="legend-item"><div class="legend-line" style="background:#E74C3C;"></div><span>Alta Via 1 Main Trail</span></div>
            <div class="legend-item"><div class="legend-line dashed" style="--c:#FF6B35;"></div><span>Detours & Side Trips</span></div>
            <div class="legend-item"><div class="legend-dot" style="background:#FFD700;"></div><span>★★★★★ Bucket List Rifugio</span></div>
            <div class="legend-item"><div class="legend-dot" style="background:#4CAF50;"></div><span>★★★★☆ Excellent Rifugio</span></div>
            <div class="legend-item"><div class="legend-dot" style="background:#2196F3;"></div><span>★★★☆☆ Solid Rifugio</span></div>
            <div class="legend-item"><div class="legend-dot" style="background:#9E9E9E;"></div><span>★★☆☆☆ Basic Rifugio</span></div>
            <div class="legend-item"><div class="legend-dot" style="background:#607D8B;"></div><span>City Hotels (pre/post)</span></div>
            <div class="legend-item"><div class="legend-dot" style="background:#FF6B35;"></div><span>Attractions & Landmarks</span></div>
            <div class="stats">
                <div class="stat"><div class="stat-val">119 km</div><div class="stat-label">Total Distance</div></div>
                <div class="stat"><div class="stat-val">7,350 m</div><div class="stat-label">Total Climbing</div></div>
                <div class="stat"><div class="stat-val">10-12</div><div class="stat-label">Days (comfortable)</div></div>
                <div class="stat"><div class="stat-val">100+</div><div class="stat-label">Attractions</div></div>
            </div>
        </div>
    </div>
    <script>
        const map = L.map('map', {{ center: [46.45, 12.08], zoom: 11, zoomControl: true }});
        L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{ attribution: 'Tiles &copy; Esri', maxZoom: 18 }}).addTo(map);
        L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/Reference/World_Transportation/MapServer/tile/{{z}}/{{y}}/{{x}}', {{ maxZoom: 18, opacity: 0.6 }}).addTo(map);
        L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{{z}}/{{y}}/{{x}}', {{ maxZoom: 18, opacity: 0.7 }}).addTo(map);
        const trailCoords = {trail_json};
        L.polyline(trailCoords, {{ color: '#ff0000', weight: 8, opacity: 0.25, lineCap: 'round', lineJoin: 'round' }}).addTo(map);
        L.polyline(trailCoords, {{ color: '#E74C3C', weight: 4, opacity: 0.9, lineCap: 'round', lineJoin: 'round' }}).addTo(map).bindPopup('<b>Alta Via 1</b><br>119 km — Lago di Braies to Belluno');
        L.marker([trailCoords[0][0], trailCoords[0][1]], {{ icon: L.divIcon({{ className: '', html: '<div style="background:#27ae60;color:#fff;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:700;white-space:nowrap;box-shadow:0 2px 8px rgba(0,0,0,0.3);border:2px solid #fff;">START — Lago di Braies</div>', iconAnchor: [80, 15] }}) }}).addTo(map);
        L.marker([trailCoords[trailCoords.length-1][0], trailCoords[trailCoords.length-1][1]], {{ icon: L.divIcon({{ className: '', html: '<div style="background:#c0392b;color:#fff;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:700;white-space:nowrap;box-shadow:0 2px 8px rgba(0,0,0,0.3);border:2px solid #fff;">FINISH — Belluno</div>', iconAnchor: [60, 15] }}) }}).addTo(map);
        {detours_js}
        {markers_js}
        {attractions_js}
        function togglePanel() {{
            const panel = document.getElementById('infoPanel');
            const btn = panel.querySelector('.collapse-btn');
            panel.classList.toggle('collapsed');
            btn.textContent = panel.classList.contains('collapsed') ? '+' : '−';
        }}
    </script>
</body>
</html>"""

output_path = r"c:\Users\DanPeterson\Dans Projects\Dolomites_Itinerary\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

# Also write to the named file
import shutil
shutil.copy(output_path, r"c:\Users\DanPeterson\Dans Projects\Dolomites_Itinerary\Alta_Via_1_Interactive_Map.html")

print(f"Map saved to {output_path}")
print("Also copied to Alta_Via_1_Interactive_Map.html")
