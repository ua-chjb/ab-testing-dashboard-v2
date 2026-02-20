from dash import Input, Output, State, ctx

from components.charts import slice_time_scatter
from components.color import lyt
from components.content import content_map, headers_map


def switchboard(app):
    @app.callback(
        Output("url", "href"),
        Input("logout_button_IN", "n_clicks"),
        prevent_initial_call=True,
    )
    def logout(n_clicks):
        return "/logout"

    @app.callback(
        Output("drawer_OUT", "opened"),
        Input("drawer_IN", "n_clicks"),
        State("drawer_OUT", "opened"),
        prevent_initial_call=True,
    )
    def all_drawer_usestate(n_clicks, opened):
        return True

    @app.callback(
        Output("main-content", "children"),
        Output("header_OUT", "children"),
        Output("drawer_OUT", "opened", allow_duplicate=True),
        Output("active-page", "data"),
        Input("nav-overview", "n_clicks"),
        Input("nav-intro", "n_clicks"),
        Input("nav-slice", "n_clicks"),
        Input("nav-t", "n_clicks"),
        Input("nav-ci", "n_clicks"),
        Input("nav-sign", "n_clicks"),
        Input("nav-permutation", "n_clicks"),
        Input("nav-rec", "n_clicks"),
        prevent_initial_call=True,
    )
    def all_navigate(overview, intro, slice, t, ci, sign, permutation, rec):
        triggered_id = ctx.triggered_id
        content = content_map.get(triggered_id, content_map["nav-overview"])
        header = headers_map.get(triggered_id, headers_map["nav-overview"])
        page_id = triggered_id.replace("nav-", "") if triggered_id else "overview"
        return content, header, False, page_id

    @app.callback(
        Output("main-content", "children", allow_duplicate=True),
        Output("header_OUT", "children", allow_duplicate=True),
        Output("active-page", "data", allow_duplicate=True),
        Input("home_button_IN", "n_clicks"),
        prevent_initial_call=True,
    )
    def all_home_affix(n_clicks):
        return (content_map["nav-intro"], headers_map["nav-intro"], "intro")

    @app.callback(
        Output("slice_time_OUT", "figure"),
        Input("slice_time_IN0", "value"),
        Input("slice_time_IN1", "value"),
    )
    def slice_time_chart(time_col, agg_func):
        return lyt(slice_time_scatter(time_col, agg_func))
