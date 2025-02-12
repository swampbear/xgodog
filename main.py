def on_button_pressed_a():
    xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
    xgo.get_version()
    xgo.leg_lift(10)
    basic.show_leds("""
    . . . . .
    . # . # .
    . . # . .
    . . . . .
    . . . . .
    """)
    music.play(music.string_playable("- - - - - - - - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    xgo.leg_lift(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    xgo.get_posestate(xgo.pose_enum.POSE1)
    
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . # . # .
    . . . . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)
