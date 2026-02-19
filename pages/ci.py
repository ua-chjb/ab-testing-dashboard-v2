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
    The confidence interval is another standard measure to determine how likely one sample is to contain the mean of another sample.
    """,
    """
    There are three things to look for: 1. does the confidence interval intersect with zero? If so, there is no significant difference between the two samples, and the test fails. 2. Is the observed difference to the left or the right of zero? This calculation uses (new - old), so if the difference is positive, the experiment was an improvement; if the difference is negative, the experiment performed worse. Finally, 3. are both the observed difference and the confidence interval beyond the practical significance threshold? This will tell you if the experiment performed well enough to justify the operational costs of implementation.
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
