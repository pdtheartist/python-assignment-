from flask import Flask, jsonify

app = Flask(__name__)


def is_prime(n):
    """Function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    # Determine if the number is prime
    result = is_prime(number)

    # Create the response dictionary as required
    response = {
        "Number": number,
        "isPrime": result
    }

    # Return the response in JSON format
    return jsonify(response)


if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True, port=5000)