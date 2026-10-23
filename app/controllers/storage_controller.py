import os
from app.models.storage_model import save_csv, save_sql, init_sql

DB_PATH = "data/produits.db"


def enregistrer_sous_categorie(produits, categorie, sous_categorie, choix, data_dir):
    if choix == "1":
        filepath = os.path.join(data_dir, categorie, sous_categorie, "recap.csv")
        save_csv(produits, filepath)
    elif choix == "2":
        init_sql(DB_PATH)
        save_sql(produits, DB_PATH)


def enregistrer_recap_categorie(tous_produits_categorie, categorie, choix, data_dir):
    if choix == "1":
        filepath = os.path.join(data_dir, categorie, "recap.csv")
        save_csv(tous_produits_categorie, filepath)
    # Pour le choix SQL, tout est déjà dans la même table, pas besoin de recap séparé