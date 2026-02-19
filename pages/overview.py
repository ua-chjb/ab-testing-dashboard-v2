from dash import html
import dash_mantine_components as dmc

progress = html.Div(
    [
        html.Div(
            [
                dmc.Text("A/B test process", fw=700, c="black"),
                dmc.Text("Step 5: statistical analysis of results", c="gray"),
                dmc.Text(
                    """
                This dashboard provides an interactive look at the A/B test recently run on Udacity, 
                from 1/2/2017 - 1/24/2017, over a period of 22 days, and tracked the actions of 290,584 
                unique users. The effect size was -0.001578%, meaning the conversion rate for the treatment 
                group was 0.16% worse than the conversion rate for the control group. Generally, this test 
                recommends not moving forward with implementation; specifically, the treatment group performed
                worse across 4/4 statistical tests, yet the results were not statistically significant. More detail
                can be found on further pages.
                """,
                    c="black",
                    className="overview-p",
                ),
            ],
            className="overview-txt",
        ),
        dmc.Timeline(
            active=3,
            bulletSize=24,
            lineWidth=5,
            variant="outline",
            children=[
                dmc.TimelineItem(
                    title="Data deep dive",
                    bullet=dmc.Text(1, p=10, fw=500),
                    children=[dmc.Text("Historical analysis", size="sm", c="dimmed")],
                ),
                dmc.TimelineItem(
                    title="Business alignment",
                    bullet=dmc.Text(2, p=10, fw=500),
                    children=[
                        dmc.Text("Potential impact on revenue", size="sm", c="dimmed")
                    ],
                ),
                dmc.TimelineItem(
                    title="Design test",
                    bullet=dmc.Text(3, p=10, fw=500),
                    children=[dmc.Text("Set test parameters", size="sm", c="dimmed")],
                ),
                dmc.TimelineItem(
                    title="Implementation",
                    bullet=dmc.Text(4, p=10, fw=500),
                    children=[dmc.Text("Implement feature", size="sm", c="dimmed")],
                ),
                dmc.TimelineItem(
                    title="Statistical analysis",
                    bullet=dmc.Text(5, p=10, fw=500),
                    children=[dmc.Text("Analyze results", size="sm", c="dimmed")],
                ),
            ],
        ),
    ],
    className="overview-lyt all-minwidth",
)
