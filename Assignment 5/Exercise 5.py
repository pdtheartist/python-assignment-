import random


def approximate_pi(n):
    """
    Approximate the value of Pi using the Monte Carlo method.
    """
    inside_circle = 0

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            inside_circle += 1

    return 4 * inside_circle / n


def main():
    while True:
        try:
            n = int(input("Enter the number of random points: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    pi_value = approximate_pi(n)
    print("Approximated value of Pi:", pi_value)


if __name__ == "__main__":
    main()