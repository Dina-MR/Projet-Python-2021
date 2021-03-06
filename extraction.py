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
import http.client, urllib.parse
import json


# ==== METHODES ====

def extraction_news_data_api(cle_api, mot_cle =  None, pays = None, langue = None, categorie = None, limite_page = 10):
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
    limite_page : int
        Nombre maximum de pages dont on veut extraire les articles
        
    Retour
    ------
    nouveaux_articles : list
        Liste d'articles de type "ArticleNewsData"
    """
    print("Collection des articles avec l'API News Data en cours...")
    # Liste de nouveaux articles :
    nouveaux_articles = list()
    # Authentification
    api_newsdata = NewsDataApiClient(apikey = cle_api)
    # Boucle d'extraction d'articles
    for iteration in range(1, limite_page + 1):
        # Construction de la requête à partir de filtres de recherche
        requete_news_data = api_newsdata.news_api(q = mot_cle, country = pays, language = langue, category = categorie, page = iteration)
        # Récupération de la liste des articles
        liste_articles = requete_news_data['results']
        # Récupération des articles à partir de la liste d'articles
        for indice, article in enumerate(liste_articles):
            # Récupération des attributs de l'article
            titre = article['title']
            auteur = article['creator']
            # S'il n'y a aucun auteur, on laisse le champ "auteur" vide
            if(article['creator'] is None):
                auteur = ""
            # S'il n'y a qu'un seul créateur, on récupère l'unique élément de la liste
            elif(len(article['creator']) == 1):
                auteur = article['creator'][0]
            # S'il y en a plusieurs, on joint le nom des auteurs par des virgules
            else:
                auteur = ', '.join(article['creator'])
            description = article['description']
            # Si la description n'existe pas, on ne garde pas l'article
            if(description is None):
                continue
            source = article['source_id']
            url = article['link']
            mots_cles = article['keywords']
            # On ne récupère que le jour de publication, pas l'heure
            if(type(article['pubDate']) == str):
                date = article['pubDate'].split(" ")[0]
            else:
                date = ""
            contenu = article['content']
            url_video = article['video_url']
            # Instanciation du nouvel article en tant qu'objet de type "ArticleNewsData"
            nouvel_article = ArticleNewsData(titre, auteur, description, source, url, date, contenu, mots_cles, url_video)
            # Ajout de l'article à la liste des nouveaux articles
            nouveaux_articles.append(nouvel_article)
    print("Collection des articles avec l'API News Data terminée !")
    return nouveaux_articles


def extraction_mediaStack(my_key_mediastack,category=None,limit_page=5):
    """ Extraction des articles avec l'API mediaStack
    
    Paramètres
    ----------
    params: dict
           
    cle_api_mediastack : str
        Clé API obtenu en créant un compte chez mediastack
    sort: str
        trie les articles par date de publication récente
    categorie : str
        Catégorie(s) désirée(s) des articles à extraire
    limit: int
         pagination, max=100
         
  
    '''  -----exemple de filtre----------
    categories=["general","busness","entertainment","health","science","sports","technology"]
    sort=["published_desc","popularity"]
     languages: 'fr,-en',
     countries: 'ca,fr',
     keywords = 'virus,-corona' or 'Wall street -wolf'
     
        
    Retour
    ------
    list_articles_mediastack : list
    """
    print("Collection des articles avec l'API Mediastack en cours...")
    list_articles_mediastack=list()
  
    # connexion au site
    conn = http.client.HTTPConnection('api.mediastack.com')
    
    # paramètres de connexion et du filtre
    
    params ={
        'access_key': my_key_mediastack,
        'categories': category, 
        'sort': 'published_desc',   #'published_desc'
        #'sort': 'popularity',   #'published_desc'
        
        'languages': 'en',
        'limit': limit_page          
    }
    params = urllib.parse.urlencode(params)
   
    # recupération des articles
    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    #req=req.decode('utf-8')
    # Transformation des données au format JSON
    decodage = data.decode('utf-8')
    data_json = json.loads(decodage)
    # Récupération de la liste des articles à partir de donnees_json['data']
    liste_articles_mediastack = data_json["data"]
    for indice, article in enumerate(liste_articles_mediastack):
                
                titre=article['title']
                auteur=article['author']
                description=article['description']
                source=article['source']
                url=article['url']
              
                img=article['image']
                categorie= article['category']
                langue= article['language']
                pays=article['country']     # 2021-11-25T17:21:41+00:00
                #date=datetime.datetime.fromtimestamp(article.published_at).strftime("%Y/%m/%d")
                #date=article['published_at']
                #date=article["published_at"]
                date = article["published_at"]
                # On ne récupère que le jour de publication, pas l'heure
                if(date is not None):
                    date = date[0:10]
                    
                
                #date=datetime.datetime.strptime(article["published_at"],"%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
                #date=datetime.datetime.strptime(date).strftime("%Y/%m/%d")
                
                # création  d'un l'objet d'article 
                nouvel_article_mediastack=ArticleMediastack(titre,auteur,description,source,url,date,categorie,langue,pays)
                list_articles_mediastack.append(nouvel_article_mediastack)
        
    print("Collection des articles avec l'API Mediastack terminée !")
    return list_articles_mediastack