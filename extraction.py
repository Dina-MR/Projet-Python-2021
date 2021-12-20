# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ==== LIBRARIES ====

import http.client
import urllib.parse
import json


# ==== Variables globales ====

# Pour "parametres"
CLE_API = 'phlj3cy0Zdym13xYRIltoI1a4J53RligMGzTgdir' 
CATEGORIES = 'general'
LIMIT = 5
LANGUE = 'en'

# Pour l'affichage des données
ENCODAGE = 'utf-8'

# ==== Extraction via l'API TheNewsAPI ====

# Connexion
connexion = http.client.HTTPSConnection('api.thenewsapi.com')

# Authentification avec la clé API
parametres = urllib.parse.urlencode({
    'api_token' : CLE_API,
    'categories' : CATEGORIES,
    'limit' : LIMIT,
    'language' : LANGUE
    })

# Requête
connexion.request('GET', '/v1/news/all?{}'.format(parametres))

# Exécution
resultats = connexion.getresponse()
donnees = resultats.read()

# Affichage des résultat
print(donnees.decode(ENCODAGE))

# ==== STOCKAGE DES DONNEES AU FORMAT JSON ====

# Transformation des données au format JSON
decodage = donnees.decode(ENCODAGE)
donnees_json = json.loads(decodage)
#fichier_json = json.dumps(donnees_json, indent = 4, sort_keys = True)
#print(fichier_json)

# ==== RECUPERATION DES DONNEES ICI DU DICTIONNAIRE JSON ====

donnees_thenews = donnees_json['data']

# On obtient une liste d'articles, représentés par des dictionnaires
