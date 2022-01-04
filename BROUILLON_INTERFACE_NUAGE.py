# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 22:39:22 2022

@author: Dina
"""

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