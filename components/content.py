from dash import html
import dash_mantine_components as dmc

from pages.ci import ci
from pages.overview import progress
from pages.intro import intro
from pages.perm import perm
from pages.rec import rec
from pages.sign import sign
from pages.slice import slice
from pages.z import z

overview_content = progress
intro_content = intro
slice_content = slice
t_content = z
ci_content = ci
sign_content = sign
permutation_content = perm
rec_content = rec


content_map = {
    "nav-overview": overview_content,
    "nav-intro": intro_content,
    "nav-slice": slice_content,
    "nav-t": t_content,
    "nav-ci": ci_content,
    "nav-sign": sign_content,
    "nav-permutation": permutation_content,
    "nav-rec": rec_content,
}

headers_map = {
    "nav-overview": dmc.Title("Title", order=2, c="#228be6"),
    "nav-intro": dmc.Title("Executive summary", order=2, c="#228be6"),
    "nav-slice": dmc.Title("Data slice", order=2, c="#228be6"),
    "nav-t": dmc.Title("Test 1: Two-proportions z-test", order=2, c="#228be6"),
    "nav-ci": dmc.Title("Test 2: Confidence interval", order=2, c="#228be6"),
    "nav-sign": dmc.Title("Test 3: Sign test", order=2, c="#228be6"),
    "nav-permutation": dmc.Title("Test 4: Permutation test", order=2, c="#228be6"),
    "nav-rec": dmc.Title("Recommendation and next steps", order=2, c="#228be6"),
}
