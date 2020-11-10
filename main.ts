input.onButtonPressed(Button.A, function () {
    sendData = !(sendData)
})
let previousMillis = 0
let currentMillis = 0
let accel = ""
let sendData = false
radio.setGroup(1)
let duration = 1000
sendData = false
basic.forever(function () {
    while (sendData) {
        accel = "" + input.acceleration(Dimension.X) + "," + input.acceleration(Dimension.Y) + "," + input.acceleration(Dimension.Z)
        radio.sendString(accel)
        currentMillis = control.millis()
        led.plotBrightness(0, 0, 255)
        if (currentMillis - previousMillis >= duration) {
            led.plotBrightness(0, 0, 0)
            previousMillis = currentMillis
        }
        basic.pause(100)
    }
    led.plotBrightness(0, 0, 0)
})
