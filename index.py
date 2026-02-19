from dash import html, dcc, _dash_renderer
from dash_iconify import DashIconify
import dash_mantine_components as dmc
_dash_renderer._set_react_version("18.2.0")

from components.content import overview_content
from components.nav import Nav

Header = html.Div([
    dmc.Group([
        dmc.ActionIcon(
            DashIconify(icon="mingcute:menu-fill", width=20),
            variant="filled",
            color="blue",
            id="drawer_IN",
            className="nav-hamburger"
        ),
        html.Div(
            dmc.Title("Overview", order=2, c="#228be6"),
            id="header_OUT", 
            className="nav-header"
        )
    ], gap="md", mb="lg"),
    
    dmc.Drawer(
        children=Nav,
        title="Menu",
        id="drawer_OUT",
        padding="md"
    ),
    html.Div(
        id="main-content",
        children=overview_content,
    ),
    dmc.Affix(
        dmc.ActionIcon(
            DashIconify(icon="mdi:home", width=24),
            id="home_button_IN",
            size="xl",
            radius="md",
            variant="filled",
            color="blue"
        ),
        position={"bottom": 20, "right": 20}
    ),
    dcc.Store(id="active-page", data="overview")
])

lyt = dmc.MantineProvider(
    [
        Header,
    ]
)