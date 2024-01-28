import reflex as rx 

from lorem_text import lorem

from ejerciciosCSS.components.opinion import opinion

def opiniones()-> rx.Component:
    return rx.box(
        rx.text(
                'OPINIONES DE CLIENTES',
                color = '#A3A3A3'
            ),
        opinion('hombre.png',5),
        opinion('mujer.png',3),
        width = '100%',
        border_style = 'solid',
        border_width = '10px',
        border_left = 'none',
        border_right = ' none',
        margin_top = '50px',
        padding_top = '40px',
        padding_left = '20px',
        padding_bottom = '40px',
        bg = '#CCCCCC',
        border_top_color = '#555555',
        border_bottom_color = '#555555',
        border_left_color = 'none',
    )



