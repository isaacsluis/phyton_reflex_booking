import reflex as rx
from ejerciciosCSS.components.heading import heading
from ejerciciosCSS.components.links import links

def navbar() -> rx.Component:
    return rx.box(
        heading(),
        links(),
        rx.image(
            src="fondo_cabecera.png", 
            width="100%", 
            height="auto"
        ),

    )