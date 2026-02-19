from dash import html, dcc
import dash_mantine_components as dmc

from components.assumptions import assumptions
from components.cards import top_cards
from components.charts import permutation_test
from components.color import lyt
from components.description import description
from components.result import result

text_lst = [
    """
    The permutation test is similar to bootstrapping. It puts the control and treatment data in one basket, then randomly samples (without replacement) from this basket, and calculates the number of times a result is at least as extreme as when the data were separated.
    """,
    """
    In this simulation, the permutation test was run 10,000 times.
    """,
]

assumptions_dct = {
    "Exchangeability under the null hypothesis": True,
    "Independence of observations": True,
}


perm = html.Div(
    [
        top_cards,
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [description(text_lst, "z-th-left")],
                            className="in",
                        ),
                        html.Div(
                            [
                                assumptions(assumptions_dct, "z-th-right"),
                            ],
                            className="in",
                        ),
                    ],
                    className="z-tophalf",
                ),
                dmc.Card(
                    [dcc.Graph(figure=lyt(permutation_test()), className="z-chart")],
                    withBorder=True,
                    radius="md",
                    className="z-bottomhalf",
                ),
            ],
            className="z",
        ),
        result(False),
    ],
)
