import random


class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars = []

for i in range(10):
    max_speed = random.randint(150, 200)
    car = Car("ABC-" + str(i+1), max_speed)
    cars.append(car)

race_finished = False

while not race_finished:

    for car in cars:

        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True

print("Race results:")

for car in cars:
    print(car.registration_number,
          car.maximum_speed,
          car.current_speed,
          car.travelled_distance)