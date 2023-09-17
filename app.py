from dash import Dash, html, callback, Input, Output, State, page_container
import dash_mantine_components as dmc
from utils import navigacny_panel
from dash_iconify import DashIconify

app = Dash(__name__, use_pages=True)
server = app.server

links = {
    "about": {"label": "About"},
    "projects": {"label": "Projects"},
    "background": {"label": "Background"},
    "contact-me.py": {"label": "Contact Me"},
    "scitanie": {"label": "Scitanie"}
}

app.layout = dmc.MantineProvider([
    navigacny_panel(links, logo="tabler:square-rounded-letter-r"),
    html.Div(page_container, style={"margin-top": 40})
], theme={"colorScheme": "dark"}, withGlobalStyles=True, id="provider-temy")

@callback(
    Output("provider-temy", "theme"),
    Input("tlacidlo-zmena-temy", "n_clicks"),
    config_prevent_initial_callbacks=True
)

def change_theme(n_clicks, theme):
    if theme['colorScheme'] == 'dark':
        return {'colorScheme': 'light'}
    else:
        return {"colorScheme": "dark"}

if __name__ == "__main__":
    app.run(debug=False)
