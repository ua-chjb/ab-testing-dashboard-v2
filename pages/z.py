from dash import html, dcc
import dash_mantine_components as dmc

from components.assumptions import assumptions
from components.cards import top_cards
from components.charts import z_test
from components.color import lyt
from components.description import description
from components.result import result

text_lst = [
    """
    The standard test for a binomial distribution is the two-proportions z-test. It is applied here with the parameters above. In addition, several assumptions need to be met, which are detailed below.
    """,
    """
    In the null hypothesis, we would expect the difference to be within 1.96 standard deviations away from 0. The observed z-statistic is -1.311. The fact that it is negative states that the new test actually performed worse than the new test; the fact that it is within [-1.96, 1.96] states that the result is not statistically significant.
    """,
]

assumptions_dct = {
    "Independence, both within and between groups": True,
    "Random assignment to control/treatment": True,
    "Sample size: n*p and n*(1-p) >= 10 for both groups": True,
}

z = html.Div(
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
                    [dcc.Graph(figure=lyt(z_test()), className="z-chart")],
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
