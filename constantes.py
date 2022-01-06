# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    Il contient l'ensemble des valeurs constantes utilisées dans l'ensemble du projet
"""

# ==== LIBRAIRIES ====

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


# ==== POUR L'EXTRACTION ====

# Paramètres de l'API Mediastack
my_key_mediastack="74713d7a61ca250397ba5e6b7b64b540"
CATEGORIES = '-general,health' 

# Paramètres de l'API NewsData 
CLE_API_NEWSDATA = 'pub_2998ef8f3cbeb3b8f1a3f91cc9d812b4f950'
PAYS_NEWSDATA = "fr, us"
LANGUES_NEWSDATA = "en, fr"
MOTS_CLES_NEWSDATA = "pizza"
CATEGORIES_NEWSDATA = "world"


# ==== POUR LA SAUVEGARDE DES CORPUS DANS DES FICHIER PKL ====

PATH_NEWS_DATA = "sauvegardes/news_data.pkl"
PATH_MEDIASTACK = "sauvegardes/mediastack.pkl"


# ==== POUR LE NETTOYAGE DE TEXTE ====

# Liste des mots vides
MOTS_VIDES = stopwords.words()


# ==== POUR L'APPLICATION ====

# Lien du thème CSS
THEME = "https://bootswatch.com/5/litera/bootstrap.min.css"

# Style des lignes bootstrap
STYLE_ROW = {'marginBottom' : 50}
# Style des images
STYLE_IMAGE = {'width' : '100%', 'height' : 'auto'}

# Sélection des catégories
SELECTION_CATEGORIES = [
    {'label' : 'Business', 'value' : 'business'},
    {'label' : 'Divertissement', 'value' : 'entertainment'},
    {'label' : 'Santé', 'value' : 'health'},
    {'label' : 'Science', 'value' : 'science'},
    {'label' : 'Sport', 'value' : 'sports'},
    {'label' : 'Technologie', 'value' : 'technology'}
]

# Couleur associées aux corpus
COULEUR_NEWS_DATA = "#ffa630"
COULEUR_MEDIASTACK = "#00a7e1"

# Nom des fichiers pour les nuages de mot
NUAGE_NEWS_DATA = "nuage_news_data.png"
NUAGE_MEDIASTACK = "nuage_mediastack.png"

# Chemin des nuages de mot
PATH_NUAGE_NEWS_DATA = "assets/" + NUAGE_NEWS_DATA
PATH_NUAGE_MEDIASTACK = "assets/" + NUAGE_MEDIASTACK

