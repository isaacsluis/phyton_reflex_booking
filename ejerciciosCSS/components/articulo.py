import reflex as rx 

from lorem_text import lorem

def articulo(logo,titulo,parrafo,color_fondo,color_borde) -> rx.Component:
    return rx.box(
                rx.image(
                    src=logo,
                    width="50px",
                    height="auto",
                    #border_radius="15px 50px",
                    #border="5px solid #555",
                    #box_shadow="lg",
                ),
                rx.text(
                    titulo,
                    text_align = 'left',
                    font_size = '2em',
                    font_weight = 'bold',
                    text_transform = 'uppercase',
                    width = '100%',
                ),
                rx.text(
                    parrafo,
                    #lorem.paragraph(),
                    font_size = '1em',
                    width = '100%',
            ),
        width = '100%',
        border_style = 'solid',
        border_width = '5px',
        margin_top = '50px',
        padding_top = '40px',
        padding_left = '20px',
        padding_bottom = '40px',
        border_radius = '50px 0px',
        bg = color_fondo,
        border_color = color_borde,
    )


