from dash import html, dcc
import dash_mantine_components as dmc

from components.accordian import full_accordion
from components.cards import top_cards
from components.charts import intro_gauge
from components.color import lyt

intro = html.Div(
    [
        top_cards,
        html.Div(
            [
                dmc.Card(
                    [
                        dcc.Graph(
                            figure=lyt(intro_gauge()).update_layout(
                                {"margin": {"t": 50, "r": 50, "b": 50, "l": 50}}
                            )
                        )
                    ],
                    withBorder=True,
                    radius="md",
                    className="intro-pie",
                ),
                dmc.Accordion(
                    chevronPosition="right",
                    variant="contained",
                    children=[
                        full_accordion(
                            "z",
                            "Two-proportion z-test",
                            "Failed",
                            [
                                "Z-statistic = -1.311",
                                "P-value = 0.1899",
                            ],
                        ),
                        full_accordion(
                            "ci",
                            "Confidence interval",
                            "Failed",
                            "CI: [-0.0039, 0.0008]",
                        ),
                        full_accordion(
                            "sign",
                            "Sign test",
                            "Failed",
                            [
                                "Binomial sign test statistic = 0.3043",
                                "P-value = 0.0931",
                            ],
                        ),
                        full_accordion(
                            "permutation",
                            "Permutation test",
                            "Failed",
                            ["Permutations = 10,000", "P-value = 0.8120"],
                        ),
                    ],
                ),
            ],
            className="intro-not-cards all-minwidth",
        ),
    ]
)
