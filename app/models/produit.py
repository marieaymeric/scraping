class Produit:
    def __init__(self, titre, prix, lien, image, categorie, sous_categorie):
        self.titre = titre
        self.prix = prix
        self.lien = lien
        self.image = image
        self.categorie = categorie
        self.sous_categorie = sous_categorie

    def to_dict(self):
        return {
            "titre": self.titre,
            "prix": self.prix,
            "lien": self.lien,
            "image": self.image,
            "categorie": self.categorie,
            "sous_categorie": self.sous_categorie,
        }