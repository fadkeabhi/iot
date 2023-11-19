import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set GPIO pins for the ultrasonic sensor
trig_pin = 17  # GPIO17
echo_pin = 18  # GPIO18

# Set up GPIO pins
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

try:
    while True:
        # Trigger the ultrasonic sensor
        GPIO.output(trig_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trig_pin, GPIO.LOW)

        # Measure the time for the echo to return
        while GPIO.input(echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        # Calculate distance using the speed of sound (343 m/s)
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        print(f"Distance: {distance} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting due to keyboard interrupt.")

finally:
    # Clean up GPIO on exit
    GPIO.cleanup()
