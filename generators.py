from faker import Faker

faker = Faker()


def generate_random_credentials():
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=10)
    return name, email, password