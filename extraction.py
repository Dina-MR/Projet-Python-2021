# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    Il permet d'extraire les articles à l'aide de différentes API
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



# ==== NEWSDATA.IO ====

# Fonction 

def extraction_news_data_api(cle_api, mot_cle =  None, pays = None, langue = None, categorie = None):
    """ Extraction des articles avec l'API NewsData.io
    
    Paramètres
    ----------
    cle_api : str
        Clé API du membre du binôme possédant un compte chez NewsData.io
    mot_cle : str
        Mot-clés utilisés pour la recherche d'articles
    pays : str
        Pays d'origine des articles à trouver
    langue : str
        Langue(s) choisie(s) pour les articles désirés
    categorie : str
        Catégorie(s) désirée(s) des articles à extraire
        
    Retour
    ------
    Aucun
    """
    # Authentification
    api_newsdata = NewsDataApiClient(apikey = cle_api)
    # Construction de la requête à partir de filtres de recherche
    requete_news_data = api_newsdata.news_api(q = mot_cle, country = pays, language = langue, category = categorie)
    # Récupération de la liste des articles
    liste_articles = requete_news_data['results']
    # Récupération des articles à partir de la liste d'articles
    for indice, article in enumerate(liste_articles):
        # A FAIRE PLUS TARD : INSTANCIER UN NOUVEAU DOCUMENT
        # EN ATTENDANT : AFFICHAGE DE QUELQUES PARAMETRES
        print("Article n° ", indice + 1)
        print("Titre :", article['title'])
        print("Mots-clé : ", article['keywords'])
        print("Publié le :", article['pubDate'])
        print("Description :", article['description'])
    #return liste_articles

# Exécution 

# Paramètres
CLE_API_NEWSDATA = 'pub_2998ef8f3cbeb3b8f1a3f91cc9d812b4f950'
PAYS_NEWSDATA = "fr, us"
LANGUES_NEWSDATA = "en, fr"
MOTS_CLES_NEWSDATA = "pizza"
CATEGORIES_NEWSDATA = "world"
# Appel de la fonction
extraction_news_data_api(cle_api = CLE_API_NEWSDATA, langue = LANGUES_NEWSDATA)