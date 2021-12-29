# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    Ce script présente des fonctions liées à la gestion des corpus sous forme de fichier (sauvegarde et ouverture)
"""

# ==== LIBRAIRIES ====

from classesCorpus import Corpus
import pickle


# ==== METHODES ====

def sauvegarder_corpus(corpus, fichier, option = "wb"):
    """ Enregistrement d'un corpus
    
    Attributs
    ----------
    corpus : Corpus
        Corpus d'articles à sauvegarder
    fichier : str
        Nom du fichier dans lequel sera sauvergardé le corpus
    option : str
        Option d'ouverture du fichier
    
    Retour
    ------
    Aucun
    """
    with open(fichier, option) as f:
        pickle.dump(corpus, f)
        
def ouvrir_corpus(fichier_corpus, option = "rb"):
    """ Ouveture d'un corpus
    
    Attributs
    ----------
    fichier_corpus : str
        Nom du fichier dans lequel est stocké un corpus
    option : str
        Option d'ouverture du fichier
    
    Retour
    ------
    Corpus
    """
    with open(fichier_corpus, option) as f:
        return pickle.load(f)