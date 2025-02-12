input.onButtonPressed(Button.A, function on_button_pressed_a() {
    xgo.init_xgo_serial(SerialPin.P2, SerialPin.P1)
    xgo.get_version()
    xgo.leg_lift(10)
    basic.showLeds(`
    . . . . .
    . # . # .
    . . # . .
    . . . . .
    . . . . .
    `)
    music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.UntilDone)
    xgo.leg_lift(0)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    xgo.GetPosestate(xgo.pose_enum.pose1)
    basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . # . # .
    . . . . .
    `)
})
