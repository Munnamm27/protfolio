from dash import dcc, html, dash_table, callback_context, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import tabs
import dash
import style

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)




app.layout = dbc.Container(
    [
        tabs.header,
        dbc.Tabs(
            [
                dbc.Tab(
                    tabs.about_tab,
                    label="About",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Experience",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Projects",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Publications & Certifications",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Skills",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Education",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Extra Curriculam Activities",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
                dbc.Tab(
                    html.I("To be updated"),
                    label="Contact",
                    # active_label_style={
                    #     "backgroundColor": "#ffe9fb",
                    #     "fontWeight": "bold",
                    #     "color": "black",
                    # },
                ),
            ],
        ),
    ],
    fluid=False,
    style={
        # "backgroundColor": "#ffe9fb",
        "border": "3px black solid",
        "border-radius": "5px",
    },
)

if __name__ == "__main__":
    app.run_server(debug=True, port=7000)