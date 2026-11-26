import time
from focar import move_forward, turn_right, stop, blink_led

LONG_SIDE = 2.0
SHORT_SIDE = 1.2
TURN_TIME = 0.45

def main():
    time.sleep(1)
    sides = [LONG_SIDE, SHORT_SIDE, LONG_SIDE, SHORT_SIDE]

    for duration in sides:
        move_forward(duration)
        stop()
        blink_led(3)
        turn_right(TURN_TIME)
        stop()

if __name__ == "__main__":
    main()