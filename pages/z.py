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
    The standard test for a binomial distribution is the two-proportions z-test. It is applied here with the parameters above. In addition, several assumptions need to be met, which are detailed to the right.
    """,
    """
    In the null hypothesis assumes the difference is zero. We would expect the difference to be within 1.96 standard deviations of the null -- if the difference is less than that, we cannot reject the null hypothesis. Because the observed z-statistic is -1.311, we fail to reject the null, and conclude there is not a statistically significant difference between the two groups.
    """,
    """
    Furthermore, the fact that the test statistic is negative tells us that the new test actually performed worse than the control variant.
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
