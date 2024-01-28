import reflex as rx 

from lorem_text import lorem

def opinion(logo,numero_estrellas)-> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=logo,
                width="60px",
                height="auto",
            ),
            estrellas(numero_estrellas),
        ),
        rx.text(
            lorem.paragraph(),
            color = '#A3A3A3'
        ),
        padding_top = '20px',
    )

def estrellas(cantidad):
    for i in range(cantidad):
        return rx.image(
                src='start.png',
                width="20px",
                height="auto",
            )
        
     


