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

import math


# ==== FONCTIONS ====
    
def frequence_brute(effectif, taille_liste_mots):
    """ Fréquence d'un mot dans une liste de mots
    
    Paramètres
    ----------
    effectif : int
        Occurrence d'un terme dans un corpus
    taille_liste_mots : int
        Taille de la liste de mots dans lequel se trouve supposément le mot associé à "effectif"
        
    Retour
    ------
    float
    """
    return effectif / taille_liste_mots

def frequence_normalisee_logarithmique(frequence_brute):
    """ Fréquence normalisée logarithmique d'un mot
    
    Paramètres
    ----------
    frequence_brute : float
        Fréquence d'un mot dans un corpus
        
    Retour
    ------
    float
    """
    return math.log(1 + frequence_brute)

def frequence_normalisee_max_demi(frequence_brute, frequence_brute_max):
    """ Fréquence normalisée "0,5" par le max d'un mot
    
    Paramètres
    ----------
    frequence_brute : float
        Fréquence d'un mot dans un corpus
    frequence_brute_max : float
        Fréquence du mot le plus présent dans un corpus
        
    Retour
    ------
    float
    """
    return 0.5 + 0.5 * frequence_brute / frequence_brute_max

def frequence_normalisee_max_k(frequence_brute, frequence_brute_max, k):
    """ Fréquence normalisée "0,5" par le max d'un mot
    
    Paramètres
    ----------
    frequence_brute : float
        Fréquence d'un mot dans un corpus
    frequence_brute_max : float
        Fréquence du mot le plus présent dans un corpus
    k : float
        Paramètre de la normalisation
        
    Retour
    ------
    float
    """
    return k + (1 - k) * frequence_brute / frequence_brute_max

def frequence_inverse_brute(effectif_brut):
    """ Fréquence normalisée logarithmique d'un mot
    
    Paramètres
    ----------
    effectif : int
        Occurrence d'un terme dans un corpus
        
    Retour
    ------
    float
    """
    if (frequence_brute != 0):
        return 1 / effectif_brut
    else:
        return 1 / (1 + effectif_brut)
    
def tf_idf(frequence, frequence_inverse):
    """ Fréquence normalisée logarithmique d'un mot
    
    Paramètres
    ----------
    frequence : float
        Fréquence d'un mot dans un corpus
    frequence_inverse : float
        Valeur inverse de la fréquence
        
    Retour
    ------
    float
    """
    return frequence * frequence_inverse
