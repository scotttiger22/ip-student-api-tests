from core.client.api_client import APIClient
import pytest
from faker import Faker



@pytest.fixture()
def api_client():
    client = APIClient()
    return client


@pytest.fixture()
def generate_random_student_data():
    faker = Faker("ru_RU")
    email = faker.email()
    gender = faker.random_element(elements=("male", "female"))
    name = faker.name()
    phone_no = f"+7{faker.numerify(text='##########')}"
    status = faker.boolean()

    data = {
        "email": email,
        "gender": gender,
        "name": name,
        "phone_no": phone_no,
        "status": status
    }

    return data


@pytest.fixture()
def create_student(api_client, generate_random_student_data):
    response = api_client.post_student(generate_random_student_data)
    assert response.get("status") == 1, f"Создание не удалось: {response}"
    return response

