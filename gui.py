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


# ==== FONCTIONS ====

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

