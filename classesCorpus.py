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
        
    def ajouter_article(self, *args):
        """ Ajout d'un ou plusieurs articles dans le corpus
        
        Paramètres
        ----------
        *args :
            Article ou ensemble d'articles à ajouter au corpus
            
        Retour
        ------
        Aucun
        """
        for article in args:
           self.nombre_articles += 1
           self.id_articles[self.nombre_articles] = article
           self.maj_articles_par_source(self.nombre_articles)
        
        
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
                                                                                          'nombre_articles' : 1})
            # Sinon, on met uniquement à jour le nombre d'article pour la dite source
            else:
                self.nombre_articles_par_source[self.nombre_articles_par_source.source == source_a_ajouter].nombre_articles += 1
        # Si l'article ne possède pas de source, on affiche un message d'erreur
        else:
            print("Erreur : l'article n° {cle_nouvel_article} ne possède pas de source.")