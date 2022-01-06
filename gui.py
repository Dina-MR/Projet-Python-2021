# -*- coding: utf-8 -*-
"""
IDE : 
    Spyder Editor
Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    Ce script regroupe des fonctions relatives à l'interface.
"""

# ==== LIBRAIRIES ====

from constantes import STYLE_IMAGE
from wordcloud import WordCloud, STOPWORDS
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import plotly.express as px
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table


# ==== FONCTIONS ====

def afficher_dataframe(dataframe):
    """ Affichage d'un data-frame sous Dash
    
    Paramètres
    ----------
    dataframe : pandas.DataFrame
        Données des articles
        
    Retour
    ------
    dash_table.DataTable
        Table de données issu du data-frame
    """
    return  dash_table.DataTable(style_data={
        'whiteSpace': 'normal',
        },
        data =  dataframe.to_dict('records'),
        columns = [{'id': c, 'name': c} for c in  dataframe.columns],
        css = [{
            'selector': '.dash-spreadsheet td div',
            'rule': '''
                line-height: 15px;
                max-height: 30px; min-height: 30px; height: 30px;
                display: block;
                overflow-y: hidden;
            '''
        }],
        tooltip_data = [
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in dataframe.to_dict('records')
        ],
        tooltip_duration = None,
        page_size = 10,
        style_cell = {'textAlign': 'left'} # left align text in columns for readability
    )


def liste_a_texte(liste_textuelle):
    """ Conversion d'une liste de mots ou de noms en chaine de caractère unique
    
    Paramètres
    ----------
    liste_textutelle : list
        Liste de mots ou de noms à reconvertir
        
    Retour
    ------
    string
        Texte issu de la liste
    """
    return ", ".join(liste_textuelle)


def afficher_carte_boostrap(titre, contenu, couleur, inversion = False):
    """ Affichage d'une carte Boostrap
    
    Paramètres
    ----------
    titre : string
        Titre de la carte
    contenu : string
        Contenu textuel de la carte
    Couleur : string
        Code couleur de la carte
    Inversion : bool
        Indication de l'inversion ou non des éléments à l'intérieur de la droite
        
    Retour
    ------
    dash_table.DataTable
        Contenu d'une carte boostrap avec son titre
    """
    return dbc.Card([
                dbc.CardBody(
                    [
                        html.H4(titre),
                        html.P(contenu),
                    ]
                ),
        ], 
        color = couleur, 
        inverse = inversion)


def texte_pour_nuage(liste_mots):
    """ Conversion d'une liste de mots en une chaîne de mots séparés par un espace
    
    Paramètres
    ----------
    liste_mots : list
        Liste de mots à convertir en chaîne de caractère
        
    Retour
    ------
    string
        Texte pour le nuage de mot
    """
    return ' '.join(liste_mots)


def nuage_mots(liste_mots, fichier_sauvegarde = ''):
    """ Génération d'un nuage de mots à partir d'une liste de mots
    
    Paramètres
    ----------
    liste_mots : list
        Liste de mots 
    fichier_sauvegarde : string
        Chemin du fichier où sera conservé le nuage de mots
        
    Retour
    ------
    Aucun
    """
    print("Création du nuage en cours...")
    texte = texte_pour_nuage(liste_mots)
    wordcloud = WordCloud(stopwords = STOPWORDS, background_color='white', width=3000, height=1500, max_words = 20).generate(texte)
    plt.imshow(wordcloud)
    plt.axis('off')        #ccache l'affichage des axes
    plt.savefig(fichier_sauvegarde)
    print("Nuage créé et sauvegardé dans le fichier " + fichier_sauvegarde + ".")
    

def afficher_image_locale(fichier, titre, application):
    """ Affichage d'une image locale sur Dash
    
    Paramètres
    ----------
    fichier : string
        Nom du fichier image dans le dossier "assets"
    titre : string
        Titre associé à l'image'
    application : dash.Dash()
        Application Dash
        
    Retour
    ------
    html.Div
        Section HTML contenant l'image et son titre
    """
    return html.Div([
        html.H4(titre),
        html.Img(src = application.get_asset_url(fichier), style = STYLE_IMAGE)
    ])
