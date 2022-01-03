# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    C'est le script principal du programme.
"""

# ==== LIBRAIRIES ====


import constantes as cst
import extraction as ext
import gestionCorpus as gc
import classesCorpus as cp
import gui
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# === RECUPERATION & STOCKAGE DES ARTICLES NEWSDATA ====
# ==== 1ère étape - Extraction ====
# Création de la liste d'article
articles_news_data = ext.extraction_news_data_api(cle_api = cst.CLE_API_NEWSDATA, 
                                                  langue = cst.LANGUES_NEWSDATA)

# ==== 2ème étape - Stockage des articles dans un corpus ====
# Corpus des articles NewsData
corpus_news_data = cp.Corpus("Corpus News Data")
corpus_news_data.ajouter_article(*articles_news_data)

# ==== 3ème étape - Sauvegarde du corpus dans un fichier ====
# Sauvegarde du corpus des articles NewsData
fichier_news_data = "sauvegardes/news_data.pkl"
gc.sauvegarder_corpus(corpus_news_data, fichier_news_data)
# Optionnel - Ouverture du corpus
corpus_test_news_data = gc.ouvrir_corpus(fichier_news_data)


# ==== RECUPERATION & STOCKAGE DES ARTICLES MEDIASTACK ====
# ==== 1ère étape - Extraction ====
articles_mediastack = ext.extraction_mediaStack(cst.my_key_mediastack, category = cst.CATEGORIES, limit_page = 100)

# ============= 2ème étape   ajout  des articles mediastack dans le Corpus ========
corpus_mediastack = cp.Corpus("Corpus News Data mediastack")
corpus_mediastack.ajouter_article(*articles_mediastack)

# ==== 3ème étape - Sauvegarde du corpus dans un fichier ====
# Sauvegarde du corpus des articles NewsData
fichier_mediastack = "sauvegardes/mediastack.pkl"
gc.sauvegarder_corpus(corpus_mediastack, fichier_mediastack)
# Optionnel - Ouverture du corpus
corpus_test_mediastack = gc.ouvrir_corpus(fichier_mediastack)


# ==== CALCUL DES SCORES OKAPI BM25 DES CORPUS ====

corpus_news_data.set_score_okapi_bm25(corpus_mediastack)
corpus_mediastack.set_score_okapi_bm25(corpus_news_data)

# OU

corpus_test_news_data.set_score_okapi_bm25(corpus_test_mediastack)
corpus_test_mediastack.set_score_okapi_bm25(corpus_test_news_data)


# ==== INTERFACE GRAPHIQUE ====
    
app = dash.Dash(__name__)

app.layout = html.Div(children = [
    # Titre
    html.H1("Projet Python 2021-2022"),
    html.H2("Comparaison de corpus"),
    # Sélection de catégories
    dcc.Dropdown(id = 'categorie', options = cst.SELECTION_CATEGORIES, value = 'business'),
    # Nuage de mots
    html.Div(children = [
        html.Img(id = 'nuage_news_data',
                  style = {'display' : 'inline-block'},
                  src = ''),
        html.Img(id = 'nuage_mediastack',
                  style = {'display' : 'inline-block'},
                  src = '')
    ])
])


"""html.Div(children = [
    dcc.Graph(id = 'nuage_news_data',
              style = {'display' : 'inline-block'},
              figure = {}),
    dcc.Graph(id = 'nuage_mediastack',
              style = {'display' : 'inline-block'},
              figure = {})
])"""

@app.callback(
    Output("nuage_news_data", "src"),
    Output("nuage_mediastack", "src"),
    [Input("categorie", "value")])

def update(categorie):
    gui.nuage_mots(corpus_test_news_data.top_mots(), 'sauvegardes/nuage_news_data.png')
    gui.nuage_mots(corpus_test_news_data.top_mots(), 'sauvegardes/nuage_mediastack.png')
    nuage_news_data = app.get_asset_url('sauvegardes/nuage_news_data.png')
    nuage_mediastack = app.get_asset_url('sauvegardes/nuage_mediastack.png')
    return nuage_news_data, nuage_mediastack
    
app.run_server(debug = False)
