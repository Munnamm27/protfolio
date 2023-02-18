import plotly.graph_objects as go
from dash import html,dcc
import dash_bootstrap_components as dbc

def get_map(pre_lat,pre_lon,per_lat,per_lon,pre_full,per_full):    
    fig=go.Figure()
    fig.add_trace(go.Scattermapbox(
        name='Present',
            lat=[pre_lat],
            lon=[pre_lon],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=21,
                color='darkblue',
                opacity=1
            ),
            text=pre_full,
            hoverinfo='text'
        ))

    fig.add_trace(go.Scattermapbox(
        name='Permanent',
            lat=[per_lat],
            lon=[per_lon],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=21,
                color='red',
                opacity=1
            ),
            text=per_full,
            hoverinfo='text'
        ))

    fig.update_layout(
        # mapbox_style='open-street-map',
        autosize=True,
        hovermode='x unified',
        margin={"r": 10, "t": 0, "l": 10, "b": 10},
        showlegend=True,
        legend=dict(
        orientation="h",
        yanchor="auto",
        y=1,
        xanchor="auto",
        x=1
    ),
        mapbox=dict(
        accesstoken="pk.eyJ1IjoibXVubmEtMTgyNSIsImEiOiJjbGNvaGhxMW0xajdsM3ltcWRzcndzcDN5In0.yt531xalbnEhc3HPRTzZkw",
            bearing=0,
            center=dict(
                lat=24.3, 
                lon=89.6
            ),
            pitch=0,
            zoom=6,
            style='streets'
        ),
    )
    return fig




def skill_card(title,skillset):
    cards = dbc.Card(
    dbc.CardBody(
        [
            html.H6(title, className="card-title text-center"),
            dcc.Markdown(
                skillset,style={'backgroundColor':'lightgreen','margin':'5px','padding':'5px',"border-radius": "4px"}
            ),
        ]
    ),
    style={
    "backgroundColor":'lightcyan',
    "margin":'15px'
       },
)
    return cards