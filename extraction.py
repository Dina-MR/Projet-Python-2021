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

from newsdataapi import NewsDataApiClient
from classes_articles.classesArticles import Article, ArticleMediastack, ArticleNewsData


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
    nouveaux_articles : list
        Liste d'articles de type "ArticleNewsData"
    """
    # Liste de nouveaux articles :
    nouveaux_articles = list()
    # Authentification
    api_newsdata = NewsDataApiClient(apikey = cle_api)
    # Construction de la requête à partir de filtres de recherche
    requete_news_data = api_newsdata.news_api(q = mot_cle, country = pays, language = langue, category = categorie)
    # Récupération de la liste des articles
    liste_articles = requete_news_data['results']
    # Récupération des articles à partir de la liste d'articles
    for indice, article in enumerate(liste_articles):
        # Récupération des attributs de l'article
        titre = article['title']
        auteur = article['creator']
        description = article['description']
        source = article['source_id']
        url = article['link']
        date = article['pubDate']
        mots_cles = article['keywords']
        date = article['pubDate']
        contenu = article['content']
        url_video = article['video_url']
        # Instanciation du nouvel article en tant qu'objet de type "ArticleNewsData"
        nouvel_article = ArticleNewsData(titre, auteur, description, source, url, date, contenu, mots_cles, url_video)
        # Ajout de l'article à la liste des nouveaux articles
        nouveaux_articles.append(nouvel_article)
    return nouveaux_articles