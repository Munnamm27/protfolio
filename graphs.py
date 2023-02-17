import plotly.graph_objects as go

def get_map(pre_lat,pre_lon,per_lat,per_lon,pre_full,per_full):    
    fig=go.Figure()
    fig.add_trace(go.Scattermapbox(
        name='Present',
            lat=[pre_lat],
            lon=[pre_lon],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=17,
                color='darkblue',
                opacity=0.7
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
                size=17,
                color='red',
                opacity=0.7
            ),
            text=per_full,
            hoverinfo='text'
        ))

    fig.update_layout(
        mapbox_style='open-street-map',
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
            bearing=0,
            center=dict(
                lat=pre_lat,
                lon=pre_lon
            ),
            pitch=0,
            zoom=5,
        ),
    )
    return fig