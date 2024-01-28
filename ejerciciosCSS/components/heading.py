import reflex as rx


def heading() -> rx.Component:
    return rx.center(
            rx.hstack(
                rx.image(
                    src="logo.png", 
                    width="50px", 
                    height="auto"
                    ),
                rx.text(
                    'ViajesOne.com'
                ),
            ),
        background_color = '#B5FD6C',
        color = 'white',
    )

    