import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# ---- Chargement des données ----
df_coop = pd.read_csv("data/cooperatives_clean.csv")
df_grandes = pd.read_csv("data/grandes_exploitations_clean.csv")
df_marches = pd.read_csv("data/marches_clean.csv")
df_plant = pd.read_csv("data/plantations_clean.csv")
df_zaaps = pd.read_csv("data/zaaps_clean.csv")
df_pep = pd.read_csv("data/pepinieres_clean.csv")

VERT = "#1b4332"
VERT2 = "#2d6a4f"
VERT3 = "#52b788"
JAUNE = "#f4a261"
BG = "#faf9f6"

app = Dash(__name__, external_stylesheets=[
    dbc.themes.FLATLY,
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap"
])

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Dashboard Agricole Togo</title>
        {%favicon%}
        {%css%}
        <style>
            * { font-family: "Poppins", sans-serif; box-sizing: border-box; }

            body {
                background-color: #faf9f6;
                background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E%3Cg fill='%2352b788' fill-opacity='0.06'%3E%3Cpath d='M40 0 Q45 20 40 40 Q35 20 40 0Z'/%3E%3Cpath d='M40 40 Q60 45 80 40 Q60 35 40 40Z'/%3E%3Cpath d='M0 40 Q20 45 40 40 Q20 35 0 40Z'/%3E%3Cpath d='M40 40 Q45 60 40 80 Q35 60 40 40Z'/%3E%3C/g%3E%3C/svg%3E");
                margin: 0;
            }

            /* ---- HEADER ---- */
            .header-gradient {
                background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 60%, #2d6a4f 100%);
                padding: 35px 50px;
                position: relative;
                overflow: hidden;
                border-bottom: 3px solid #52b788;
            }
            .header-gradient::before {
                content: '';
                position: absolute;
                top: -60px; right: -60px;
                width: 250px; height: 250px;
                background: radial-gradient(circle, rgba(82,183,136,0.15), transparent);
                border-radius: 50%;
                animation: pulse 4s ease-in-out infinite;
            }
            .header-gradient::after {
                content: '🌿';
                position: absolute;
                right: 50px; top: 20px;
                font-size: 5rem;
                opacity: 0.1;
                animation: float 6s ease-in-out infinite;
            }

            /* ---- STATS ---- */
            .stat-card {
                background: white;
                border-radius: 20px;
                padding: 22px 18px;
                text-align: center;
                box-shadow: 0 4px 20px rgba(0,0,0,0.07);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                cursor: pointer;
                min-width: 140px;
                margin: 8px;
                border-bottom: 3px solid transparent;
                animation: fadeInUp 0.6s ease forwards;
            }
            .stat-card:hover {
                transform: translateY(-10px) scale(1.03);
                box-shadow: 0 16px 35px rgba(0,0,0,0.13);
            }
            .stat-number {
                font-size: 2.2rem;
                font-weight: 700;
                margin: 5px 0;
            }
            .stat-label {
                font-size: 0.78rem;
                color: #777;
                margin: 0;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }

            /* ---- FILTRE ---- */
            .dropdown-container {
                background: linear-gradient(135deg, #ffffff 60%, #eafaf1);
                border-radius: 20px;
                padding: 25px 35px;
                box-shadow: 0 8px 30px rgba(45,106,79,0.10);
                margin: 20px;
                border: 1.5px solid #b7e4c7;
                position: relative;
                animation: fadeInUp 0.7s ease forwards;
            }
            .dropdown-container::after {
                content: '🔍';
                position: absolute;
                right: 30px; top: 22px;
                font-size: 1.8rem;
                opacity: 0.25;
            }
            .Select-control {
                border-radius: 12px !important;
                border: 2px solid #52b788 !important;
                padding: 6px !important;
                font-family: "Poppins" !important;
                background: #f9fffe !important;
                box-shadow: 0 2px 10px rgba(82,183,136,0.12) !important;
                transition: all 0.3s ease !important;
            }
            .Select-control:hover {
                border-color: #1b4332 !important;
                box-shadow: 0 4px 18px rgba(27,67,50,0.2) !important;
            }
            .Select-placeholder { color: #aaa !important; font-style: italic !important; }
            .Select-menu-outer {
                border-radius: 14px !important;
                border: 1.5px solid #b7e4c7 !important;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
                overflow: hidden !important;
                animation: fadeInUp 0.3s ease !important;
            }
            .Select-option:hover {
                background: linear-gradient(90deg, #d8f3dc, #f0faf4) !important;
                color: #1b4332 !important;
                padding-left: 20px !important;
                transition: all 0.2s ease !important;
            }

            /* ---- GRAPHIQUES ---- */
            .graph-card {
                background: white;
                border-radius: 20px;
                padding: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.07);
                margin: 10px;
                flex: 1;
                transition: box-shadow 0.3s ease, transform 0.3s ease;
                animation: fadeInUp 0.8s ease forwards;
            }
            .graph-card:hover {
                box-shadow: 0 12px 30px rgba(0,0,0,0.12);
                transform: translateY(-4px);
            }

            /* ---- SECTION TITLE ---- */
            .section-title {
                color: #1b4332;
                font-weight: 700;
                font-size: 1.2rem;
                padding: 20px 30px 5px;
                border-left: 5px solid #52b788;
                margin: 10px 20px 0;
                letter-spacing: 0.3px;
            }

            /* ---- CARTE ---- */
            .carte-container {
                margin: 10px 20px 20px;
                border-radius: 20px;
                overflow: hidden;
                box-shadow: 0 8px 30px rgba(0,0,0,0.10);
                border: 2px solid #b7e4c7;
                animation: fadeInUp 1s ease forwards;
            }

            /* ---- FOOTER ---- */
            .footer {
                background: linear-gradient(135deg, #0a0a0a, #1b4332);
                color: white;
                text-align: center;
                padding: 25px;
                margin-top: 30px;
                border-top: 3px solid #52b788;
            }

            /* ---- ANIMATIONS ---- */
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(25px); }
                to   { opacity: 1; transform: translateY(0); }
            }
            @keyframes pulse {
                0%, 100% { transform: scale(1); opacity: 0.5; }
                50%       { transform: scale(1.2); opacity: 1; }
            }
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50%       { transform: translateY(-15px); }
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def stat_card(titre, valeur, couleur, emoji):
    return html.Div([
        html.P(emoji, style={"fontSize": "1.8rem", "margin": "0"}),
        html.P(f"{valeur:,}", className="stat-number", style={"color": couleur}),
        html.P(titre, className="stat-label")
    ], className="stat-card", style={"borderBottomColor": couleur})

app.layout = html.Div([

    # ---- Header ----
    html.Div([
        html.H1("🌱 Tableau de Bord Agricole du Togo",
                style={"color": "white", "fontWeight": "700",
                       "fontSize": "2rem", "margin": "0"}),
        html.P("Data Challenge • Togo AI Lab 2026 • Géographie du tissu agricole",
               style={"color": "#95d5b2", "margin": "8px 0 0", "fontWeight": "300",
                      "fontSize": "0.95rem", "letterSpacing": "0.5px"})
    ], className="header-gradient"),

    # ---- Stats ----
    html.P("📊 Vue d'ensemble", className="section-title"),
    html.Div([
        stat_card("Coopératives",     len(df_coop),   "#2d6a4f", "🤝"),
        stat_card("Grandes Exploit.", len(df_grandes), "#52b788", "🏭"),
        stat_card("Marchés",          len(df_marches), "#f4a261", "🛒"),
        stat_card("Plantations",      len(df_plant),   "#e76f51", "🌴"),
        stat_card("ZAAPs",            len(df_zaaps),   "#457b9d", "🗺️"),
        stat_card("Pépinières",       len(df_pep),     "#6d6875", "🌿"),
    ], style={"display": "flex", "flexWrap": "wrap",
              "justifyContent": "center", "padding": "10px 20px"}),

    # ---- Filtre ----
    html.Div([
        html.Label("Filtrer par région",
                   style={"fontWeight": "700", "color": "#1b4332",
                          "fontSize": "1rem", "letterSpacing": "0.3px"}),
        html.P("Sélectionne une région pour affiner toutes les analyses",
               style={"color": "#999", "fontSize": "0.78rem", "margin": "2px 0 12px"}),
        dcc.Dropdown(
            id="filtre-region",
            options=[{"label": f"📍 {r}", "value": r}
                     for r in sorted(df_coop["region_nom_bdd"].dropna().unique())],
            value=None,
            placeholder="🌍 Toutes les régions du Togo",
            clearable=True,
        )
    ], className="dropdown-container"),

    # ---- Graphiques ligne 1 ----
    html.P("📈 Analyses par région", className="section-title"),
    html.Div([
        html.Div(dcc.Graph(id="graph-coop",   config={"displayModeBar": False}), className="graph-card"),
        html.Div(dcc.Graph(id="graph-marches",config={"displayModeBar": False}), className="graph-card"),
    ], style={"display": "flex", "padding": "5px 10px"}),

    # ---- Graphiques ligne 2 ----
    html.Div([
        html.Div(dcc.Graph(id="graph-terrain",config={"displayModeBar": False}), className="graph-card"),
        html.Div(dcc.Graph(id="graph-annee",  config={"displayModeBar": False}), className="graph-card"),
    ], style={"display": "flex", "padding": "5px 10px"}),

    # ---- Carte ----
    html.P("🗺️ Carte Interactive", className="section-title"),
    html.Div([
        html.Iframe(
            src="/assets/carte.html",
            style={"width": "100%", "height": "580px", "border": "none"}
        )
    ], className="carte-container"),

    # ---- Footer ----
    html.Div([
        html.P("🌱 Togo AI Lab • Data Challenge Agriculture 2026",
               style={"margin": "0", "fontWeight": "600"}),
        html.P("Données : geodata.gouv.tg & opendata.gouv.tg",
               style={"opacity": "0.6", "fontSize": "0.75rem", "margin": "5px 0 0"})
    ], className="footer")
])

# ---- Callbacks ----
@app.callback(
    Output("graph-coop",    "figure"),
    Output("graph-marches", "figure"),
    Output("graph-terrain", "figure"),
    Output("graph-annee",   "figure"),
    Input("filtre-region",  "value")
)
def update_graphs(region):
    coop   = df_coop   if not region else df_coop[df_coop["region_nom_bdd"]     == region]
    marches= df_marches if not region else df_marches[df_marches["region_nom_bdd"]== region]
    plant  = df_plant  if not region else df_plant[df_plant["region_nom_bdd"]   == region]
    grandes= df_grandes if not region else df_grandes[df_grandes["region_nom_bdd"]== region]

    LAYOUT = dict(
        plot_bgcolor="white", paper_bgcolor="white",
        font=dict(family="Poppins", size=12, color="#333"),
        margin=dict(t=50, b=30, l=20, r=20),
        showlegend=False
    )

    fig1 = px.bar(
        coop.groupby("region_nom_bdd").size().reset_index(name="n"),
        x="region_nom_bdd", y="n",
        title="🤝 Coopératives par région",
        color="n", color_continuous_scale="Greens"
    )
    fig1.update_traces(marker_line_width=0, opacity=0.85)

    fig2 = px.bar(
        marches.groupby("region_nom_bdd").size().reset_index(name="n"),
        x="region_nom_bdd", y="n",
        title="🛒 Marchés par région",
        color="n", color_continuous_scale="Oranges"
    )
    fig2.update_traces(marker_line_width=0, opacity=0.85)

    fig3 = px.pie(
        plant.groupby("terrain").size().reset_index(name="n"),
        names="terrain", values="n",
        title="🌴 Plantations par type de terrain",
        color_discrete_sequence=["#2d6a4f","#52b788","#95d5b2","#f4a261","#e76f51"]
    )
    fig3.update_traces(hole=0.4, pull=[0.05]*10)

    fig4 = px.area(
        grandes.groupby("exploitation_annee").size().reset_index(name="n"),
        x="exploitation_annee", y="n",
        title="📅 Grandes exploitations par année",
        color_discrete_sequence=["#2d6a4f"]
    )
    fig4.update_traces(fill="tozeroy", fillcolor="rgba(82,183,136,0.15)")

    for fig in [fig1, fig2, fig3, fig4]:
        fig.update_layout(**LAYOUT)
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=True, gridcolor="#f5f5f5")

    return fig1, fig2, fig3, fig4

if __name__ == "__main__":
    app.run(debug=True)