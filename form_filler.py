import requests
from faker import Faker

faker = Faker()

def generate_credit_card_number():
    iin = '4'  # Visa cards start with a 4
    length = 16  # Standard Visa credit card number length
    number = iin

    while len(number) < (length - 1):
        number += str(faker.random_digit())

    # Luhn algorithm to calculate the check digit
    sum_ = 0
    pos = 0
    reversed_number = number[::-1]

    while pos < length - 1:
        odd = int(reversed_number[pos]) * 2
        if odd > 9:
            odd -= 9
        sum_ += odd

        if pos != length - 2:
            sum_ += int(reversed_number[pos + 1])

        pos += 2

    check_digit = ((sum_ // 10) + 1) * 10 - sum_
    number += str(check_digit % 10)

    return number

# Generate random data
name = faker.name()
credit_card_number = generate_credit_card_number()
expiration_date = faker.credit_card_expire()
cvv = faker.random_int(min=100, max=999)
phone_number = faker.phone_number()

# URL of the PHP page with the HTML form
url = 'https://site-domain.com/step2.php'

# Form data
data = {
    'fullname': name,
    'ccnum': credit_card_number,
    'mm': expiration_date,
    'cvv': cvv,
    'tel': phone_number
}

# Send a POST request to submit the form
response = requests.post(url, data=data)

# Check the response status
if response.status_code == 200:
    print('Form submitted successfully.')
else:
    print('Failed to submit the form.', response.reason)
