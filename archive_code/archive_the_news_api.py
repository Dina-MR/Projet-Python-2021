# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 21:57:20 2021

@author: Dina
"""
# ==== LIBRARIES ====

import http.client
import urllib.parse
import json
from newsdataapi import NewsDataApiClient

# ==== THENEWSAPI ====

# Fonction

def extraction_thenews_api(parametres, encodage = None):
    """ Extraction des articles avec l'API TheNewsAPI
    
    Paramètres
    ----------
    parametres : dict
        Filtres pour la requête
    encodage : str
        Type d'encodage pour le décodage en chaîne de caractères du fichier JSON en bytes généré par la requête
        
    Retour
    ------
    Aucun
    """
    # Connexion
    connexion = http.client.HTTPSConnection('api.thenewsapi.com')
    # Authentification avec la clé API
    parametres_thenews_api = urllib.parse.urlencode(parametres)
    # Requête
    connexion.request('GET', '/v1/news/all?{}'.format(parametres_thenews_api))
    # Exécution
    resultats = connexion.getresponse()
    donnees = resultats.read()
    # Transformation des données au format JSON
    decodage = donnees.decode(encodage)
    donnees_json = json.loads(decodage)
    # Récupération de la liste des articles à partir de donnees_json['data']
    liste_articles = donnees_json['data']
    # Récupération des articles à partir de la liste d'articles
    for indice, article in enumerate(liste_articles):
        # A FAIRE PLUS TARD : INSTANCIER UN NOUVEAU DOCUMENT
        # EN ATTENDANT : AFFICHAGE DE QUELQUES PARAMETRES
        print("Article n° ", indice + 1)
        print("Titre :", article['title'])
        print("Mots-clé : ", article['keywords'])
        print("Publié le :", article['published_at'])
        print("Description :", article['description'])
    #return liste_articles
    
    
# Exécution

# Paramètres
CLE_API_THENEWS = 'phlj3cy0Zdym13xYRIltoI1a4J53RligMGzTgdir' 
CATEGORIES_THENEWS = 'general'
LIMIT_THENEWS = 5
LANGUE_THENEWS = 'en'
ENCODAGE_THENEWS = 'utf-8'

# Instanciation du dictionnaire de paramètres
parametres_thenews_api = {
    'api_token' : CLE_API_THENEWS,
    'categories' : CATEGORIES_THENEWS,
    'limit' : LIMIT_THENEWS,
    'language' : LANGUE_THENEWS
    }

# Exécution de la fonction
extraction_thenews_api(parametres_thenews_api, ENCODAGE_THENEWS)