from dash_iconify import DashIconify
import dash_mantine_components as dmc


def assumptions(assumptions_dct, className):

    assumptions_lst = [
        dmc.ListItem(
            text,
            icon=DashIconify(
                icon="mdi-check-circle" if passed else "mdi-close-circle",
                color="#2b8a3e" if passed else "#c92a2a",
            ),
        )
        for text, passed in assumptions_dct.items()
    ]
    return dmc.Card(
        [
            dmc.Text("Assumptions", size="sm", fw=700, mb="sm"),
            dmc.List(assumptions_lst, type="unordered", size="md", spacing="xs"),
        ],
        w="auto",
        withBorder=True,
        radius="md",
        className=className,
    )
