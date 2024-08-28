import reflex as rx
from portfolio_bio.components.navbar import navbar
from portfolio_bio.components.footer import footer
from portfolio_bio.views.header.header import header
from portfolio_bio.views.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.chakra.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )

app = rx.App()
app.add_page(index)