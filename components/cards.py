import dash_mantine_components as dmc
from components.card import card

top_cards = dmc.Group(
    [
        card(0.05, "alpha parameter, equivalent to 95% confidence", "#4dabf7"),
        card(0.20, "beta parameter, equivalent to 80% power", "#4dabf7"),
        card(f"2% lift", "practical significance threshold", "#4dabf7"),
        card(f"290,584", "total data points", "#4dabf7"),
        card(22, "days in the test", "#4dabf7"),
    ],
    className="intro-lyt",
    gap="xs",
)
