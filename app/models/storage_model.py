import os
import csv
import sqlite3


def save_csv(produits, filepath):
    if not produits:
        print(f"Aucun produit à enregistrer dans {filepath}")
        return

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=produits[0].to_dict().keys())
        writer.writeheader()
        for p in produits:
            writer.writerow(p.to_dict())
    print(f"{len(produits)} produits enregistrés dans {filepath}")


def init_sql(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT,
            prix TEXT,
            lien TEXT,
            image TEXT,
            categorie TEXT,
            sous_categorie TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_sql(produits, db_path):
    if not produits:
        return
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for p in produits:
        cur.execute(
            """INSERT INTO produits
               (titre, prix, lien, image, categorie, sous_categorie)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (p.titre, p.prix, p.lien, p.image, p.categorie, p.sous_categorie)
        )
    conn.commit()
    conn.close()
    print(f"{len(produits)} produits enregistrés dans {db_path}")