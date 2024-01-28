import reflex as rx
from  ejerciciosCSS.views.navbar import navbar

import ejerciciosCSS.styles.styles as styles

from ejerciciosCSS.components.opinion import opinion
from ejerciciosCSS.views.body import body
from ejerciciosCSS.views.opiniones import opiniones

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.center(
        rx.box(
            navbar(),
            body(),
            opiniones(),   
            width = '80%', 
        ),
    )


# Create app instance and add index page.
app = rx.App(
    stylesheets=styles.STYLESHEETS
)
app.add_page(index)
