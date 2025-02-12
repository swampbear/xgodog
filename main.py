def on_button_pressed_a():
    basic.show_icon(IconNames.ASLEEP)
    xgo.execution_action(xgo.action_enum.SQUAT)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
music.play(music.string_playable("C D E F G A B C5 ", 350),
    music.PlaybackMode.UNTIL_DONE)