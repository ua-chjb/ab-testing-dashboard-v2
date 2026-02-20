from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def result(passed):
    return html.Div(
        [
            dmc.Card(
                [
                    html.Div(
                        [
                            dmc.Text("Passed" if passed else "Failed", fw=700),
                            DashIconify(
                                icon=(
                                    "mdi-check-circle" if passed else "mdi-close-circle"
                                ),
                                color="#2b8a3e" if passed else "#c92a2a",
                                width=100,
                            ),
                        ],
                        className="res-center",
                    )
                ],
                withBorder=True,
                radius="md",
                className="res-main",
            )
        ],
        className="res-outer",
    )
