# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 01:07:05 2022

@author: Lenovo
"""

import dash
import dash_table
import pandas as pd
from collections import OrderedDict
import pandas as pd

import os
#os.chdir("D:/Cours_M1Info/Programmation__python/Projet_python2021")
#df=pd.read_csv("articles1.csv",delimiter=",",header=0)

# scraping des données 

import  scrappingMediastack as sgm

import constantes_mediastack as cst
#import extraction as ext
import gestionCorpus as gc
import classesCorpus as cp
#import pandas as pd
#import nltk

# ==== 1ère étape - Extraction ====
categories=["busness","entertainment","health","science","sports","technology"]


articles_brut,articles_mediastack=sgm.extraction_mediaStack(cst.my_key_mediastack,category="sports",limit_page=100)

index=['author', 'title', 'description','source','category','language', 'country', 'published_at']
#colonnes=["author","title"]

df=pd.DataFrame(articles_brut)
df=df[index]




app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    style_data={
        'whiteSpace': 'normal',
    },
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df.columns],
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 15px;
            max-height: 30px; min-height: 30px; height: 30px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    tooltip_data=[
        {
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df.to_dict('records')
    ],
    tooltip_duration=None,

    style_cell={'textAlign': 'left'} # left align text in columns for readability
)

if __name__ == '__main__':
    app.run_server(debug=True)
