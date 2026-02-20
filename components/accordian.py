from dash import html
import dash_mantine_components as dmc


def accordion_hidden(header, passed_failed, color):
    return dmc.AccordionControl(
        [
            html.Div(
                [
                    dmc.Text(header, size="xl", fw=700),
                    dmc.Badge(
                        passed_failed,
                        variant="filled",
                        color=color,
                        c="white",
                        size="sm",
                    ),
                ]
            )
        ]
    )


def accordion_displayed(text):
    if isinstance(text, list):
        return dmc.AccordionPanel(
            dmc.List([dmc.ListItem(dmc.Text(t, size="sm")) for t in text])
        )
    return dmc.AccordionPanel(dmc.Text(text, size="sm"))


def full_accordion(id, header, passed_failed, text):
    if passed_failed == "Passed":
        color = "#2b8a3e"
    else:
        color = "#c92a2a"
    return dmc.AccordionItem(
        [accordion_hidden(header, passed_failed, color), accordion_displayed(text)],
        value=id,
    )
