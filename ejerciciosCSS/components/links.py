import reflex as rx

def links() -> rx.Component:
    return rx.box(
            rx.breadcrumb(
                rx.breadcrumb_item(
                    rx.breadcrumb_link("Inicio", href="#")
                ),
                rx.breadcrumb_item(
                    rx.breadcrumb_link("Casas Rurales", href="#")
                ),
                rx.breadcrumb_item(
                    rx.breadcrumb_link("Camping", href="#")
                ),
                rx.breadcrumb_item(
                    rx.breadcrumb_link("Hoteles", href="#")
                ),
                rx.breadcrumb_item(
                    rx.breadcrumb_link("Opiniones!!", href="#")
                ),
            ),
            separator="||",
            color="white",
            bg = '#73A345',
            padding_left = '10px',
        
    )