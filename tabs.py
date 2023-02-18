import os
import base64
import json
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import style as st
import graphs as gs


BASE_DIR = os.path.abspath('.')
about_path = os.path.join(BASE_DIR, "data/about.json")
para_path = os.path.join(BASE_DIR, "data/paragraph.json")
image_path = os.path.join(BASE_DIR, "assets/image.png")
about_data = json.load(open(about_path, 'rb'))
paragraph = json.load(open(para_path, 'rb'))['paragraph']

present_cord=about_data["ADDRESS"]["present"]["cordinates"]
permanent_cord=about_data["ADDRESS"]["permanent"]["cordinates"]
present_add=about_data["ADDRESS"]["present"]["description"]
permanent_add=about_data["ADDRESS"]["permanent"]["description"]

with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()
image = html.Img(src=f"data:image/jpg;base64,{encoded_image}")

header = dbc.Row(html.H1(about_data['NAME'],style={'color':'white'}))


about_tab = dbc.Row(
    [   dbc.Col( 
    [ 
        html.Div(style={'border':'1px black solid','height':'300px','marginTop':'10px'}),
        html.Div(
            [html.I("Curently Working As"),
            html.H4("Data Scientist"),
            html.H5("SSL Wirelsess"),
            html.I("Standard Center, 27/1, New Eskaton Road, Dhaka-1000")],
        style=st.designation),
    ],md=3
    ),
        dbc.Col(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.P(paragraph, style={"marginTop": '20px'})
                        ], md=7, style=st.section_para
                    ),
                    dbc.Col(
                        [   
                            html.Div(html.H6("Address")),
                            dcc.Graph(figure=gs.get_map(present_cord[0],present_cord[1],permanent_cord[0],permanent_cord[1],present_add,permanent_add)),
                        ], md=4, style=st.section
                    ),

                ], align='left', justify='left'
            )
        ], md=9

    ),
        ], align='left', justify='left'
)



skill_tab=dbc.Row( 
    [ 
        dbc.Col( 
            [gs.skill_card("Languages",'''
           - Python
           - SQL
            '''),
            gs.skill_card("Analysis & Visualization",'''
            - Pandas
            - Dask 
            - Matplotlib 
            - Seaborn 
            - Plotly'''),
            gs.skill_card("Dashboarding Tools",'''
            - Plotly-Dash
            - Streamlit 
            - Power BI
            '''),
            ],md=3

        ),
        dbc.Col( 
            [   gs.skill_card("Machine Learning",'''
            - Supervised Learnng
            - Clustering
            - Scikit Learn
            - Tensorflow
            - DNN
            - CNN
            - RNN
            - LSTM
            - Transfer Learning
            '''),
                gs.skill_card("Feature Engineering",'''
                - Outlier detection 
                - Feature encoding
                - Feature selection
                - Null value handling
                '''),
                
             
             
             ],md=3
        ),
        dbc.Col( 
            [
    gs.skill_card("Natural Language Processing",'''
            - Bag of Words
            - Word Embedding
            - N-Grams
            - Sentiment Analysis
            - NER 
            - HuggingFace Models
    '''),
    gs.skill_card("Deployment & API",'''
    - Docker
    - FastAPI
    - Flask''')],md=3
        ),

    ],justify='center'
)


education_tab=[dbc.Row( 
    [ 
        dbc.Col( gs.edu_card("BSc","Rajshahi University of Enginnering & Technology","Major: Electronics and Telecommunication Engineering","2021"),md=5 ),
        dbc.Col( gs.edu_card("HSC","New Govt. Degree College, Rajshahi","Major: Science","2015"),md=5 ),
    ],justify='center'
),

dbc.Row( 
    [ 
        dbc.Col( gs.edu_card("SSC","Mohanpur Govt. High School, Rajshahi","Major: Science","2013"),md=5 ),
    ],justify='center'
),
]