import reflex as rx
from portfolio_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.chakra.vstack(
        link_button("A","http://google.es"),
        link_button("B","b"),
        link_button("C","c"),
        link_button("D","d"),
    )