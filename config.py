from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    return webdriver.Chrome(options=options)


# Structure : Catégorie -> Sous-catégorie -> URL de recherche Amazon
CATEGORIES = {
    "Cuisine et maison": {
        "Décoration": "https://www.amazon.fr/gp/browse.html?node=57927031&ref_=nav_em__dec_0_2_16_12",
        "Meuble": "https://www.amazon.fr/gp/browse.html?node=194641031&ref_=nav_em__meubles_0_2_16_7",
    },
    "Jeux et Consoles": {
        "Consoles rétro": "https://www.amazon.fr/gp/browse.html?node=26864502031&ref_=nav_em_retroconsoles_0_2_12_12",
        "PC": "https://www.amazon.fr/gp/browse.html?node=548026&ref_=nav_em_pc_0_2_12_10",
    },
    "Livres": {
        "Ebooks Kindle": "https://www.amazon.fr/amz-books/store?node=695398031&ref_=dbs_ksf&storeType=browse&filters=v1%3AFORMAT%5Bkindle_edition%5D&ccs_id=01c6d5e1-0159-4f56-94f3-4ef0853e172a",
        "Manuels scolaires et parascolaire": "https://www.amazon.fr/gp/browse.html?node=301146&ref_=nav_em__scpr_0_2_10_7",
    },
}

DATA_DIR = "data"
NB_PAGES_PAR_SOUS_CATEGORIE = 1

PAUSE_MIN_ENTRE_SOUS_CATEGORIES = 180  # 3 minutes
PAUSE_MAX_ENTRE_SOUS_CATEGORIES = 300  # 5 minutes