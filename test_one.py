import urllib.request

urls_to_test = [
    ("Lago di Braies", "https://commons.wikimedia.org/w/thumb.php?w=600&f=Pragser_Wildsee_-_Lago_di_Braies_04.jpg"),
    ("Tre Cime", "https://commons.wikimedia.org/w/thumb.php?w=600&f=Tre_Cime_di_Lavaredo_2012_2.jpg"),
    ("Rifugio Nuvolau", "https://commons.wikimedia.org/w/thumb.php?w=600&f=Rifugio-Nuvolau_2972_a.jpg"),
    ("Monte Civetta", "https://commons.wikimedia.org/w/thumb.php?w=600&f=Monte_Civetta.jpg"),
    ("Rifugio Lagazuoi", "https://commons.wikimedia.org/w/thumb.php?w=600&f=Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg"),
]

for name, url in urls_to_test:
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        ct = resp.headers.get('Content-Type', 'unknown')
        print(f"  OK  {name} -> {resp.getcode()} ({ct})")
    except Exception as e:
        print(f"FAIL  {name} -> {e}")
