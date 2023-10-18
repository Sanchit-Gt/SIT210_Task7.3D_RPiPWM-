# Importing necessary modules
from gpiozero import DistanceSensor, PWMOutputDevice
from time import sleep

# Defining GPIO pins
trigPin = 17  # Pin that sends out signals for distance measurement
echoPin = 27  # Pin that receives signals for distance measurement
buzzerPin = 22  # Pin that controls the buzzer

# Setting up the distance sensor with defined pins and a maximum detection range of 1.0 meter
ultraSonicSensor = DistanceSensor(trigger=trigPin, echo=echoPin, max_distance=1.0)

# Initializing the buzzer for making sounds
buzzer = PWMOutputDevice(buzzerPin)

try:
    while True:
        sleep(0.5)

        # Measuring the distance to an object in centimeters
        distanceInCM = ultraSonicSensor.distance * 100
        print("Distance (CM): %.2f" % distanceInCM)

        # Adjusting the buzzer sound based on the measured distance
        # When the object is far (100cm or more), the buzzer is silent.
        # As the object gets closer, the buzzer makes more noise.
        buzz = 1.0 - (distanceInCM / 100)
        print("Buzz: %.2f" % buzz)

        # Controlling the buzzer sound intensity
        buzzer.value = buzz

except KeyboardInterrupt:
    print("Program Ended")