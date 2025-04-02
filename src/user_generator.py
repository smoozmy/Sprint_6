from faker import Faker

class UserGenerator:

    generator = Faker('ru_RU')

    first_name = generator.first_name()
    last_name = generator.last_name()
    date = generator.date()
    text = generator.text()