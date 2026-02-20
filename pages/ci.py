from dash import html, dcc
import dash_mantine_components as dmc

from components.assumptions import assumptions
from components.cards import top_cards
from components.charts import ci_chart
from components.color import lyt
from components.description import description
from components.result import result

text_lst = [
    """
    The confidence interval is another standard measure of difference.
    """,
    """
    The first thing to check is: does the confidence interval contain zero? If so, there is no significant difference between the two samples, and the test fails. That is what happens here. Additionally, as we saw in our two-proportions z-test, the observed difference was negative, indicating the new variant performed worse than the control. 
    """,
    """
    The final aspect to analyze -- although it does not apply here, as our confidence interval contained zero -- is whether or not the CI was beyond the bounds of our practical significance threshold. This tells you if the experiment performed well enough to justify the operational costs of implementation.
    """,
]

assumptions_dct = {
    "Independence, both within and between groups": True,
    "Random assignment to control/treatment": True,
}


ci = html.Div(
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
                    [dcc.Graph(figure=lyt(ci_chart()), className="z-chart")],
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
