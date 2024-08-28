import reflex as rx

def header() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.avatar(name="Alberto Dasi", size="xl"),
        rx.text("Alberto Dasi"),
        rx.text("""Hola, soy desarrollador de software desde 2019.
                Actualmente formo parte del equipo de soporte para el Instituto Valenciano de Estadistica""")
    )