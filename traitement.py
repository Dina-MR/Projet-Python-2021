# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    Ce script présente une fonction permettant de nettoyer le contenu de textes
"""

# ==== LIBRAIRIE ====

import string
import re


# ==== METHODE ====

def nettoyer_texte(texte):
    """ Nettoyage d'un texte
    
    Attributs
    ----------
    texte : str
        Texte auquel plusieurs traitements sont appliqués
    
    Retour
    ------
    texte_propre : str
        Version nettoyée du texte
    """
    texte_propre = texte
    # Mise en minuscule
    texte_propre = texte_propre.lower()
    # Suppression des ponctuations
    texte_propre = texte_propre.translate(str.maketrans("", "", string.punctuation))
    # Suppression des nombres (entiers, décimaux, positifs, négatifs...)
    texte_propre = re.sub(r"-?\b\d+(\.\d+)?\b", "", texte_propre)
    # Suppression des petits mots usuels (pronoms, déterminants, conjonctions de coordionation...)
    texte_propre = re.sub(r"\b[a-z]{1,4}\b", "", texte_propre)
    # Suppression des espaces en trop
    texte_propre = re.sub(" +", " ", texte_propre)
    return texte_propre

# ==== TEST ====
    
texte = "32, d2l ma 456bn 38784 -12378 26.9 9"
nettoyer_texte(texte)