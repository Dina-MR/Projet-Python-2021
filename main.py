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
import pandas
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# === RECUPERATION & STOCKAGE DES ARTICLES NEWSDATA ====
# ==== 1ère étape - Extraction ====
# Création de la liste d'article
#articles_news_data = ext.extraction_news_data_api(cle_api = cst.CLE_API_NEWSDATA, langue = cst.LANGUES_NEWSDATA)

# ==== 2ème étape - Stockage des articles dans un corpus ====
# Corpus des articles NewsData
#corpus_news_data = cp.Corpus("Corpus News Data")
#corpus_news_data.ajouter_article(*articles_news_data)

# ==== 3ème étape - Sauvegarde du corpus dans un fichier ====
# Sauvegarde du corpus des articles NewsData
fichier_news_data = "sauvegardes/news_data.pkl"
#gc.sauvegarder_corpus(corpus_news_data, fichier_news_data)
# Optionnel - Ouverture du corpus
corpus_test_news_data = gc.ouvrir_corpus(fichier_news_data)


# ==== RECUPERATION & STOCKAGE DES ARTICLES MEDIASTACK ====
# ==== 1ère étape - Extraction ====
#articles_mediastack = ext.extraction_mediaStack(cst.my_key_mediastack, category = cst.CATEGORIES, limit_page = 100)

# ============= 2ème étape   ajout  des articles mediastack dans le Corpus ========
#corpus_mediastack = cp.Corpus("Corpus News Data mediastack")
#corpus_mediastack.ajouter_article(*articles_mediastack)

# ==== 3ème étape - Sauvegarde du corpus dans un fichier ====
# Sauvegarde du corpus des articles NewsData
fichier_mediastack = "sauvegardes/mediastack.pkl"
#gc.sauvegarder_corpus(corpus_mediastack, fichier_mediastack)
# Optionnel - Ouverture du corpus
corpus_test_mediastack = gc.ouvrir_corpus(fichier_mediastack)


# ==== CALCUL DES SCORES OKAPI BM25 DES CORPUS ====

#corpus_news_data.set_score_okapi_bm25(corpus_mediastack)
#corpus_mediastack.set_score_okapi_bm25(corpus_news_data)

# OU

corpus_test_news_data.set_score_okapi_bm25(corpus_test_mediastack)
corpus_test_mediastack.set_score_okapi_bm25(corpus_test_news_data)


# ==== INTERFACE GRAPHIQUE ====

# ==== VERSION DE MOREL ====

# Génération des diagrammes circulaires dans l'application

app = dash.Dash(__name__)

app.layout = html.Div([
	dcc.Dropdown(
		id = 'categorie',
		options = cst.SELECTION_CATEGORIES,
		value=1
	),
	'Articles:',
    html.H3('Articles du corpus Mediastack'),
	html.Div(id = 'output_mediastack',
              children = []),
    html.H3('Articles du corpus News Data'),
	html.Div(id = 'output_news_data',
              children = []),
])

@app.callback(Output('output_mediastack', 'children'),
              Output('output_news_data', 'children'),
              Input('categorie', 'value'))
def update_output(categorie):
    articles_bruts_news_data, articles_news_data = ext.extraction_news_data_api(cle_api = cst.CLE_API_NEWSDATA, langue = cst.LANGUES_NEWSDATA, categorie = categorie)
    articles_bruts_mediastack, articles_mediastack = ext.extraction_mediaStack(cst.my_key_mediastack,category = categorie,limit_page=100)

    #index=['author', 'title', 'description','source','category','language', 'country', 'published_at']
    #index_news_data = ['title', 'creator', 'description', 'full_description']

    #df = pandas.DataFrame(articles_brut)
    #df = df[index]
    
    dataframe_mediastack = pandas.DataFrame(articles_bruts_mediastack)
    dataframe_news_data = pandas.DataFrame(articles_bruts_news_data)
    
    return gui.afficher_dataframe(dataframe_mediastack), gui.afficher_dataframe(dataframe_news_data)

#if __name__ == '__main__':
    #app.run_server(port=4000)
    
app.run_server(port=4000)
