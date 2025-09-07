def on_gesture_tilt_left():
    basic.show_number(input.rotation(Rotation.ROLL))
    basic.pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_six_g():
    music.set_volume(200)
    music.play(music.tone_playable(784, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.ASLEEP)
    basic.clear_screen()
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
    basic.pause(100)
    music.play(music.string_playable("B A G A G F A C5 ", 358),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(5000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    basic.show_number(input.rotation(Rotation.PITCH))
    basic.pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

y = 0
x = 0
radio.set_group(67)

def on_forever():
    global x, y
    x = input.rotation(Rotation.ROLL)
    radio.send_value("rotaton y", y)
    y = input.rotation(Rotation.PITCH)
    radio.send_value("rotaton x ", x)
    serial.write_value("x", x)
    serial.write_value("y", y)
    basic.pause(100)
basic.forever(on_forever)
