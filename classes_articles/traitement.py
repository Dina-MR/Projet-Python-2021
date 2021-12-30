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


def supprimer_mots_vides(mots_initiaux):
    """ Suppression des mots "vides" (inutiles) dans une liste de mots
    
    Attributs
    ----------
    mots_initiaux : list
        Liste de mots, contenant potentiellement des mots inutiles
    
    Retour
    ------
    mots_conserves : list
        Liste des mots contenus dans mots_initiaux, sans les mots inutiles
    """
    mots_conserves = [mot for mot in mots_initiaux if mot not in MOTS_VIDES]
    return mots_conserves