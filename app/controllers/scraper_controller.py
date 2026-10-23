import os
import time
import random
from bs4 import BeautifulSoup
from app.models.produit import Produit


def page_contient_captcha(soup):
    texte = soup.get_text().lower()
    indices = [
        "enter the characters you see",
        "captcha",
        "robot check",
        "saisissez les caractères",
        "automated access to amazon data",
        "api-services-support@amazon.com",
    ]
    return any(indice in texte for indice in indices)


def sauvegarder_debug(driver, soup, categorie, sous_categorie, page):
    os.makedirs("debug", exist_ok=True)
    nom_fichier = f"debug/{categorie}_{sous_categorie}_page{page}".replace(" ", "_")

    with open(f"{nom_fichier}.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    driver.save_screenshot(f"{nom_fichier}.png")
    print(f"Debug sauvegardé : {nom_fichier}.html / .png")


def scraper_sous_categorie(driver, url, categorie, sous_categorie, nb_pages=1):
    produits = []

    for page in range(1, nb_pages + 1):
        page_url = f"{url}&page={page}"
        driver.get(page_url)
        time.sleep(random.uniform(2.5, 5))

        soup = BeautifulSoup(driver.page_source, "html.parser")

        if page_contient_captcha(soup):
            print(f"\n⚠️  CAPTCHA détecté sur {categorie} / {sous_categorie} (page {page}).")
            print("Amazon a probablement repéré une activité automatisée.")
            input("Résous le CAPTCHA manuellement dans la fenêtre du navigateur, puis appuie sur Entrée pour continuer...")
            soup = BeautifulSoup(driver.page_source, "html.parser")

        # Supporte les deux formats de page : recherche classique (/s?k=...)
        # et page de catégorie (/b/?node=...)
        items = soup.select(
            "div[data-component-type='s-search-result'], div[data-cy='asin-faceout-container']"
        )

        if len(items) == 0:
            sauvegarder_debug(driver, soup, categorie, sous_categorie, page)

        for item in items:
            try:
                titre_elem = item.select_one("h2 span")
                titre = titre_elem.get_text(strip=True) if titre_elem else None
            except AttributeError:
                titre = None

            try:
                prix_elem = item.select_one("span.a-price > span.a-offscreen")
                prix = prix_elem.get_text(strip=True) if prix_elem else None
            except AttributeError:
                prix = None

            try:
                lien_elem = item.select_one("h2 a") or item.select_one("a.a-link-normal.s-no-outline")
                lien = "https://www.amazon.fr" + lien_elem["href"] if lien_elem else None
            except (AttributeError, TypeError):
                lien = None

            try:
                image_elem = item.select_one("img.s-image")
                image = image_elem["src"] if image_elem else None
            except (AttributeError, TypeError):
                image = None

            if titre:
                produits.append(Produit(titre, prix, lien, image, categorie, sous_categorie))

        time.sleep(random.uniform(1.5, 3.5))

    return produits