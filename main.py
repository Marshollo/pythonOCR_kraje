import requests
import pytesseract
from PIL import Image


def load_image(photo):
    image = Image.open(photo)
    text = pytesseract.image_to_string(image)
    print(text)
    text_stripped = text.strip()
    return text_stripped


# connecting with restapi
def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        country_data = response.json()[0]
        return country_data
    else:
        return None


# displaying the data from api
def display_country_info(country_data):
    if country_data:
        print("Country information:")
        print(f"Name: {country_data['name']['common']}")
        print(f"Capital: {country_data['capital'][0]}")
        print(f"Currency: {', '.join(country_data['currencies'].keys())}")
        print(f"Population: {country_data['population']}")
        print(f"Region: {country_data['subregion']}")
    else:
        print("Couldn't find any country information.")


def main():
    country_name = load_image("Italy.png")
    country_data = get_country_info(country_name)
    display_country_info(country_data)


if __name__ == "__main__":
    main()
