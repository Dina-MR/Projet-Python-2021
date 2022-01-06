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


# ==== INTERFACE GRAPHIQUE ====

app = dash.Dash(external_stylesheets=[cst.THEME])

app.layout = dbc.Container([
    dbc.Row([
        html.Header([
            html.H1('Projet Python 2021-2022'),
            html.H1('Comparaison de corpus'),
        ])
    ], align = 'center', style = cst.STYLE_ROW),
    dbc.Row([
        "Sélectionnez une catégorie",
    	dcc.Dropdown(
    		id = 'categorie',
    		options = cst.SELECTION_CATEGORIES,
    		value=1
    	)
    ], align = 'center', style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('Top 20 des mots pour chaque corpus'),
        dbc.Row([
            dbc.Col(html.Div(id = "nuage_news_data")),
            dbc.Col(html.Div(id = "nuage_mediastack")),
        ], style = cst.STYLE_ROW),
    ], style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('Mots communs entre les deux corpus'),
        html.Div(id = "mots_communs"),
    ], style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('Mots exclusifs à chaque corpus'),
        dbc.Row([
            dbc.Col(html.Div([
                html.H4("Pour News Data"),
                html.Div(id = "mots_ex_news_data")
                ])),
            dbc.Col(html.Div([
                html.H4("Pour News Data"),
                html.Div(id = "mots_ex_mediastack")
                ]))
        ]),
    ], style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('Meilleur source pour chaque corpus'),
        dbc.Row([
            dbc.Col(html.Div(id = "source_news_data")),
            dbc.Col(html.Div(id = "source_mediastack")),
        ], style = cst.STYLE_ROW)
    ], align = "center", style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('Score OKAPI BM25 des corpus'),
        dbc.Row([
            dbc.Col(html.Div(id = "score_okapi_news_data")),
            dbc.Col(html.Div(id = "score_okapi_mediastack")),
        ], style = cst.STYLE_ROW),
        dbc.Row([
            dbc.Col(html.Div("Corpus avec le meilleur score :")),
            dbc.Col(html.Div(id = "meilleur_corpus"))
        ], style = cst.STYLE_ROW)
    ], style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('ARTICLES'),
        html.H3('Articles du corpus Mediastack'),
    	html.Div(id = 'articles_mediastack',
                  children = []),
        html.H3('Articles du corpus News Data'),
    	html.Div(id = 'articles_news_data',
                  children = []),
    ], style = cst.STYLE_ROW),
    dbc.Row([
        html.H2('STATISTIQUES'),
        html.H3('Statistiques du corpus Mediastack'),
    	html.Div(id = 'stats_mediastack',
                  children = []),
        html.H3('Statistiques du corpus News Data'),
    	html.Div(id = 'stats_news_data',
                  children = []),
    ], style = cst.STYLE_ROW)
])


# === MISE A JOUR DE L'APPLICATION ====

@app.callback(Output('nuage_news_data', 'children'),
              Output('nuage_mediastack', 'children'),
              Output('mots_communs', 'children'),
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
    corpus_mediastack = cp.Corpus("Corpus Mediastack")
    corpus_mediastack.ajouter_article(*articles_mediastack)
    
    # ==== 3. Calcul des scores OKAPI BM25 des corpus ====
    corpus_news_data.set_score_okapi_bm25(corpus_mediastack)
    corpus_mediastack.set_score_okapi_bm25(corpus_news_data)
    
    # ==== 4. Sauvegarde des corpus dans des fichiers ===
    # Problème :  ne met pas à jour les fichiers
    gc.sauvegarder_corpus(corpus_news_data, cst.PATH_NEWS_DATA)
    gc.sauvegarder_corpus(corpus_mediastack, cst.PATH_MEDIASTACK)
    
    # ==== 5. Création des nuages de mot & récupération des images générées ====
    gui.nuage_mots(corpus_news_data.vocabulaire_duplicatas, cst.PATH_NUAGE_NEWS_DATA)
    gui.nuage_mots(corpus_mediastack.vocabulaire_duplicatas, cst.PATH_NUAGE_MEDIASTACK)
    nuage_news_data = gui.afficher_image_locale(cst.NUAGE_NEWS_DATA, "Pour News Data", app)
    nuage_mediastack = gui.afficher_image_locale(cst.NUAGE_MEDIASTACK, "Pour Mediastack", app)
    
    # ==== 6. Récupération des mots communs & exclusifs entre les corpus ===
    # 6.1. Mots communs
    mots_communs = cmp.mots_communs_dataframe(corpus_news_data, corpus_mediastack).Mot.head().tolist()
    # 6.2. Mots exclusifs
    mots_exclusifs_news_data = cmp.mots_exclusifs_dataframe(corpus_news_data, corpus_mediastack).Mot.head().tolist()
    mots_exclusifs_mediastack = cmp.mots_exclusifs_dataframe(corpus_mediastack, corpus_news_data).Mot.head().tolist()
    
    # ==== 7. Récupération des meilleurs sources ====
    source_news_data = gui.afficher_carte_boostrap("Pour News Data", gui.liste_a_texte(corpus_news_data.get_meilleur_source()), cst.COULEUR_NEWS_DATA)
    source_mediastack = gui.afficher_carte_boostrap("Pour Mediastack", gui.liste_a_texte(corpus_mediastack.get_meilleur_source()), cst.COULEUR_MEDIASTACK)
    
    # ==== 8. Scores OKAPI BM25 des corpus ====
    score_news_data = gui.afficher_carte_boostrap("Pour News Data", str(corpus_news_data.score_okapi_bm25), cst.COULEUR_NEWS_DATA)
    score_mediastack = gui.afficher_carte_boostrap("Pour Mediastack", str(corpus_mediastack.score_okapi_bm25), cst.COULEUR_MEDIASTACK)  
    
    # ==== 9. Création des data-frames pour les articles ====
    # 9.1. Stockage des articles sous forme de liste de dictionnaire pour chaque corpus
    liste_dataframe_news_data = corpus_news_data.__asdictlist__()
    liste_dataframe_mediastack = corpus_mediastack.__asdictlist__()
    # 9.2. Génération des data-frames à partir des listes ci-dessus
    dataframe_news_data = pandas.DataFrame(liste_dataframe_news_data)
    dataframe_mediastack = pandas.DataFrame(liste_dataframe_mediastack)
    
    return nuage_news_data, nuage_mediastack, gui.liste_a_texte(mots_communs), gui.liste_a_texte(mots_exclusifs_news_data), gui.liste_a_texte(mots_exclusifs_mediastack), source_news_data, source_mediastack, score_news_data, score_mediastack, cmp.meilleur_score_okapi_bm25(corpus_news_data, corpus_mediastack), gui.afficher_dataframe(dataframe_news_data), gui.afficher_dataframe(dataframe_mediastack), gui.afficher_dataframe(corpus_news_data.stats), gui.afficher_dataframe(corpus_mediastack.stats)

    
# ==== LANCEMENT DE L'APPLICATION ====   

app.run_server(port=4000)
