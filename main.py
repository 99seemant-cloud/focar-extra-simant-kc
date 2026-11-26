from time import sleep
import focar

# Rectangle dimensions (movement time in seconds)
LONG_SIDE = 2.0
SHORT_SIDE = 1.2

# Turning time (calibrate for your FoCar)
TURN_TIME = 0.8

# Wait before starting
sleep(5)

# Start rectangular route
for side in range(4):

    print("Moving along side", side + 1)

    # Alternate long and short sides
    if side % 2 == 0:
        focar.move_forward(LONG_SIDE)
    else:
        focar.move_forward(SHORT_SIDE)

    # Stop at the corner
    focar.stop()

    print("Reached corner", side + 1)

    # Flash LED three times
    focar.flash_led(3, 0.5)

    # Turn 90 degrees left
    focar.turn_left(TURN_TIME)

# Final stop
focar.stop()

focar.led_off()

print("Rectangular route completed!")
print("FoCar has returned to its starting position.")