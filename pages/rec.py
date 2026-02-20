from dash import html
import dash_mantine_components as dmc

from dash import html, dcc
import dash_mantine_components as dmc

from components.description import description
from components.cards import top_cards

rec = html.Div(
    [
        top_cards,
        html.Div(
            [
                html.Div(
                    [
                        dmc.Text("Do not proceed", fw=700, c="#c92a2a"),
                        dmc.Text("Recommendation", c="gray"),
                        dmc.Text(
                            """
                    In an A/B test, we check for two things: 1. which group performed better? and 2. was this improvement statistically significant? Since
                    the first check fails, we do not proceed to the second step, and we can conclude that it would not be advisable to implement this new feature.
                    Furthermore, because of the large sample size analyxed (n ~= 300,000), we can be reaosnably sure that this data was not anomalistic, and that
                    we would likely get similar results were we to repeat the test without changing the test variant. Therefore, this analysis recommends further ideation
                    around landing page variants to increase conversion rate in a way that is statistically significant.
                """,
                            c="black",
                            className="overview-p",
                        ),
                    ],
                    className="overview-txt",
                ),
            ],
            className="overview-lyt all-minwidth",
        ),
    ],
)
