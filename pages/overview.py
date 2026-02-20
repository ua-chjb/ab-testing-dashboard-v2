from dash import html
import dash_mantine_components as dmc

progress = html.Div(
    [
        html.Div(
            [
                dmc.Text("Landing page: A/B testing", fw=700, c="black"),
                dmc.Text("Step 5: statistical analysis of results", c="gray"),
                dmc.Text(
                    """
                This dashboard provides an interactive look at a simulated dataset of a landing page. Run over
                a period of 22 days, with two versions (new, control), there was not a statistically significant
                difference between the two groups. Furthermore, this analysis determined the conversion rate actually
                decreased with the new variant, with an effect size of -0.1578%. Generally, this analysis 
                recommends not moving forward with implementation; more specifically, it is also recommended to
                not engage in further testing without first adjusting the variant in question.
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
                    title="Business impact",
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
                dmc.TimelineItem(
                    title="Implementation",
                    bullet=dmc.Text(6, p=10, fw=500),
                    children=[dmc.Text("Implement new feature", size="sm", c="dimmed")],
                ),
            ],
        ),
    ],
    className="overview-lyt all-minwidth",
)
