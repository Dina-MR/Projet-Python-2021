# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:09:29 2021

Auteurs : 
    MBEDI Morel, RANDRIAZANAMPARANY Dina
Rôle du Script : 
    C'est le script principal du programme mediastack.

"""
# extration des articles 
import  scrappingMediastack as sgm

import constantes_mediastack as cst
#import extraction as ext
import gestionCorpus as gc
import classesCorpus as cp
import pandas as pd
#import nltk

# ==== 1ère étape - Extraction ====

article_brut,articles_mediastack=sgm.extraction_mediaStack(cst.my_key_mediastack,category=cst.CATEGORIES,limit_page=100)

df=pd.DataFrame(article_brut)
index=['author', 'title', 'description','source','category','language', 'country', 'published_at']
df=df[index]
print(df.columns)
df.to_csv("articles1.csv")
# ============= 2ème étape   ajout  des articles mediastack dans le Corpus ========
corpus_news_data_mediastack = cp.Corpus("Corpus News Data mediastack")
corpus_news_data_mediastack.ajouter_article(*articles_mediastack)


# ==== 3ème étape - Sauvegarde du corpus dans un fichier ====

# Sauvegarde du corpus des articles NewsData
fichier_news_data = "sauvegardes/news_data.pkl"
gc.sauvegarder_corpus(corpus_news_data_mediastack, fichier_news_data)

# Optionnel - Ouverture du corpus
corpus_test = gc.ouvrir_corpus(fichier_news_data)

