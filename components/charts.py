import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.proportion import confint_proportions_2indep

from components.data import online, permutation_df


def intro_pie(tests_passed, tests_failed):

    v1 = tests_passed
    v2 = tests_failed

    return (
        px.pie(
            values=[v1, v2],
            names=["Passed", "Failed"],
            hole=0.6,
            color_discrete_sequence=["#c92a2a", "#2b8a3e"],
        )
        .update_traces(textposition="inside", texttemplate="%{percent}")
        .add_annotation(
            {
                "text": f"{(v1/(v1+v2))*100:.0f}%",
                "x": 0.5,
                "y": 0.5,
                "font": {"size": 20, "color": "black"},
                "showarrow": False,
                "xref": "paper",
                "yref": "paper",
            }
        )
        .update_layout({"title": {"text": f"{(v1/(v1+v2))*100:.0f}% of tests passed"}})
    )


def intro_gauge():

    control_rate = online.query("group == 'control'")["converted"].mean()
    treatment_rate = online.query("group == 'treatment'")["converted"].mean()
    d_min = 0.02

    absolute_lift = treatment_rate - control_rate
    relative_lift_pct = (absolute_lift / control_rate) * 100
    d_min_relative_pct = (d_min / control_rate) * 100
    distance_from_target = abs(relative_lift_pct - d_min_relative_pct)

    fig = (
        go.Figure(
            go.Indicator(
                mode="gauge+number+delta",
                value=relative_lift_pct,
                number={"font": {"size": 12, "color": "white"}},
                # title={"text": "Relative lift vs threshold", "font": {"size": 24}},
                gauge={
                    "bar": {"color": "#1616a7"},
                    "axis": {"range": [-10, 20], "ticksuffix": "%"},
                    "steps": [
                        {"range": [-10, 0], "color": "lightcoral"},
                        {"range": [0, d_min_relative_pct], "color": "lightyellow"},
                        {"range": [d_min_relative_pct, 40], "color": "lightgreen"},
                    ],
                    "threshold": {
                        "line": {"color": "red", "width": 4},
                        "thickness": 0.75,
                        "value": d_min_relative_pct,
                    },
                },
            )
        )
        .add_annotation(
            text=f"▼ {abs(relative_lift_pct):.2f}%",
            x=0.5,
            y=0.3,
            xref="paper",
            yref="paper",
            showarrow=False,
            bgcolor="white",
            font=dict(size=36, color="#1616a7"),
        )
        .add_annotation(
            text=f"-{distance_from_target:.2f}% from target",
            x=0.5,
            y=0.2,
            xref="paper",
            yref="paper",
            showarrow=False,
            bgcolor="white",
            font=dict(size=18, color="red"),
        )
        .add_annotation(
            text="Relative lift vs threshold",
            x=0.5,
            y=1.0,
            xref="paper",
            yref="paper",
            font={"size": 24},
            showarrow=False,
        )
    )

    return fig.update_layout(height=400, font={"size": 16})


def slice_distributions():
    # sample statistics
    n = len(online)
    p = online["group_bin"].mean()
    observed_mean = n * p
    std = np.sqrt(n * p * (1 - p))
    x_min = int(max(0, observed_mean - 4 * std))
    x_max = int(min(n, observed_mean + 4 * std))

    # binomial distribution
    x = np.arange(x_min, x_max)
    pmf = stats.binom.pmf(x, n, p)

    # bar counts
    vc = online["group_bin"].value_counts()

    # figure
    bigfig = make_subplots(
        1,
        2,
        column_widths=[0.25, 0.75],
        subplot_titles=("Failures and successes", "Binomial distribution"),
    )

    #  add bar
    bigfig.add_trace(
        go.Bar(
            x=[0, 1],
            y=vc.values,
            showlegend=False,
            marker={"color": "#4c78a8"},
            name="group_bin",
        ),
        row=1,
        col=1,
    )

    # add binom distribution
    bigfig.add_trace(
        go.Scattergl(
            x=x,
            y=pmf,
            mode="lines",
            fill="tozeroy",
            opacity=0.7,
            marker={"color": "#4c78a8"},
            name="conversion",
        ),
        row=1,
        col=2,
    ).add_vline(
        x=observed_mean,
        line_dash="solid",
        line_color="green",
        line_width=1,
        annotation_text=f"observed mean<br>{observed_mean:.2f}",
        row=1,
        col=2,
    )

    return bigfig.update_layout(
        {
            "title": {"text": ""},
            "xaxis1": {"title": {"text": "Success"}},
            "yaxis1": {"title": {"text": "Counts"}},
            "xaxis2": {"title": {"text": "Number of successes"}},
            "yaxis2": {"title": {"text": "Probability"}},
            "template": "plotly_white",
        }
    ).update_xaxes(
        {
            "tickvals": [0, 1],
            "ticktext": ["Failure", "Success"],
        },
        row=1,
        col=1,
    )


def slice_time_scatter(time_colstr="Day", agg_func="sum"):

    gb_time = (
        online.groupby([time_colstr, "group"])
        .agg({"converted": agg_func})
        .reset_index()
    )
    if time_colstr == "Weekday":
        weekday_order_lst = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        gb_time["Weekday"] = pd.Categorical(
            gb_time["Weekday"], categories=weekday_order_lst, ordered=True
        )
        gb_time = gb_time.sort_values("Weekday")

    group_msk = gb_time["group"] == "control"

    fig = go.Figure()

    color_lst = px.colors.qualitative.T10

    fig.add_trace(
        go.Scatter(
            x=gb_time.loc[group_msk, time_colstr],
            y=gb_time.loc[group_msk, "converted"],
            mode="lines+markers",
            marker={"color": color_lst[5]},
            name="control",
        )
    ).add_trace(
        go.Scatter(
            x=gb_time.loc[~group_msk, time_colstr],
            y=gb_time.loc[~group_msk, "converted"],
            mode="lines+markers",
            marker={"color": color_lst[1]},
            name="treatment",
        )
    ).update_layout(
        {
            "title": {"text": f"conversions by group, {time_colstr}"},
            "xaxis": {
                "title": {"text": time_colstr},
            },
            "yaxis": {"title": {"text": f"Sum of conversions per {time_colstr}"}},
            "template": "plotly_white",
        }
    )

    if time_colstr == "Weekday":
        fig.update_layout(
            {
                "xaxis": {
                    "categoryorder": "array",
                    "categoryarray": [
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday",
                        "Sunday",
                    ],
                }
            }
        )

    return fig


def z_test():

    # Calculate test results
    convert_old = online.query("group == 'control'")["converted"]
    convert_new = online.query("group == 'treatment'")["converted"]

    n_old = len(convert_old)
    n_new = len(convert_new)

    count_old = convert_old.sum()
    count_new = convert_new.sum()

    rate_old = count_old / n_old
    rate_new = count_new / n_new
    observed_diff = rate_new - rate_old

    # Two-proportion z-test
    z_stat, p_val = sm.stats.proportions_ztest(
        [count_new, count_old], [n_new, n_old], alternative="two-sided"
    )

    # Generate standard normal distribution (null hypothesis)
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)  # Standard normal (mean=0, std=1)

    # Create figure
    fig = go.Figure()

    # Plot null distribution
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            fill="tozeroy",
            line=dict(color="lightblue"),
            showlegend=False,
            name="Null Distribution",
        )
    )

    # Add observed z-statistic
    fig.add_vline(
        x=z_stat,
        line_color="#c92a2a",
        line_width=3,
        annotation_text=f"Observed Z = {z_stat:.3f}",
    ).add_vline(
        x=0,
        line_color="black",
        line_width=2,
        line_dash="dash",
        annotation_text="expected: 0",
        annotation_position="top",
    )
    # Add critical values for alpha=0.05 (two-sided)
    z_critical = 1.96
    fig.add_vline(
        x=z_critical,
        line_dash="dash",
        line_color="yellow",
        annotation_text=f"Critical = {z_critical}",
    )
    fig.add_vline(x=-z_critical, line_dash="dash", line_color="yellow")

    # Shade rejection regions
    fig.add_vrect(
        x0=-4,
        x1=-z_critical,
        fillcolor="green",
        opacity=0.1,
        annotation_text="Reject",
        annotation_position="top left",
    )
    fig.add_vrect(
        x0=z_critical,
        x1=4,
        fillcolor="green",
        opacity=0.1,
        annotation_text="Reject",
        annotation_position="top right",
    )

    # Add p-value annotation
    fig.add_annotation(
        text=f'P-value = {p_val:.4f}<br>{"Significant" if p_val < 0.05 else "Not significant"}',
        x=-0.76,
        y=0.35,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
    )

    fig.update_layout(
        title="Two-proportion z-test results",
        xaxis_title="Z-statistic",
        yaxis_title="Probability density",
        template="plotly_white",
        showlegend=True,
    )

    return fig


def ci_chart():

    # Calculate test results - CONTROL FIRST
    convert_old = online.query("group == 'control'")["converted"]
    convert_new = online.query("group == 'treatment'")["converted"]

    n_old = len(convert_old)
    n_new = len(convert_new)

    count_old = convert_old.sum()
    count_new = convert_new.sum()

    rate_old = count_old / n_old
    rate_new = count_new / n_new

    # Observed difference - CONTROL FIRST
    observed_diff = rate_new - rate_old  # ← Changed to control - treatment

    # Confidence interval - CONTROL FIRST
    ci_low, ci_high = confint_proportions_2indep(
        count_new,
        n_new,  # ← Control first
        count_old,
        n_old,  # ← Treatment second
        method="wald",
        alpha=0.05,
    )

    # Create figure
    fig = go.Figure()

    # Add horizontal line for CI
    fig.add_trace(
        go.Scatter(
            x=[ci_low, observed_diff, ci_high],
            y=[0, 0, 0],
            mode="lines+markers",
            line=dict(color="#c92a2a", width=3, dash="dash"),
            marker=dict(size=10),
            name="95% CI",
            showlegend=False,
        )
    )

    # Add null hypothesis line (0)
    fig.add_vline(
        x=0,
        line_color="black",
        line_width=2,
        line_dash="solid",
        annotation_text="Null (no difference)",
        annotation_position="top",
    )

    # Add practical significance boundary (if you have d_min)
    # Assuming d_min = 0.01 (1 percentage point)
    d_min = 0.02
    fig.add_vline(
        x=-d_min,
        line_dash="dash",
        line_color="yellow",
    )
    fig.add_vline(
        x=d_min,
        line_dash="dash",
        annotation_text=f"practical significance = {d_min}",
        line_color="yellow",
        annotation_position="top",
    )

    # Shade region around null
    fig.add_vrect(
        x0=-0.05,
        x1=-0.02,
        fillcolor="green",
        opacity=0.05,
        annotation_text="New performed worse",
        annotation_position="top left",
    )
    fig.add_vrect(
        x0=0.02,
        x1=0.05,
        fillcolor="green",
        opacity=0.05,
        annotation_text="New performed better",
        annotation_position="top right",
    )

    # Add annotations
    fig.add_annotation(
        text=f"Observed: {observed_diff:.4f}<br>95% CI: [{ci_low:.4f}, {ci_high:.4f}]",
        # xref='paper', yref='paper',
        x=-0.004,
        y=-0.5,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
        align="left",
    )

    fig.update_layout(
        title="95% confidence interval for difference in conversion rates",
        xaxis_title="Difference in conversion rate",
        yaxis=dict(showticklabels=False, range=[-1, 1]),
        template="plotly_white",
        height=300,
        xaxis=dict(zeroline=True, zerolinewidth=2, zerolinecolor="black"),
    )

    return fig


def sign_test():

    daily_stats = (
        online.groupby("Date")
        .apply(
            lambda x: pd.Series(
                {
                    "control_rate": x.query("group == 'control'")["converted"].mean(),
                    "treatment_rate": x.query("group == 'treatment'")[
                        "converted"
                    ].mean(),
                }
            )
        )
        .reset_index()
    )

    daily_stats["diff"] = daily_stats["treatment_rate"] - daily_stats["control_rate"]

    n_pos = (daily_stats["diff"] > 0).sum()
    n_neg = (daily_stats["diff"] < 0).sum()
    n_zero = (daily_stats["diff"] == 0).sum()
    n_tot = len(daily_stats)

    sign_res = stats.binomtest(n_pos, n_tot - n_zero, p=0.5, alternative="two-sided")

    g0_msk = daily_stats["diff"] > 0

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=daily_stats.loc[g0_msk, "Date"],
            y=daily_stats.loc[g0_msk, "diff"],
            marker={"color": "#2b8a3e"},
            name="Treatment performed better",
        )
    ).add_trace(
        go.Bar(
            x=daily_stats.loc[~g0_msk, "Date"],
            y=daily_stats.loc[~g0_msk, "diff"],
            marker={"color": "#c92a2a"},
            name="Treatment performed worse",
        )
    ).add_annotation(
        text=f"Binomial sign test statistic = {round(sign_res.statistic, 4)}<br>P-value = {round(sign_res.pvalue, 4)}",
        x="2017-01-5",
        y=0.015,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
    ).update_layout(
        {
            "title": {"text": "Difference in mean conversion rate, all 20 days"},
            "xaxis": {"title": {"text": "Date"}},
            "yaxis": {"title": {"text": "Difference in mean conversion rate"}},
            "template": "plotly_white",
        }
    )

    return fig


def permutation_test():

    # Create histogram of permuted differences
    # permutation_diffs_arr = permutation_test.values.flatten()
    permuted_diffs_arr = permutation_df.values.flatten()

    convert_old = online.query("group == 'control'")["converted"]
    convert_new = online.query("group == 'treatment'")["converted"]

    n_old = len(convert_old)
    n_new = len(convert_new)

    count_old = convert_old.sum()
    count_new = convert_new.sum()

    rate_old = count_old / n_old
    rate_new = count_new / n_new
    observed_diff = rate_new - rate_old

    perm_pval = (np.abs(permuted_diffs_arr) < np.abs(observed_diff)).mean()

    fig = go.Figure()

    # Histogram of null distribution
    fig.add_trace(
        go.Histogram(
            x=permuted_diffs_arr,
            nbinsx=50,
            name="Permutation Distribution",
            marker=dict(color="lightblue"),
            opacity=0.7,
        )
    )

    # Add observed difference
    fig.add_vline(
        x=observed_diff,
        line_color="#c92a2a",
        line_width=3,
        annotation_text=f"Observed: {observed_diff:.4f}",
    ).add_vline(
        x=0,
        line_color="black",
        line_width=2,
        line_dash="dash",
        annotation_text="expected: 0",
        annotation_position="top",
    )
    # Add critical values (approximate 95% CI from permutations)
    lower_critical = np.percentile(permuted_diffs_arr, 2.5)
    upper_critical = np.percentile(permuted_diffs_arr, 97.5)

    fig.add_vline(
        x=lower_critical,
        line_color="yellow",
        line_width=2,
        line_dash="dash",
        annotation_text="lower critical",
        annotation_position="bottom left",
    )

    fig.add_vline(
        x=upper_critical,
        line_color="yellow",
        line_width=2,
        line_dash="dash",
        annotation_text="upper critical",
        annotation_position="bottom right",
    )

    # Shade rejection regions
    fig.add_vrect(
        x0=permuted_diffs_arr.min(), x1=lower_critical, fillcolor="green", opacity=0.1
    )

    fig.add_vrect(
        x0=upper_critical, x1=permuted_diffs_arr.max(), fillcolor="green", opacity=0.1
    )

    # Add p-value annotation
    fig.add_annotation(
        text=f"P-value = {perm_pval:.4f}<br>Permutations = 10,000",
        # xref='paper', yref='paper',
        x=-0.00115,
        y=580,
        showarrow=False,
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
        align="right",
    )

    fig.update_layout(
        title="Permutation test",
        xaxis_title="Difference in conversion rates",
        yaxis_title="Frequency",
        template="plotly_white",
        height=400,
    )

    return fig
