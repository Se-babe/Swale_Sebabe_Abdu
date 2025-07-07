import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load and clean data
df = pd.read_csv("Life_Expectancy_Data.csv")

# Clean column names (strip spaces)
df.columns = df.columns.str.strip()

# Convert BMI to numeric
df["BMI"] = pd.to_numeric(df["BMI"], errors="coerce")

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "🌍 Life Expectancy Dashboard"

# Layout
app.layout = html.Div([
    html.H1("🌍 Life Expectancy Insights Dashboard By Sebabe", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            options=[{"label": c, "value": c} for c in sorted(df["Country"].unique())],
            value="Uganda",
            id="country-dropdown"
        ),
    ], style={"width": "40%", "margin": "auto"}),

    html.Br(),

    # Dynamic graph based on country
    dcc.Graph(id="life-expectancy-trend"),

    html.Div([
        # Static graphs
        dcc.Graph(id="scatter-gdp-schooling"),
        dcc.Graph(id="heatmap-correlation")
    ], style={"display": "flex", "flexWrap": "wrap"}),

], style={"padding": "20px"})


# Callback: Line plot updates with country selection
@app.callback(
    Output("life-expectancy-trend", "figure"),
    Input("country-dropdown", "value")
)
def update_life_expectancy_plot(selected_country):
    dff = df[df["Country"] == selected_country]
    fig = px.line(dff, x="Year", y="Life expectancy",
                  title=f"📈 Life Expectancy Over Time: {selected_country}")
    return fig


# Scatter plot: Static (GDP vs Schooling vs Life Expectancy)
@app.callback(
    Output("scatter-gdp-schooling", "figure"),
    Input("country-dropdown", "value")  # Just to trigger render; you can remove if preferred
)
def scatter_gdp_schooling(_):
    fig = px.scatter_3d(df, x="GDP", y="Schooling", z="Life expectancy",
                        color="Status", title="💰 GDP vs 🎓 Schooling vs 🧬 Life Expectancy")
    return fig


# Heatmap: Static (correlation)
@app.callback(
    Output("heatmap-correlation", "figure"),
    Input("country-dropdown", "value")  # Just to refresh on change
)
def heatmap_correlation(_):
    corr = df.select_dtypes(include='number').corr()
    fig = px.imshow(corr, text_auto=True, title="📊 Correlation Heatmap")
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
