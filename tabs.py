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

header = dbc.Row(html.H1(about_data['NAME']))
about_tab = dbc.Row(
    [   dbc.Col(image, md=3,),
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
