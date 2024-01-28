import reflex as rx 

# Lorem para que se creen texto atutomaticos
from lorem_text import lorem

# componentes propios
from ejerciciosCSS.components.articulo import articulo


def body() -> rx.Component:
    return rx.box(
        articulo('casa.png','Casas rurales',lorem.paragraph(),'#FDFCB7','#B79B34'),
        articulo('camping.png','Camping',lorem.paragraph(),'#D3FFAC','#79A24A'),
        articulo('hotel.png','Hotel',lorem.paragraph(),'#B8E3FF','#0C356F'),
    )