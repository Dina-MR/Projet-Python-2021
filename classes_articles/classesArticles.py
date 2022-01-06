# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:36:39 2021

@author: Lenovo
"""

# ==== LIBRAIRIES ====

import classes_articles.traitement as tt


# ==== CLASSES ====

class Article:
    """ Article de presse
    
    Attributs
    ----------
    titre : str
        Titre de l'article
    auteur : str
        Auteur de l'article
    description : str
        Description de l'article
    source : str
        Provenance de l'article
    url : str
        Lien URL permettant d'accéder à l'article
    date : str
        Date de publication de l'article
    type : str
        Type de l'article (Mediastack ou NewsData)
    liste_mots : set
        Ensemble des mots distincts contenus dans l'article
    """
    
    # Initialisation des variables de la classe mère
    def __init__(self, titre="", auteur="", description="",source="",url="",date="",type=""):
        self.titre = titre
        self.auteur = auteur
        self.description=description
        self.source=source
        self.url = url
        self.date = date
        self.type=type
        self.liste_mots = list()
     
# accesseurs
    def get_source(self):
        return self.source
    
# mutateur
    def set_liste_mots(self):
        """ Récupération des mots d'un article sous forme de liste, avec des traitements préalables
        
        Paramètres
        ----------
        Aucun
            
        Retour
        ------
        Aucun
        """
        texte_nettoye = tt.nettoyer_texte(self.description)
        liste_mots_temporaire = texte_nettoye.split()
        self.liste_mots += tt.supprimer_mots_vides(liste_mots_temporaire)
    
    
    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(Article)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDescription : {self.description}\Source : {self.source}\tURL : {self.url}\tDate : {self.date}\t"

    # Fonction qui renvoie le texte à afficher: str(Article)
    def __str__(self):
        return f"{self.titre}, écrit par  {self.auteur}"
    
    # Fonction qui renvoie l'article sous forme de dictionnaire
    def __asdict__(self):
        return {"Titre" : self.titre,
                "Auteur" : self.auteur,
                "Description" : self.description,
                "Source" : self.source,
                "Date de publication" : self.date
                }

    
# classe héritière d'articles "Mediastack"
class ArticleMediastack(Article):
    """ Article de presse extrait avec l'API Mediastack
    
    Attributs
    ----------
    categories : str
        Catégorie(s) dans laquelle/lesquelles se trouve l'article
    langue : str
        Langue de rédaction de l'article
    pays : str
        Pays d'origine où a été publié l'article
    """

    def __init__(self, titre="", auteur="", description="",source="",url="",date="",categories="",langue="",pays=""):
                 super().__init__(titre=titre,auteur=auteur,description=description,source=source,url=url,date=date,type="Mediastack")
                 self.categories=categories
                 self.langue=langue
                 self.pays=pays
                 self.set_liste_mots()

# accesseur
    def get_categories(self):
        return self.categories
    
    # mutateur
    def set_categories(self,categories):
        self.categories=categories
    
    #renvoie le texte à afficher: str(ArticleMediastack)
    #def __str__(self):
        #return f"Article Mediastack: {self.titre}, écrit par :{self.auteur} de catégorie: {self.categories}"
        #return {"source":"mediastack","titre":self.titre,"auteur":self.auteur,"categorie":self.categories,"date":self.date}
    def viewMediastack(self):
        return {"source":"mediastack","titre":self.titre,"auteur":self.auteur,"categorie":self.categories,"date":self.date}

    # Fonction qui renvoie un article Mediastack sous forme de dictionnaire
    def __asdict__(self):
        dictionnaire = super().__asdict__()
        dictionnaire["Langue"] = self.langue
        dictionnaire["Pays d'origine"] = self.pays
        return dictionnaire
    

# classe héritière  d'articles "NewsData"
class ArticleNewsData(Article):
    """ Article de presse extrait avec l'API NewsData
    
    Attributs
    ----------
    contenu : str
        Contenu détaillé de l'article
    mots_cles : list
        Liste des mots clés de l'article
    url_video : str
        Lien URL de la vidéo potentiellement associée à l'article
    """

    def __init__(self, titre="", auteur="", description="",source="",url="",date="",contenu="",mots_cles="",url_video=""):
                 super().__init__(titre=titre,auteur=auteur,description=description,source=source,url=url,date=date,type="NewsData")
                 self.contenu = contenu
                 self.mots_cles = mots_cles
                 self.url_video = url_video
                 self.set_liste_mots()

# accesseur
    def get_contenu(self):
        return self.contenu
    
    # mutateur
    def set_contenu(self,contenu):
        self.contenu=contenu
        
    def set_liste_mots(self):
        """ Récupération des mots d'un article sous forme de liste, avec des traitements préalables
        
        Paramètres
        ----------
        Aucun
            
        Retour
        ------
        Aucun
        """
        if(self.get_contenu() is not None):
            texte_nettoye = tt.nettoyer_texte(self.get_contenu())
        else:
            texte_nettoye = tt.nettoyer_texte(self.description)
        liste_mots_temporaire = texte_nettoye.split()
        self.liste_mots += tt.supprimer_mots_vides(liste_mots_temporaire)
        # Ajout des mots clés dans la liste des mots
        if(self.mots_cles is not None):
            self.liste_mots += self.mots_cles
    
   
    #renvoie le texte à afficher: str(ArticleNewsData)
    def __str__(self):
        return f"Article NewsData: {self.titre}, écrit par :{self.auteur} mots clés: {self.mots_cles}"
    
    # Fonction qui renvoie un article News Data sous forme de dictionnaire
    def __asdict__(self):
        dictionnaire = super().__asdict__()
        dictionnaire["Contenu"] = self.contenu
        return dictionnaire
    
    
    
    
    
    
    
   