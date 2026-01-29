import random

target = random.randint(1, 10)
while True:
    guess = int(input("Đoán một số từ 1 đến 10: "))
    if guess < target:
        print("Too low")
    elif guess > target:
        print("Too high")
    else:
        print("Correct")
        break