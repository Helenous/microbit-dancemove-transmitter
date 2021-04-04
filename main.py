def on_forever():
    if images.icon_image(IconNames.HEART) == images.arrow_image(ArrowNames.WEST):
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.FORWARD,
            81)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
            kitronik_motor_driver.MotorDirection.FORWARD,
            100)
        basic.pause(500)
basic.forever(on_forever)

