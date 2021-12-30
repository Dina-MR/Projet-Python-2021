# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    Il contient la fonction calculant le score OKAPI BM25 d'un corpus (considéré comme un gros document), ainsi que des petites fonctions utilitaires.
"""

# ==== MODULES ====

import math


# ==== FONCTIONS UTILITAIRES ====

def occurrence_multi_corpus(mot, corpus_1, corpus_2):
    """ Nombre de corpus dans lesquels est contenu un mot
    
    Paramètres
    ----------
    mot : string
        Mot recherché
    corpus_1 : Corpus
        Premier corpus
    corpus_2 : Corpus
        Second corpus
        
    Retour
    ------
    nombre_corpus : int
    """
    nombre_corpus = 0
    if list(corpus_1.vocabulaire_unique).count(mot) > 0:
        nombre_corpus += 1
    if list(corpus_2.vocabulaire_unique).count(mot) > 0:
        nombre_corpus += 1
    return nombre_corpus 
    
def frequence_mot_dans_corpus(mot, corpus):
    """ Frequence d'un mot dans un corpus donné
    
    Paramètres
    ----------
    mot : string
        Mot recherché
    corpus : Corpus
        Corpus contenant le mot
        
    Retour
    ------
    float
    """
    resultats_dataframe = corpus.stats.loc[corpus.stats['terme'] == mot, 'frequence_brute']
    if not resultats_dataframe.empty:
        return resultats_dataframe.item()
    return 0

def frequence_inversee_dans_corpus(mot, corpus, corpus_2):
    """ Frequence inversée d'un mot dans un corpus donné
    
    Paramètres
    ----------
    mot : string
        Mot recherché
    corpus : Corpus
        Corpus contenant le mot
    corpus_2 : Corpus
        Corpus de comparaison
        
    Retour
    ------
    float
    """
    n = occurrence_multi_corpus(mot, corpus, corpus_2)
    return math.log((2 - n + 0.5) / (n + 0.5))

def score_facteur_quotient(mot, corpus, corpus_2, k, b):
    """ Quotient constituant le 2nd facteur de la grande somme de la formule du score OKAPI BM25
    
    Paramètres
    ----------
    mot : string
        Mot recherché
    corpus : Corpus
        Corpus contenant le mot
    corpus_2 : Corpus
        Corpus de comparaison
    k : float
        Paramètre k de la formule finale
    b : float
        Paramètre b de la formule finale
        
    Retour
    ------
    float
    """
    # Nombre de mots uniques dans le corpus
    D = len(corpus.vocabulaire_unique)
    # Nombre moyen de mots entre les deux corpus
    avgdl = (D + len(corpus_2.vocabulaire_unique)) / 2
    numerateur = frequence_mot_dans_corpus(mot, corpus) * (k + 1)
    denominateur = frequence_mot_dans_corpus(mot, corpus) + k * (1 - b + b * D / avgdl)
    return numerateur / denominateur


# ==== FONCTION PRINCIPALE ====

def score(corpus, corpus_2, k, b = 0.75):
    """ Score complet basé sur la formule d'OKAPI BM25
    
    Paramètres
    ----------
    corpus : Corpus
        Corpus étudié
    corpus_2 : Corpus
        Corpus de comparaison
    k : float
        Paramètre k de la formule finale
    b : float
        Paramètre b de la formule finale
        
    Retour
    ------
    float
    """
    # Liste de mots des deux corpus
    liste_mots = list(corpus.vocabulaire_unique) + list(corpus_2.vocabulaire_unique)
    return sum(frequence_inversee_dans_corpus(mot, corpus, corpus_2) * score_facteur_quotient(mot, corpus, corpus_2, k, b)
               for mot in liste_mots)