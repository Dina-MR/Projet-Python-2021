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


import extraction as ext
import gestionCorpus as gc
import classesCorpus as cp
import comparaison_corpus as cmp
import constantes as cst
import gui
import pandas
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
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
#fichier_news_data = "sauvegardes/news_data.pkl"
#gc.sauvegarder_corpus(corpus_news_data, fichier_news_data)
# Optionnel - Ouverture du corpus
#corpus_test_news_data = gc.ouvrir_corpus(cst.PATH_NEWS_DATA)


# ==== RECUPERATION & STOCKAGE DES ARTICLES MEDIASTACK ====
# ==== 1ère étape - Extraction ====
#articles_mediastack = ext.extraction_mediaStack(cst.my_key_mediastack, category = cst.CATEGORIES, limit_page = 100)

# ============= 2ème étape   ajout  des articles mediastack dans le Corpus ========
#corpus_mediastack = cp.Corpus("Corpus News Data mediastack")
#corpus_mediastack.ajouter_article(*articles_mediastack)

# ==== 3ème étape - Sauvegarde du corpus dans un fichier ====
# Sauvegarde du corpus des articles NewsData
#fichier_mediastack = "sauvegardes/mediastack.pkl"
#gc.sauvegarder_corpus(corpus_mediastack, fichier_mediastack)
# Optionnel - Ouverture du corpus
#corpus_test_mediastack = gc.ouvrir_corpus(cst.PATH_MEDIASTACK)


# ==== CALCUL DES SCORES OKAPI BM25 DES CORPUS ====

#corpus_news_data.set_score_okapi_bm25(corpus_mediastack)
#corpus_mediastack.set_score_okapi_bm25(corpus_news_data)

# OU

#corpus_test_news_data.set_score_okapi_bm25(corpus_test_mediastack)
#corpus_test_mediastack.set_score_okapi_bm25(corpus_test_news_data)


# ==== INTERFACE GRAPHIQUE ====

# ==== VERSION DE MOREL ====

# Génération des diagrammes circulaires dans l'application

app = dash.Dash(__name__)

app.layout = dbc.Container([
    dbc.Row([
        html.H1('Projet Python 2021-2022'),
        html.H1('Comparaison de corpus'),
    ], align = 'center'),
    dbc.Row([
        "Sélectionnez une catégorie",
    	dcc.Dropdown(
    		id = 'categorie',
    		options = cst.SELECTION_CATEGORIES,
    		value=1
    	)
    ], align = 'center'),
    dbc.Row([
        html.H2('Mots communs entre les deux corpus'),
        html.Div(id = "mots_communs"),
    ]),
    dbc.Row([
        html.H2('Mots exclusifs à chaque corpus'),
        dbc.Row([
            dbc.Col(html.Div(id = "mots_ex_news_data")),
            dbc.Col(html.Div(id = "mots_ex_mediastack")),
        ]),
    ]),
    dbc.Row([
        html.H2('Meilleur source pour chaque corpus'),
        dbc.Row([
            dbc.Col(html.Div(id = "source_news_data")),
            dbc.Col(html.Div(id = "source_mediastack")),
        ])
    ], align = "center"),
    dbc.Row([
        html.H2('Score OKAPI BM25 des corpus'),
        dbc.Row([
            dbc.Col(html.Div(id = "score_okapi_news_data")),
            dbc.Col(html.Div(id = "score_okapi_mediastack")),
        ]),
        dbc.Row([
            dbc.Col(html.Div("Corpus avec le meilleur score :")),
            dbc.Col(html.Div(id = "meilleur_corpus"))
        ])
    ]),
    dbc.Row([
        html.H2('ARTICLES'),
        html.H3('Articles du corpus Mediastack'),
    	html.Div(id = 'articles_mediastack',
                  children = []),
        html.H3('Articles du corpus News Data'),
    	html.Div(id = 'articles_news_data',
                  children = []),
    ]),
    dbc.Row([
        html.H2('STATISTIQUES'),
        html.H3('Statistiques du corpus Mediastack'),
    	html.Div(id = 'stats_mediastack',
                  children = []),
        html.H3('Statistiques du corpus News Data'),
    	html.Div(id = 'stats_news_data',
                  children = []),
    ])
])

@app.callback(Output('mots_communs', 'children'),
              Output('mots_ex_news_data', 'children'),
              Output('mots_ex_mediastack', 'children'),
              Output('source_news_data', 'children'),
              Output('source_mediastack', 'children'),
              Output('score_okapi_news_data', 'children'),
              Output('score_okapi_mediastack', 'children'),
              Output('meilleur_corpus', 'children'),
              Output('articles_news_data', 'children'),
              Output('articles_mediastack', 'children'),
              Output('stats_news_data', 'children'),
              Output('stats_mediastack', 'children'),
              Input('categorie', 'value'))

def update_output(categorie):
    # ==== 1. Collecte des articles ====
    articles_news_data = ext.extraction_news_data_api(cle_api = cst.CLE_API_NEWSDATA, langue = cst.LANGUES_NEWSDATA, categorie = categorie)
    articles_mediastack = ext.extraction_mediaStack(cst.my_key_mediastack,category = categorie,limit_page=100)
    
    # ==== 2. Stockage des articles dans des corpus ====
    # Corpus News Data
    corpus_news_data = cp.Corpus("Corpus News Data")
    corpus_news_data.ajouter_article(*articles_news_data)
    # Corpus Mediastack
    corpus_mediastack = cp.Corpus("Corpus News Data mediastack")
    corpus_mediastack.ajouter_article(*articles_mediastack)
    
    # ==== 3. Calcul des scores OKAPI BM25 des corpus ====
    corpus_news_data.set_score_okapi_bm25(corpus_mediastack)
    corpus_mediastack.set_score_okapi_bm25(corpus_news_data)
    
    # ==== 4. Sauvegarde des corpus dans des fichiers ===
    #gc.sauvegarder_corpus(corpus_news_data, cst.PATH_NEWS_DATA)
    #gc.sauvegarder_corpus(corpus_mediastack, cst.PATH_MEDIASTACK)
    
    # ==== 5. Récupération des mots communs & exclusifs entre les corpus ===
    # 5.1. Mots communs
    mots_communs = cmp.mots_communs_dataframe(corpus_news_data, corpus_mediastack).Mot.head().tolist()
    # 5.2. Mots exclusifs
    mots_exclusifs_news_data = cmp.mots_exclusifs_dataframe(corpus_news_data, corpus_mediastack).Mot.head().tolist()
    mots_exclusifs_mediastack = cmp.mots_exclusifs_dataframe(corpus_mediastack, corpus_news_data).Mot.head().tolist()
    
    # ==== 6. Récupération des meilleurs sources ====
    source_news_data = gui.afficher_carte_boostrap("Pour News Data", gui.liste_a_texte(corpus_news_data.get_meilleur_source()), cst.COULEUR_NEWS_DATA)
    source_mediastack = gui.afficher_carte_boostrap("Pour Mediastack", gui.liste_a_texte(corpus_mediastack.get_meilleur_source()), cst.COULEUR_MEDIASTACK, True)
    
    # ==== 7. Scores OKAPI BM25 des corpus ====
    score_news_data = gui.afficher_carte_boostrap("Pour News Data", str(corpus_news_data.score_okapi_bm25), cst.COULEUR_NEWS_DATA)
    score_mediastack = gui.afficher_carte_boostrap("Pour Mediastack", str(corpus_mediastack.score_okapi_bm25), cst.COULEUR_MEDIASTACK)  
    
    # ==== 8. Création des data-frames pour les articles ====
    # 8.1. Stockage des articles sous forme de liste de dictionnaire pour chaque corpus
    liste_dataframe_news_data = corpus_news_data.__asdictlist__()
    liste_dataframe_mediastack = corpus_mediastack.__asdictlist__()
    # 8.2. Génération des data-frames à partir des listes ci-dessus
    dataframe_news_data = pandas.DataFrame(liste_dataframe_news_data)
    dataframe_mediastack = pandas.DataFrame(liste_dataframe_mediastack)
    
    return gui.liste_a_texte(mots_communs), gui.liste_a_texte(mots_exclusifs_news_data), gui.liste_a_texte(mots_exclusifs_mediastack), source_news_data, source_mediastack, score_news_data, score_mediastack, cmp.meilleur_score_okapi_bm25(corpus_news_data, corpus_mediastack), gui.afficher_dataframe(dataframe_news_data), gui.afficher_dataframe(dataframe_mediastack), gui.afficher_dataframe(corpus_news_data.stats), gui.afficher_dataframe(corpus_mediastack.stats)
    
#if __name__ == '__main__':
    #app.run_server(port=4000)
    
app.run_server(port=4000)
