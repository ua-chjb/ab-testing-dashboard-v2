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
    The sign test calculates how many "wins" were observed in each variant. This is analyze per unit of time; in this case, the time dimension is in days. So, how many days did the control have a better mean conversion rate than the test?
    """,
    """
    The below chart shows test wins colored in green, and contorl wins colored in red. In total, treatment exceeded control 7 times, and control exceeded treatment 16 times. Again, we see that the test performed worse -- though not significantly so.
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
