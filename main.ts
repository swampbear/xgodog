input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
    xgo.execution_action(xgo.action_enum.Squat)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Angry)
    xgo.execution_action(xgo.action_enum.Go_prone)
})
basic.showIcon(IconNames.Asleep)
xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
music.play(music.stringPlayable("C D E F G A B C5 ", 350), music.PlaybackMode.UntilDone)
