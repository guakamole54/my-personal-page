from dash import register_page, html, callback, Input, Output, dcc
import dash_mantine_components as dmc
from utils import priprava_dat
from plotly.express import bar

df = priprava_dat()

register_page(__name__)

layout = dmc.Stack([
    dmc.Select(
        id="vyber-uzemi",
        value="Česká republika",
        label="Vyberte oblast:",
        data=[
            {
                "value": moznost,
                "label": moznost}
            for moznost in df['uzemi_txt'].drop_duplicates().sort_values()

        ]
    ),

    dcc.Graph(id="graf_vzdelania")


])

@callback(
    Output("graf_vzdelania", "figure"),
    Input("vyber-uzemi", "value")
)

def data_do_grafu(uzemi):
    w_df = df.copy()
    w_df = w_df[w_df['uzemi_txt'] == uzemi]
    w_df = w_df.groupby(by=['vzdelani_txt'])['hodnota'].sum().reset_index()

    fig = bar(
        w_df,
        x="vzdelani_txt",
        y="hodnota"
    )

    return fig

# print(df[["uzemi_txt", "vzdelani_txt", "hodnota"]])
