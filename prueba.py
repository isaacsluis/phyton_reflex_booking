import reflex as rx 

def estrellas(cantidad):
    for i in range(cantidad):
        print(i)
        d = rx.image(
                src='start.png',
                width="20px",
                height="auto",
            )
    return d


a = estrellas(4)

print(a)