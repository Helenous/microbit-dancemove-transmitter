def on_button_pressed_a():
    global sendData
    sendData = not (sendData)
input.on_button_pressed(Button.A, on_button_pressed_a)

previousMillis = 0
currentMillis = 0
sendData = False
radio.set_group(1)
strVar = "Hello World!"
duration = 1000
sendData = False

def on_forever():
    global currentMillis, previousMillis
    while sendData:
        radio.send_string(strVar)
        currentMillis = control.millis()
        led.plot_brightness(0, 0, 255)
        if currentMillis - previousMillis >= duration:
            led.plot_brightness(0, 0, 0)
            previousMillis = currentMillis
        basic.pause(100)
    led.plot_brightness(0, 0, 0)
basic.forever(on_forever)
