# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    On y retrouve des méthodes permettant d'effectuer des comparaisons simples de corpus
"""

# ==== LIBRAIRIES ====

from classesCorpus import Corpus
import pandas


# ==== FONCTIONS ====

def meilleur_score_okapi_bm25(corpus_1, corpus_2):
    """ Détermination du corpus ayant le meilleur score OKAPI BM25
    
    Paramètres
    ----------
    corpus_1 : Corpus
        1er corpus
        
    corpus_2 : Corpus 
        2nd corpus
        
    Retour
    ------
    string
        Nom du corpus ayant le meilleur score
    """
    if(corpus_1.score_okapi_bm25 > corpus_2.score_okapi_bm25):
        return corpus_1.nom
    elif(corpus_1.score_okapi_bm25 < corpus_2.score_okapi_bm25):
        return corpus_2.nom
    else:
        return "Egalité"
    
    
def mots_communs_liste(corpus_1, corpus_2):
    """ Liste des mots présents dans les deux corpus
    
    Paramètres
    ----------
    corpus_1 : Corpus
        1er corpus
        
    corpus_2 : Corpus 
        2nd corpus
        
    Retour
    ------
    list
    """
    print("Récupération des mots communs entre " + corpus_1.nom + " et " + corpus_2.nom + "...")
    return corpus_1.vocabulaire_unique.intersection(corpus_2.vocabulaire_unique)


def mots_communs_dataframe(corpus_1, corpus_2):
    """ Data-frame des mots communs entre deux corpus, avec indication de l'occurrence pour chaque mot
    
    Paramètres
    ----------
    corpus_1 : Corpus
        1er corpus
        
    corpus_2 : Corpus 
        2nd corpus
        
    Retour
    ------
    pandas.DataFrame
    """
    liste_mots_communs = mots_communs_liste(corpus_1, corpus_2)
    print("Formatage des mots communs entre " + corpus_1.nom + " et " + corpus_2.nom + " sous forme de data-frame...")
    dataframe_mots_communs = pandas.DataFrame(columns = ["Mot", "Occurrences"])
    for mot in liste_mots_communs:
        dataframe_mots_communs = dataframe_mots_communs.append({"Mot" : mot,
                                       "Occurrences" : corpus_1.get_effectif_mot(mot) + corpus_2.get_effectif_mot(mot)
                                       },ignore_index = True)
    dataframe_mots_communs = dataframe_mots_communs.sort_values(by = 'Occurrences', ascending = False)
    return dataframe_mots_communs


def mots_exclusifs_liste(corpus_principal, corpus_secondaire):
    """ Liste des mots exclusifs à un corpus en comparaison à un autre
    
    Paramètres
    ----------
    corpus_principal : Corpus
        Corpus dont on veut récupérer les mots exclusifs
        
    corpus_secondaire : Corpus 
        Corpus de comparaison
        
    Retour
    ------
    list
    """
    print("Récupération des mots exclusifs au corpus " + corpus_principal.nom + "...")
    return corpus_principal.vocabulaire_unique.difference(corpus_secondaire.vocabulaire_unique)


def mots_exclusifs_dataframe(corpus_principal, corpus_secondaire):
    """ Data-frame des mots exclusifs à un corpus
    
    Paramètres
    ----------
    corpus_principal : Corpus
        Corpus dont on veut récupérer les mots exclusifs
        
    corpus_secondaire : Corpus 
        Corpus de comparaison
        
    Retour
    ------
    pandas.DataFrame
    """
    liste_mots_exclusifs = mots_exclusifs_liste(corpus_principal, corpus_secondaire)
    print("Formatage des mots exclusifs au corpus " + corpus_principal.nom + " sous forme de data-frame...")
    dataframe_mots_exclusifs = pandas.DataFrame(columns = ["Mot", "Occurrences"])
    for mot in liste_mots_exclusifs:
        dataframe_mots_exclusifs = dataframe_mots_exclusifs.append({"Mot" : mot,
                                       "Occurrences" : corpus_principal.get_effectif_mot(mot)
                                       },ignore_index = True)
    dataframe_mots_exclusifs = dataframe_mots_exclusifs.sort_values(by = 'Occurrences', ascending = False)
    return dataframe_mots_exclusifs
