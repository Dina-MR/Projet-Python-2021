# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:09:03 2022

@author: Lenovo
"""

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
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

articles_brut,articles_mediastack=sgm.extraction_mediaStack(cst.my_key_mediastack,category="busness",limit_page=100)

df=pd.DataFrame(articles_brut)

default_font = 'Roboto bold'

# ==== 1ère étape - Extraction ====



col_options=[dict(label=x,value=x)
    for x in categories]

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Articles"),
    #html.H2(id="the_output"),
    #dcc.Input(id='the_input')
    dcc.Dropdown(id='categories',value="busness",options=col_options),
    html.H2("articles "),
    dash_table.DataTable()
   

])

@app.callback(Output('table2'),[Input('categories','value')])
def dataFrameArticle(categories):
    categories=categories if categories else "busness"
    df_articles=df.query("categories==@categories")

    return dash_table.DataTable(style_data={
        'whiteSpace': 'normal',
    },
    data= df_articles.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in df_articles.columns],
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

app.run_server(debug=True)


























articles_brut,articles_mediastack=sgm.extraction_mediaStack(cst.my_key_mediastack,category="sports",limit_page=100)

df=pd.DataFrame(articles_brut)
