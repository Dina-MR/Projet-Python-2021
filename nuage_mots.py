# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 22:45:13 2021

@author: Lenovo
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def nuage_mots(texte,max_mots=20):
    
    wordcloud = WordCloud(max_words=max_mots, stopwords = STOPWORDS, background_color='white', width=3000, height=1500).generate(texte)
    plt.imshow(wordcloud)
    plt.axis('off')        #ccache l'affichage des axes
    plt.show()
    
    
msg = "Belief is a beautiful Belief  But makes Belief for the heaviest  Belief beautiful Belief sword Like Belief punching underwater You Belief  never can Belief  hit beautiful Belief who Belief  you're trying Belief for"


nuage_mots(msg)





'''
message = "Belief is a beautiful armor But makes for the heaviest sword Like punching underwater You never can hit who you're trying for"

wordcloud = WordCloud(max_words=10, stopwords = STOPWORDS, background_color='white', width=1920, height=1080).generate(message)

plt.imshow(wordcloud)
plt.axis('off')        #evite l'affichage des axes
plt.show()
'''