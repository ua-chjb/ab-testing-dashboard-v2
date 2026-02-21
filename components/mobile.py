from dash import html
import dash_mantine_components as dmc

mobile = html.Div(
    [
        dmc.Text("Please access from a desktop or tablet.", className="mobile-warning"),
    ]
)
