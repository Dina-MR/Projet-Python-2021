# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 14:13:22 2021

@author: Lenovo
"""
#https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4463445-organisez-un-projet-en-modules
# Python 3

import http.client, urllib.parse
import json

list_articles=[]
cat_articles={}

def extraction_mediaStack(params):
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
    # connexion au site
    conn = http.client.HTTPConnection('api.mediastack.com')
    
    # paramètres de connexion et du filtre
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
    
    # Récupération de la liste des articles
    # Récupération des articles à partir de la liste d'articles
    for indice, article in enumerate(liste_articles_mediastack):
        # A FAIRE PLUS TARD : INSTANCIER UN NOUVEAU DOCUMENT
        # EN ATTENDANT : AFFICHAGE DE QUELQUES PARAMETRES
        idArticle={}
        print(f"############### {indice+1}  #######################")
        indice_i=indice+1
        print("Article n° ", indice + 1)
        idArticle['titre']=article['title']
        print("Titre :", article['title'])
        
        idArticle['auteur']=article['author']
        print("Auteur : ", article['author'])
        
        idArticle['des']=article['description']
        print("Description :", article['description'])
        
        idArticle['url']=article['url']
        print("Url :", article['url'])
        
        idArticle['source']=article['source']
        print("Source :", article['source'])
        
        idArticle['img']=article['image']
        print("Url image :", article['image'])
        
        idArticle['categorie']= article['category']
        print("Categorie :", article['category'])
        
        idArticle['langue']= article['language']
        print("Langue :", article['language'])
        
        idArticle['pays']=article['country']
        print("Pays :", article['country'])
        
        idArticle['date']=article['published_at']
        print("Date publication :", article['published_at'])
        cat_articles[" indice_i"]=idArticle
    return list_articles.append(cat_articles)

# Exécution

''' exemple de filtre
categories=["general","busness","entertainment","health","science","sports","tehcnology"]
sort=["published_desc","popularity"]
 languages: 'fr,-en',
 countries: 'ca,fr',
 keywords = 'virus,-corona' or 'Wall street -wolf'
 
 '''    
# Paramètres
my_key_mediastack="74713d7a61ca250397ba5e6b7b64b540"
CATEGORIES = '-general,science'   #'-general,-sports'
LIMIT_mediastack = 20             # pagination max=100


# Instanciation du dictionnaire de paramètres
params ={
    'access_key': my_key_mediastack,
    'categories': CATEGORIES, 
    'sort': 'popularity',   #'published_desc'
    'limit': LIMIT_mediastack          
}



# appel de la fonction

extraction_mediaStack(params)

res=extraction_mediaStack(params)
print(res)

