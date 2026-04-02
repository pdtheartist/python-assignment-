import requests

def fetch_random_joke():
    """
    Fetches a random Chuck Norris joke from the official API
    and prints only the joke text.
    """
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        # Sending a GET request to the API
        response = requests.get(api_url)

        # Checking if the request was successful
        response.raise_for_status()

        # Parsing the JSON response
        data = response.json()

        # Extracting the joke text from the 'value' field
        joke_text = data.get("value")

        # Displaying only the joke text as per requirements
        print(joke_text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_random_joke()