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

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
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
    texte = texte_pour_nuage(liste_mots)
    wordcloud = WordCloud(stopwords = STOPWORDS, background_color='white', width=3000, height=1500).generate(texte)
    plt.imshow(wordcloud)
    plt.axis('off')        #ccache l'affichage des axes
    plt.savefig(fichier_sauvegarde)
    plt.show()
    #return plt
    

# ==== TESTS ====
    
msg = "Belief is a beautiful Belief  But makes Belief for the heaviest  Belief beautiful Belief sword Like Belief punching underwater You Belief  never can Belief  hit beautiful Belief who Belief  you're trying Belief for"
test_cours = msg.split()
nuage_mots(test_cours, "sauvegardes/test_cours.png")

#nuage_mots(corpus_test_news_data.top_mots())

