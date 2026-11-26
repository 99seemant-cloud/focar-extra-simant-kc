import time
from focar import move_forward, turn_right, stop

LONG_SIDE = 2.0
SHORT_SIDE = 1.2
TURN_TIME = 0.45

def main():
    time.sleep(1)
    sides = [LONG_SIDE, SHORT_SIDE, LONG_SIDE, SHORT_SIDE]

    for duration in sides:
        move_forward(duration)
        stop()
        turn_right(TURN_TIME)
        stop()

if __name__ == "__main__":
    main()