import toga

def button_handler(widget):
    print("hello")

def build(app):
    box = toga.Box()

    button = toga.Button("Hello world", on_press=button_handler)
    button.style.margin = (20,50,50,50)
    """
    What is done here is say that the button will have a margin of 50 pixels on all sides. If we wanted to 
    define a margin of 20 pixels on top of the button, we could have defined margin_top = 20, or we could have 
    specified the margin = (20, 50, 50, 50).
    """
    button.style.flex = 1
    """
    The flex attribute specifies how a widget is sized with respect to other widgets along its direction. 
    The default direction is row (horizontal) and since the button is the only widget here, it will take up the whole width. 
    Check out style docs for more information on how to use the flex attribute.
    """
    box.add(button)

    return box

def main():
    return toga.App("First App", "org.beeware.toga.examples.tutorial", startup=build)

if __name__ == "__main__":
    main().main_loop()