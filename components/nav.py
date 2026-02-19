import dash_mantine_components as dmc

Nav = dmc.Stack(
    [
        dmc.NavLink(label="Title", id="nav-overview"),
        dmc.NavLink(label="Executive summary", id="nav-intro"),
        dmc.NavLink(label="Data slice", id="nav-slice"),
        dmc.NavLink(label="Test 1: Significance test", id="nav-t"),
        dmc.NavLink(label="Test 2: Confidence interval", id="nav-ci"),
        dmc.NavLink(label="Test 3: Sign test", id="nav-sign"),
        dmc.NavLink(label="Test 4: Permutation test", id="nav-permutation"),
        dmc.NavLink(label="Recommendaion and next steps", id="nav-rec"),
    ]
)
