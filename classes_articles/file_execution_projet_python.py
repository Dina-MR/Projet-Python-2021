# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:21:28 2021

@author: Lenovo
"""
import api_mediastack as media
from classes_articles.classesArticles import Article, ArticleMediastack, ArticleNewsData

from classesArticles  import  Article
my_key_mediastack="74713d7a61ca250397ba5e6b7b64b540"
CATEGORIES = '-general,health' 
res=media.extraction_mediaStack(my_key_mediastack,category=CATEGORIES,limit_page=10)
print(res)