# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:36:39 2021

@author: Lenovo
"""

# ==== LIBRAIRIES ====

import traitement as tt


# ==== CLASSES ====

class Article:
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
        self.set_liste_mots()
     
# accesseurs
    def get_source(self):
        return self.type
    
    def get_source(self):
        return self.source
    


    # Fonction qui renvoie le texte à afficher lorsqu'on tape repr(Article)
    def __repr__(self):
        return f"Titre : {self.titre}\tAuteur : {self.auteur}\tDescription : {self.description}\Source : {self.source}\tURL : {self.url}\tDate : {self.date}\t"

    #renvoie le texte à afficher: str(Article)
    def __str__(self):
        return f"{self.titre}, écrit par  {self.auteur}"
    
    
    
    
    # Fonction instanciant la liste de mots, avec au préalable un nettoyage du texte
    def set_liste_mots(self):
        texte_nettoye = tt.nettoyer_texte(self.description)
        self.liste_mots += texte_nettoye.split()
    
    
    
    
# classe héritière  d'articles "Mediastack"
class ArticleMediastack(Article):

    def __init__(self, titre="", auteur="", description="",source="",url="",date="",categories="",langue="",pays=""):
                 super().__init__(titre=titre,auteur=auteur,description=description,source=source,url=url,date=date,type="Mediastack")
                 self.categories=categories
                 self.langue=langue
                 self.pays=pays

# accesseur
    def get_categories(self):
        return self.categories
    
    # mutateur
    def set_categories(self,categories):
        self.categories=categories
    
    #renvoie le texte à afficher: str(ArticleMediastack)
    def __str__(self):
        return f"Article Mediastack: {self.titre}, écrit par :{self.auteur} de catégorie: {self.categories}"



# classe héritière  d'articles "NewsData"
class ArticleNewsData(Article):

    def __init__(self, titre="", auteur="", description="",source="",url="",date="",contenu="",mots_cles="",url_video=""):
                 super().__init__(titre=titre,auteur=auteur,description=description,source=source,url=url,date=date,type="NewsData")
                 self.contenu=contenu
                 self.mots_cles=mots_cles
                 self.url_video=url_video

# accesseur
    def get_contenu(self):
        return self.contenu
    
    # mutateur
    def set_contenu(self,contenu):
        self.contenu=contenu
    
   
    #renvoie le texte à afficher: str(ArticleNewsData)
    def __str__(self):
        return f"Article NewsData: {self.titre}, écrit par :{self.auteur} mots clés: {self.mots_cles}"
    
    
    
    
    
    
    
   