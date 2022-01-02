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
corpus_test = gc.ouvrir_corpus(fichier_news_data)


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
corpus_test = gc.ouvrir_corpus(fichier_mediastack)


# ==== CALCUL DES SCORES OKAPI BM25 DES CORPUS ====

corpus_news_data.set_score_okapi_bm25(corpus_mediastack)
corpus_mediastack.set_score_okapi_bm25(corpus_news_data)
    
