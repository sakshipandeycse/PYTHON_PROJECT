
from dash import Dash, html, Input, Output, dcc
import plotly.express as px

# Step 1: Load dataset
df = px.data.iris()

# Step 2: Create Dash application
app = Dash(__name__)

# Step 3: Define Layout
app.layout = html.Div([
    html.H1("Iris Flower Analysis Dashboard"),

    html.Label("Select Flower Species"),

    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {"label": "Setosa", "value": "setosa"},
            {"label": "Versicolor", "value": "versicolor"},
            {"label": "Virginica", "value": "virginica"}
        ],
        value="setosa",
        clearable=False
    ),

    dcc.Graph(id="iris_graph")
])

# Step 4: Define Callback
@app.callback(
    Output("iris_graph", "figure"),
    Input("species_dropdown", "value")
)
def update_graph(selected_species):
    filtered_df = df[df["species"] == selected_species]

    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title="Iris Flower Analysis"
    )

    return fig

# Step 5: Run application
if __name__ == "__main__":
    app.run(debug=True)
