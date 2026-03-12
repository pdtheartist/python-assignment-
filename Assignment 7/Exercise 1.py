class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Maximum speed:", car.maximum_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)