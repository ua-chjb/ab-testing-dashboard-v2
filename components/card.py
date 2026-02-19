from dash import html
import dash_mantine_components as dmc

def card(number, text, color):
    return dmc.Card(
        [
            dmc.CardSection(    
                dmc.Text(f"{number}", size="xl", c=color, fw=700, className="card-p")
            ),
            dmc.CardSection(    
                dmc.Text(text, size="sm", c="white", className="card-p card-subheader"),
                style={"backgroundColor": color, "flex": 1}
            )        
        ], 
    withBorder=True,
    shadow="sm",
    radius="md",
    w=150,
    className="card"
    )