import os
import base64
import json
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import style as st


BASE_DIR = os.path.abspath('.')
about_path = os.path.join(BASE_DIR, "data/about.json")
para_path = os.path.join(BASE_DIR, "data/paragraph.json")
image_path = os.path.join(BASE_DIR, "assets/image.png")
about_data = json.load(open(about_path, 'rb'))
paragraph = json.load(open(para_path, 'rb'))['paragraph']

with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()
image = html.Img(src=f"data:image/jpg;base64,{encoded_image}")

header = dbc.Row(html.H1(about_data['NAME']))
about_tab = dbc.Row(
    [dbc.Col(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Graph(id='location_map'),
                        ], md=5, style=st.common_border
                    ),
                    dbc.Col(
                        [
                            html.P(paragraph, style={"marginTop": '20px'})
                        ], md=6, style=st.common_border
                    ),

                ], align='left', justify='left'
            )
        ], md=9

    ),
        dbc.Col(image, md=3, style={'border': '1px solid black'})], align='left', justify='left'
)
