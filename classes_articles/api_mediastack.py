# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:13:22 2021
AUTHORS:
    
"""
#https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4463445-organisez-un-projet-en-modules
# Python 3

import http.client, urllib.parse
import json

list_articles=[]
cat_articles={}

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
        
    Retour
    ------
    Aucun
    """
    list_articles=[]
    cat_articles={}
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
    liste_articles_mediastack = data_json['data']
    for k,article in enumerate(liste_articles_mediastack):
        list_articles.append(('mediastack',article))
        
        
    
    return list_articles
   

# Exécution

''' exemple de filtre
categories=["general","busness","entertainment","health","science","sports","technology"]
sort=["published_desc","popularity"]
 languages: 'fr,-en',
 countries: 'ca,fr',
 keywords = 'virus,-corona' or 'Wall street -wolf'
 
'''

# appel de la fonction

my_key_mediastack="74713d7a61ca250397ba5e6b7b64b540"
CATEGORIES = '-general,health' 

liste_articles_mediastack=extraction_mediaStack(my_key_mediastack,category=CATEGORIES,limit_page=10)
print(liste_articles_mediastack)




## -----------création du corpus ----------------------------------

from classesArticles import Article, ArticleMediastack, ArticleNewsData
import datetime

import classesCorpus as  clc

# instancier l'objet corpusArticle
corpusArticle=clc.Corpus('mediastack')
#article_mediastack=Article()

# Ajout des article dans le corpus
for nature, article in enumerate(liste_articles_mediastack):
        # A FAIRE PLUS TARD : INSTANCIER UN NOUVEAU DOCUMENT
        if nature=="mediastack":
      
            idArticle={}
        
            #indice_i=indice+1
            
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
            date=article["published_at"]
            
            #date=datetime.datetime.strptime(article["published_at"],"%Y-%m-%dT%H:%M:%SZ").strftime("%Y/%m/%d")
            #date=datetime.datetime.strptime(date).strftime("%Y/%m/%d")
            
            # création  d'un l'objet d'article 
            article_mediastack=Article(titre,auteur,description,source,url,date,type="mediastack")
            
            corpusArticle.ajouter_article(article_mediastack)
            #collection.append(,article_mediastack)
            #collection.append(idArticle)





print(corpusArticle)
for i,v in enumerate(corpusArticle):
    print(f"i: {v}")
    
# construction des vocabulaires pour chaque corpus



'''

#ajout d'un article
import classesCorpus as  clc

corpusArticle=clc.Corpus('medaistack')

corpusArticle.ajouter_article(liste_articles_mediastack)
 
'''






