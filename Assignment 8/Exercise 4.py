import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            change_of_speed = random.randint(-10, 15)
            car.accelerate(change_of_speed)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'Car':<10} {'Speed':<10} {'Distance':<10}")
        for car in self.car_list:
            print(f"{car.registration_number:<10} {car.current_speed:<10} {car.distance_traveled:<10}")

    def race_finished(self):
        for car in self.car_list:
            if car.distance_traveled >= self.kilometers:
                return True
        return False


# Main program
cars = []
for i in range(1, 11):
    car = Car(f"ABC-{i}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\nStatus after {hours} hours:")
        race.print_status()

print("\nFinal status:")
race.print_status()


