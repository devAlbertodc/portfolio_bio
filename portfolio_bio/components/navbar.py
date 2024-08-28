import reflex as rx

def navbar() -> rx.Component:
    return rx.chakra.hstack(
        rx.text(
            "alberto",
            height="40px",
        ),
        position="sticky",
        bg="yellow",
        padding_x="16px",
        padding_y="8px",
        z_index="999",
    )
