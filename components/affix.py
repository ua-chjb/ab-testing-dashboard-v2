import dash_mantine_components as dmc
from dash_iconify import DashIconify

logout = dmc.Affix(
    dmc.ActionIcon(
        DashIconify(icon="mdi:logout", width=20),
        id="logout_button_IN",
        size="lg",
        radius="md",
        variant="filled",
        color="blue",
    ),
    position={"top": 52, "right": 52},
)
