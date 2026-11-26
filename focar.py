from machine import Pin, PWM
from time import sleep

# Motor pins
motor_a_speed = PWM(Pin(28))
motor_a_direction = Pin(27, Pin.OUT)

motor_b_speed = PWM(Pin(26))
motor_b_direction = Pin(22, Pin.OUT)

# Onboard LED (Raspberry Pi Pico W)
led = Pin("LED", Pin.OUT)
# Motor settings
motor_a_speed.freq(1000)
motor_b_speed.freq(1000)

SPEED = 32767


def set_motors(direction_a, direction_b, speed_a=SPEED, speed_b=SPEED):
    motor_a_direction.value(direction_a)
    motor_b_direction.value(direction_b)

    motor_a_speed.duty_u16(speed_a)
    motor_b_speed.duty_u16(speed_b)


def stop(duration=0):
    motor_a_speed.duty_u16(0)
    motor_b_speed.duty_u16(0)
    sleep(duration)


def move_forward(duration=2.0):
    set_motors(1, 1)
    sleep(duration)
    stop()


def move_backward(duration=2.0):
    set_motors(0, 0)
    sleep(duration)
    stop()


def turn_left(duration=0.8):
    set_motors(0, 1)
    sleep(duration)
    stop()


def turn_right(duration=0.8):
    set_motors(1, 0)
    sleep(duration)
    stop()


def led_on():
    led.on()


def led_off():
    led.off()


def flash_led(times=3, interval=0.2):
    for _ in range(times):
        led.on()
        sleep(interval)

        led.off()
        sleep(interval)
        