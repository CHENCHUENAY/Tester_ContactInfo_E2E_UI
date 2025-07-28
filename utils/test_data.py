import random

class PositiveData:
        firstName = "Chenchu"
        lastName = "Enay"
        birthdate = "1997-04-19"
        email = "chenchuTest@fake.com"
        gen_phone = str(random.randint(9000000000, 9999999999))  # Generate a random phone number
        street1 = "Abu Dhabi"
        street2 = "United Arab Emirates"
        city = "Abu Dhabi"
        stateProvince = "Abu Dhabi"
        postalCode = "00000"
        country = "United Arab Emirates"


class NegativeData:
    invalid_email = "chenchutestfake.com"
    invalid_phone = "99999"
    invalid_postal = "00"

class LoginData:
    login_email = "test2.enay1@fake.com",
    login_password = "myNewPassword"

