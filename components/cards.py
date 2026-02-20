import dash_mantine_components as dmc
from components.card import card

top_cards = dmc.Group(
    [
        card(0.05, "alpha parameter, equivalent to 95% confidence", "#228be6 "),
        card(0.20, "beta parameter, equivalent to 80% power", "#228be6 "),
        card(f"2% lift", "practical significance threshold", "#228be6 "),
        card(f"290,584", "total data points", "#228be6 "),
        card(22, "days in the test", "#228be6 "),
    ],
    className="intro-lyt",
    gap="xs",
)
