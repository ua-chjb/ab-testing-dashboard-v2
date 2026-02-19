from dash import html, dcc
import dash_mantine_components as dmc

from components.cards import top_cards
from components.charts import slice_distributions
from components.color import lyt
from components.data import online

slice = html.Div(
    [
        top_cards,
        dmc.Card(
            [dcc.Graph(figure=lyt(slice_distributions()))],
            withBorder=True,
            radius="md",
            className="slice-tophalf",
        ),
        html.Div(
            [
                html.Div(
                    [
                        dmc.Card(
                            [
                                dmc.Select(
                                    label="Time slice",
                                    value="Day",
                                    data=["Day", "Weekday", "Hour", "Minute"],
                                    clearable=False,
                                    id="slice_time_IN0",
                                ),
                                dmc.Select(
                                    label="Aggregation function",
                                    value="sum",
                                    data=["sum", "mean"],
                                    clearable=False,
                                    id="slice_time_IN1",
                                ),
                            ],
                            withBorder=True,
                            radius="sm",
                            className="slice-bh-left",
                        ),
                    ],
                    className="in",
                ),
                dmc.Card(
                    [
                        dcc.Graph(figure={}, id="slice_time_OUT"),
                    ],
                    withBorder=True,
                    radius="md",
                    className="slice-bh-right",
                ),
            ],
            className="slice-bottomhalf",
        ),
    ]
)
