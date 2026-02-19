from dash import html
import dash_mantine_components as dmc

from dash import html, dcc
import dash_mantine_components as dmc

from components.description import description
from components.cards import top_cards

rec = html.Div(
    [
        top_cards,
        dmc.Accordion(
            chevronPosition="right",
            variant="contained",
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl(
                            dmc.Text(
                                "Do not proceed",
                                c="#c92a2a",
                                className="rec-tit",
                                fw=800,
                            ),
                        ),
                        dmc.AccordionPanel(
                            dmc.Text(
                                """
                                We are essentialy checking for two things here: 1. Which group performed better, and 2. was 
                                that differrence statiscally insignificant. We went 0/2 on all four tests. The effect size -- 
                                the difference in mean conversion rate -- was negative, indicating
                                that the new design actually performed worse. In addition, none of these differences were statistically
                                significant. Due to large sample size, one could reasonably assume that these statistics are a valid representation
                                of user behavior on the site; therefore, desppite the lack of stat sig, I would recommend against 
                                re-doing the experiment to father more data. Instead,  I would recommend going "back to the drawing board", including
                                potentially leveraging focus groups or user experience research sessions to optimize pain points of the current interface
                                and create something the users really like.
                                """,
                                p=0,
                            )
                        ),
                    ],
                    value="recommendation",
                )
            ],
            className="rec-all",
        ),
    ]
)
