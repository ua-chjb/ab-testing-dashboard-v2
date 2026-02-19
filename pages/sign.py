from dash import html, dcc
import dash_mantine_components as dmc

from components.assumptions import assumptions
from components.cards import top_cards
from components.charts import sign_test
from components.color import lyt
from components.description import description
from components.result import result

text_lst = [
    """
    The sign test calculates how many "wins" were observed in each group, per unit of time (in this case, days). So, how many days did treatment win vs control?
    """,
    """
    The below chart shows treatment wins colored in green, and contorl wins colored in red. In total, treatment exceeded control 7 times, and control exceeded treatment 16 times.
    """,
]

assumptions_dct = {
    "Independence of pairs/days": True,
    "Binary outcome per unit": True,
    "Random assignment to control/treatment": True,
}


sign = html.Div(
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
                    [dcc.Graph(figure=lyt(sign_test()), className="z-chart")],
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
