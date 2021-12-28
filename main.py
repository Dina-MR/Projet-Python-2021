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


# ==== 1ère étape - Extraction ====

# Avec l'API NewsData
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
corpus_test = gc.ouvrir_corpus(fichier_news_data)
