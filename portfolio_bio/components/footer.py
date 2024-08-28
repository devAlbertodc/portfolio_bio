import reflex as rx

def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.text("2019-2024 - Alberto Dasi - Construyendo software con ?? desde Valencia para el mundo")
    )