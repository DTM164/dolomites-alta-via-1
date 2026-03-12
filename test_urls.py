import urllib.request
import json
import sys

W = "https://upload.wikimedia.org/wikipedia/commons"

all_urls = {
    "Rifugio Auronzo": f"{W}/thumb/1/14/Rifugio_Auronzo_Tre_Cime_2.JPG/800px-Rifugio_Auronzo_Tre_Cime_2.JPG",
    "Rifugio Locatelli": f"{W}/thumb/b/b7/Tre_cime_-_rifugio_Locatelli.jpg/800px-Tre_cime_-_rifugio_Locatelli.jpg",
    "Hotel Prato Piazza": f"{W}/thumb/5/5a/Prato_Piazza.jpg/800px-Prato_Piazza.jpg",
    "Rifugio Biella": f"{W}/thumb/c/cc/Croda_del_Becco_and_Rifugio_Biella_202008.jpg/800px-Croda_del_Becco_and_Rifugio_Biella_202008.jpg",
    "Rifugio Sennes": f"{W}/thumb/0/07/Rifugio_Munt_Sennes_03.JPG/800px-Rifugio_Munt_Sennes_03.JPG",
    "Rifugio Fodara Vedla": f"{W}/thumb/a/a5/Rifugio_Fodara_Vedla.jpg/800px-Rifugio_Fodara_Vedla.jpg",
    "Rifugio Pederu": f"{W}/thumb/0/0e/Fodara_Vella_-_panoramio.jpg/800px-Fodara_Vella_-_panoramio.jpg",
    "Rifugio Lavarella": f"{W}/thumb/6/6d/L%27ambiente_attorno_al_rifugio_Fanes.jpg/800px-L%27ambiente_attorno_al_rifugio_Fanes.jpg",
    "Rifugio Scotoni": f"{W}/b/bf/Lagozoi_Scotoni_Hutte_%282040m%29_-_panoramio.jpg",
    "Rifugio Lagazuoi": f"{W}/thumb/0/09/Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg/800px-Rifugio_Lagazuoi%2C_Passo_Falzarego_BL%2C_Dolomiti%2C_Italia_by_Marco_Zaffignani.jpg",
    "Rifugio Col Gallina": f"{W}/f/ff/Passo_di_Falzarego.jpg",
    "Rifugio Giussani": f"{W}/thumb/e/e3/Rifugio_Camillo_Giussani.jpg/800px-Rifugio_Camillo_Giussani.jpg",
    "Rifugio Nuvolau": f"{W}/thumb/7/73/Rifugio-Nuvolau_2972_a.jpg/800px-Rifugio-Nuvolau_2972_a.jpg",
    "Rifugio Croda da Lago": f"{W}/d/df/Rifugio_palmieri.jpg",
    "Rifugio Fedare": f"{W}/thumb/8/81/Ra_Gusela%2C_view_from_Passo_Giau.jpg/800px-Ra_Gusela%2C_view_from_Passo_Giau.jpg",
    "Rifugio Citta di Fiume": f"{W}/thumb/1/14/Rifugio_citta_di_fiume.JPG/800px-Rifugio_citta_di_fiume.JPG",
    "Rifugio Coldai": f"{W}/thumb/6/61/Rifugio_Coldai.jpg/800px-Rifugio_Coldai.jpg",
    "Rifugio Tissi": f"{W}/thumb/4/40/Monte_Civetta.jpg/800px-Monte_Civetta.jpg",
    "Rifugio Vazzoler": f"{W}/thumb/9/9a/IMG_0058_Rif._Mario_Vazzoler.JPG/800px-IMG_0058_Rif._Mario_Vazzoler.JPG",
    "Rifugio Carestiato": f"{W}/thumb/4/40/Monte_Civetta.jpg/800px-Monte_Civetta.jpg",
    "Rifugio Sommariva": f"{W}/thumb/8/8e/Am_Rifugio_Pramperet.JPG/800px-Am_Rifugio_Pramperet.JPG",
    "Rifugio Pian de Fontana": f"{W}/thumb/8/8e/Am_Rifugio_Pramperet.JPG/800px-Am_Rifugio_Pramperet.JPG",
    "Rifugio Re Alberto": f"{W}/thumb/3/30/Torri_del_Vajolet%2C_rifugio_Re_Alberto.jpg/800px-Torri_del_Vajolet%2C_rifugio_Re_Alberto.jpg",
    "Ca Del Sole": f"{W}/thumb/b/b1/Canal_Grande_Chiesa_della_Salute_e_Dogana_dal_ponte_dell_Accademia.jpg/800px-Canal_Grande_Chiesa_della_Salute_e_Dogana_dal_ponte_dell_Accademia.jpg",
    "Hotel Toblacherhof": f"{W}/thumb/d/d3/Toblach_-_Dobbiaco.JPG/800px-Toblach_-_Dobbiaco.JPG",
    "Tenuta Contarini": f"{W}/thumb/a/a2/Bassano_del_Grappa_120508_01.jpg/800px-Bassano_del_Grappa_120508_01.jpg",
    "Tre Cime": f"{W}/thumb/4/46/Tre_Cime_di_Lavaredo_2012_2.jpg/800px-Tre_Cime_di_Lavaredo_2012_2.jpg",
    "Tofane": f"{W}/2/28/Tofana.jpg",
    "Monte Pelmo": f"{W}/thumb/8/8b/Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg/800px-Winter_sunset_on_Monte_Pelmo%2C_San_Vito_di_Cadore_-_Dolomiti%2C_Italy.jpg",
    "Monte Civetta": f"{W}/thumb/4/40/Monte_Civetta.jpg/800px-Monte_Civetta.jpg",
    "Marmolada": f"{W}/thumb/6/63/Marmolada%2C_Italy.jpg/800px-Marmolada%2C_Italy.jpg",
    "Croda del Becco": f"{W}/thumb/c/cc/Croda_del_Becco_and_Rifugio_Biella_202008.jpg/800px-Croda_del_Becco_and_Rifugio_Biella_202008.jpg",
    "Prato Piazza": f"{W}/thumb/5/5a/Prato_Piazza.jpg/800px-Prato_Piazza.jpg",
    "Gola di Fanes": f"{W}/thumb/9/9e/Gola_di_Fanes_2008.JPG/800px-Gola_di_Fanes_2008.JPG",
    "Lago di Braies": f"{W}/thumb/2/24/Pragser_Wildsee_-_Lago_di_Braies_04.jpg/800px-Pragser_Wildsee_-_Lago_di_Braies_04.jpg",
    "Passo di Falzarego": f"{W}/f/ff/Passo_di_Falzarego.jpg",
    "Ra Gusela": f"{W}/thumb/8/81/Ra_Gusela%2C_view_from_Passo_Giau.jpg/800px-Ra_Gusela%2C_view_from_Passo_Giau.jpg",
    "Rifugio Pramperet": f"{W}/thumb/8/8e/Am_Rifugio_Pramperet.JPG/800px-Am_Rifugio_Pramperet.JPG",
    "Lago di Sorapis": f"{W}/thumb/a/a2/Lago_di_Sorapis.jpg/800px-Lago_di_Sorapis.jpg",
    "Lago di Misurina": f"{W}/thumb/8/8f/Lago_di_misurina.jpg/800px-Lago_di_misurina.jpg",
    "Lago di Limides": f"{W}/thumb/7/7a/Dolomity_-_Lago_di_Limides_02.jpg/800px-Dolomity_-_Lago_di_Limides_02.jpg",
    "Valparolapass": f"{W}/thumb/3/3a/Valparolapass.jpg/800px-Valparolapass.jpg",
    "Lago d'Antorno": f"{W}/thumb/4/4e/Lago_d%27Antorno_e_Cadini_di_Misurina.jpg/800px-Lago_d%27Antorno_e_Cadini_di_Misurina.jpg",
    "Antelao Lago di Mosigo": f"{W}/thumb/c/c2/Antelao_Lago_di_Mosigo.jpg/800px-Antelao_Lago_di_Mosigo.jpg",
    "Monte Antelao": f"{W}/thumb/0/0d/Monte_Antelao_6.jpg/800px-Monte_Antelao_6.jpg",
    "Croda da Lago Lastoi": f"{W}/thumb/9/92/Croda_da_Lago_Lastoi_de_Formin.jpg/800px-Croda_da_Lago_Lastoi_de_Formin.jpg",
    "Fort Tre Sassi Averau": f"{W}/thumb/1/1e/Fort_Tre_Sassi_und_Averau_%28Valparolapass%29.jpg/800px-Fort_Tre_Sassi_und_Averau_%28Valparolapass%29.jpg",
    "Sass de Stria": f"{W}/thumb/e/e2/Sass_de_Stria_Falzarego_Lagazuoi.jpg/800px-Sass_de_Stria_Falzarego_Lagazuoi.jpg",
    "Col di Lana": f"{W}/thumb/a/a3/Ccol_di_Lana_Sief.jpg/800px-Ccol_di_Lana_Sief.jpg",
    "Sorapiss": f"{W}/thumb/b/b6/Sorapiss_von_Tondi_de_Faloria.jpg/800px-Sorapiss_von_Tondi_de_Faloria.jpg",
    "Monte Cristallo": f"{W}/thumb/0/06/Monte-Cristallo_Forcella-Staunies_3239a.jpg/800px-Monte-Cristallo_Forcella-Staunies_3239a.jpg",
    "Becco di Mezzodi": f"{W}/thumb/4/4e/Becco_di_Mezzod%C3%AC.jpg/800px-Becco_di_Mezzod%C3%AC.jpg",
    "Sella Piz Boe": f"{W}/thumb/3/3b/Sella_group_with_Piz_Bo%C3%A8.jpg/800px-Sella_group_with_Piz_Bo%C3%A8.jpg",
    "Monte Rite": f"{W}/thumb/f/f9/Monte_Rite.jpg/800px-Monte_Rite.jpg",
    "Belluno Dolomites NP": f"{W}/thumb/5/5d/National_Park_of_the_Belluno_Dolomites.jpg/800px-National_Park_of_the_Belluno_Dolomites.jpg",
    "Cortina church": f"{W}/thumb/0/0e/Cortina_d%27Ampezzo_-_church.jpg/800px-Cortina_d%27Ampezzo_-_church.jpg",
    "Arabba": f"{W}/thumb/6/6e/Arabba_-_Livinallongo_del_Col_di_Lana.jpg/800px-Arabba_-_Livinallongo_del_Col_di_Lana.jpg",
    "Fodara Vedla": f"{W}/thumb/a/a5/Rifugio_Fodara_Vedla.jpg/800px-Rifugio_Fodara_Vedla.jpg",
    "Rifugio Palmieri": f"{W}/d/df/Rifugio_palmieri.jpg",
}

ok = 0
fail = 0
fails = []
for name, url in all_urls.items():
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        status = resp.getcode()
        if status == 200:
            ok += 1
            print(f"  OK  {name}")
        else:
            fail += 1
            fails.append((name, url, status))
            print(f"FAIL  {name} -> {status}")
    except Exception as e:
        fail += 1
        fails.append((name, url, str(e)))
        print(f"FAIL  {name} -> {e}")

print(f"\n=== RESULTS: {ok} OK, {fail} FAILED ===")
for name, url, err in fails:
    print(f"  BROKEN: {name}")
    print(f"    URL: {url}")
    print(f"    Error: {err}")
