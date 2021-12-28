# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    On y retrouve la structure des classes associées aux corpus ainsi que leurs méthodes.
"""

# ==== MODULES ====

from classes_articles.classesArticles import Article, ArticleMediastack, ArticleNewsData
import pandas


# ==== CLASSES ====

class Corpus:
    """ Ensemble d'articles
    
    Attributs
    ----------
    nom : str
        Nom du corpus
    id_articles : dict
        Dictionnaire des articles. A chaque article est associé un numéro
    nombres_articles : int
        Nombre d'articles dans le corpus
    nombre_articles_par_source : pandas.DataFrame
        Data-frame en deux colonnes représentant l'ensemble des nombres d'articles pour chaque source détectée
    vocabulaire_duplicatas : list
        Liste de mots présents dans le corpus (avec possibilité de doublons)
    vocabulaire_unique : set
        Ensemble des mots dans le corpus (sans doublons)
    
    Retour
    ------
    Aucun
    """
    
    def __init__(self, nom):
        """ Constructeur d'un corpus
        
        Paramètres
        ----------
        nom : str
            Nom du corpus
        """
        self.nom = nom
        self.id_articles = {}
        self.nombre_articles = 0
        self.nombre_articles_par_source = pandas.DataFrame(columns = ['source', 'nombre_articles'])
        self.vocabulaire_duplicatas = list()
        self.vocabulaire_unique = set() 
        
    def ajouter_article(self, *articles):
        """ Ajout d'un ou plusieurs articles dans le corpus
        
        Paramètres
        ----------
        *args :
            Article ou ensemble d'articles à ajouter au corpus
            
        Retour
        ------
        Aucun
        """
        for article in articles:
           self.nombre_articles += 1
           self.id_articles[self.nombre_articles] = article
           print("Article n° {} ajouté au corpus {}.".format(self.nombre_articles, self.nom))
           # Mise à jour du vocabulaire avec duplicatas
           self.maj_vocabulaire_duplicatas(self.nombre_articles)
           # Mise à jour du dataframe
           self.maj_articles_par_source(self.nombre_articles)
        # Mise à jour du vocabulaire sans doublons
        self.set_vocabulaire_unique()
        
        
    def maj_articles_par_source(self, cle_nouvel_article):
        """ Mise à jour du nombre d'article par source suite à l'ajout d'un article dans le corpus
        
        Paramètres
        ----------
        cle_nouvel_article :
            Clé du nouvel article dont on veut récupérer la source
            
        Retour
        ------
        Aucun
        """
        source_a_ajouter = self.id_articles[cle_nouvel_article].get_source()
        # Si l'article possède bien une source
        if (source_a_ajouter != None):
            # Si la source n'existe pas dans nombre_articles_par_source, on l'ajoute à ce dernier
            if (len(self.nombre_articles_par_source[self.nombre_articles_par_source.source == source_a_ajouter]) < 1):
                self.nombre_articles_par_source = self.nombre_articles_par_source.append({'source' : source_a_ajouter,
                                                                                          'nombre_articles' : 1},
                                                                                         ignore_index = True)
            # Sinon, on met uniquement à jour le nombre d'article pour la dite source
            else:
                self.nombre_articles_par_source[self.nombre_articles_par_source.source == source_a_ajouter].nombre_articles += 1
        # Si l'article ne possède pas de source, on affiche un message d'erreur
        else:
            print("Erreur : l'article n° {cle_nouvel_article} ne possède pas de source.")
            
    def maj_vocabulaire_duplicatas(self, cles_nouveaux_articles):
        """ Mise à jour du vocabulaire avec duplicats
        
        Paramètres
        ----------
        *cles_nouveaux_articles : int ou list(int)
            Clé ou liste de clés des articles dont on veut ajouter les mots au vocabulaire avec duplicatas
            
        Retour
        ------
        Aucun
        """
        if(type(cles_nouveaux_articles) is not list):
            article = self.id_articles[cles_nouveaux_articles]
            self.vocabulaire_duplicatas += article.liste_mots
        else:
            for cle_article in cles_nouveaux_articles:
                article = self.id_articles[cle_article]
                self.vocabulaire_duplicatas += article.liste_mots
        
    
    def set_vocabulaire_unique(self):
        """ Mise à jour du vocabulaire sans duplicatas
        
        Paramètres
        ----------
        Aucun
            
        Retour
        ------
        Aucun
        """
        # Si le vocabulaire avec duplicatas est vide, on le met à jour
        if(len(self.vocabulaire_duplicatas) < 1):
            self.maj_vocabulaire_duplicatas(list(range(1, self.nombre_articles+1)))
        self.vocabulaire_unique = set(self.vocabulaire_duplicatas)