def demander_mode_stockage():
    print("Où souhaitez-vous enregistrer les données ?")
    print("1 - Fichiers CSV (un récap par catégorie et par sous-catégorie)")
    print("2 - Base de données SQL")
    choix = input("Votre choix (1 ou 2) : ")
    return choix


def demander_mode_execution(categories):
    print("\nComment souhaitez-vous lancer le scraping ?")
    print("1 - Une seule sous-catégorie (recommandé pour tester sans risquer un blocage)")
    print("2 - Toutes les sous-catégories, avec une longue pause entre chacune")
    choix = input("Votre choix (1 ou 2) : ")

    if choix == "1":
        print("\nCatégories disponibles :")
        liste = []
        for categorie, sous_categories in categories.items():
            for sous_categorie in sous_categories:
                liste.append((categorie, sous_categorie))
                print(f"{len(liste)} - {categorie} / {sous_categorie}")

        num = int(input("Choisissez le numéro de la sous-catégorie à scraper : "))
        categorie, sous_categorie = liste[num - 1]
        return "une_seule", categorie, sous_categorie

    return "toutes", None, None


def afficher_debut_scraping(categorie, sous_categorie):
    print(f"\n--- Scraping : {categorie} / {sous_categorie} ---")


def afficher_resultat(nb_produits, categorie, sous_categorie):
    print(f"{nb_produits} produits trouvés pour {categorie} / {sous_categorie}")


def afficher_fin():
    print("\nScraping terminé.")


def afficher_pause(minutes):
    print(f"\n⏸  Pause de {minutes:.1f} minutes avant la prochaine sous-catégorie (pour éviter un blocage)...")