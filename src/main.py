from dash import Dash, html

# Step 1: Create Dash application
app = Dash(__name__)

# Step 2: Create layout
app.layout = html.Div([
    html.H1("Welcome to Python Dash"),
    html.P("My First Interactive Dashboard"),
    html.H2("Learning Dash Framework")
])

# Step 3: Run application
if __name__ == "__main__":
    app.run(debug=True)