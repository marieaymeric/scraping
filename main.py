import time
import random

from config import (
    get_driver,
    CATEGORIES,
    DATA_DIR,
    NB_PAGES_PAR_SOUS_CATEGORIE,
    PAUSE_MIN_ENTRE_SOUS_CATEGORIES,
    PAUSE_MAX_ENTRE_SOUS_CATEGORIES,
)
from app.views.console_view import (
    demander_mode_stockage,
    demander_mode_execution,
    afficher_debut_scraping,
    afficher_resultat,
    afficher_fin,
    afficher_pause,
)
from app.controllers.scraper_controller import scraper_sous_categorie
from app.controllers.storage_controller import (
    enregistrer_sous_categorie,
    enregistrer_recap_categorie,
)


def traiter_sous_categorie(driver, categorie, sous_categorie, url, choix_stockage):
    afficher_debut_scraping(categorie, sous_categorie)

    produits = scraper_sous_categorie(
        driver, url, categorie, sous_categorie,
        nb_pages=NB_PAGES_PAR_SOUS_CATEGORIE
    )

    afficher_resultat(len(produits), categorie, sous_categorie)
    enregistrer_sous_categorie(produits, categorie, sous_categorie, choix_stockage, DATA_DIR)
    return produits


def main():
    choix_stockage = demander_mode_stockage()
    mode, categorie_choisie, sous_categorie_choisie = demander_mode_execution(CATEGORIES)

    driver = get_driver(headless=False)

    try:
        if mode == "une_seule":
            url = CATEGORIES[categorie_choisie][sous_categorie_choisie]
            produits = traiter_sous_categorie(
                driver, categorie_choisie, sous_categorie_choisie, url, choix_stockage
            )
            enregistrer_recap_categorie(produits, categorie_choisie, choix_stockage, DATA_DIR)

        else:
            premiere = True
            for categorie, sous_categories in CATEGORIES.items():
                produits_categorie = []

                for sous_categorie, url in sous_categories.items():
                    if not premiere:
                        pause = random.uniform(
                            PAUSE_MIN_ENTRE_SOUS_CATEGORIES,
                            PAUSE_MAX_ENTRE_SOUS_CATEGORIES
                        )
                        afficher_pause(pause / 60)
                        time.sleep(pause)

                    premiere = False

                    produits = traiter_sous_categorie(
                        driver, categorie, sous_categorie, url, choix_stockage
                    )
                    produits_categorie.extend(produits)

                enregistrer_recap_categorie(produits_categorie, categorie, choix_stockage, DATA_DIR)

    finally:
        driver.quit()

    afficher_fin()


if __name__ == "__main__":
    main()