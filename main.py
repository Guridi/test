def on_forever():
    basic.show_string("Hola")
    basic.show_leds("""
        . # . # .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
    """)
    basic.show_leds("""
        . # # # .
                . # . # .
                . # . # .
                . # . # .
                . # # # .
    """)
    basic.show_leds("""
        . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
    """)
    basic.show_leds("""
        . # # # .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
    """)
    basic.show_leds("""
        . # . # .
                . # . # .
                # . . . #
                # # . # #
                . # # # .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
basic.forever(on_forever)
