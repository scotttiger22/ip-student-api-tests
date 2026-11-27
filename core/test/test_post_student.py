import allure
import pytest
from pydantic import ValidationError
from core.models.post_student import StudentCreatedResponse


@allure.feature('Test Post Student')
@allure.story('Test post student with valid random data')
def test_post_student_with_valid_data(api_client, generate_random_student_data):
    response = api_client.post_student(student_data=generate_random_student_data)

    try:
        StudentCreatedResponse.model_validate(response)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")
    assert response["message"] == "Student created successfully"
    assert response["status"] == 1
    assert response["student"]["email"] == generate_random_student_data["email"]
    assert response["student"]["gender"] == generate_random_student_data["gender"]
    assert response["student"]["name"] == generate_random_student_data["name"]
    assert response["student"]["phone_no"] == generate_random_student_data["phone_no"]
    assert response["student"]["status"] == generate_random_student_data["status"]


@allure.feature('Test Post Student')
@allure.story('Test post student without parameter email')
def test_post_student_without_parameter_email(api_client):
    data = {
        "gender": "male",
        "name": "Ivan Ivanov",
        "phone_no": "+79990001122",
        "status": 1
    }
    response = api_client.post_student(student_data=data)
    assert response['message'] == "Wrong JSON, student not created"
    assert response['status'] == 0


@allure.story('Test Post Student with invalid field gender and status')
@pytest.mark.parametrize(
    "field,value,message",
    [
        ("gender", "other", "Wrong gender, student not created"),
        ("status", 5, "Wrong status, student not created"),
    ],
)
def test_post_student_invalid_field_gender_and_status(api_client, generate_random_student_data, field, value, message):
    payload = dict(generate_random_student_data)
    payload[field] = value
    response = api_client.post_student(student_data=payload)
    assert response['message'] == message
    assert response['status'] == 0


@allure.story('Test Post Student with invalid field')
@pytest.mark.parametrize(
    "field,value",
    [
        ("email", 123),
        ("name", 123),
        ("phone_no", "aaaa")
    ],
)
def test_post_student_invalid_field(api_client, generate_random_student_data, field, value):
    payload = dict(generate_random_student_data)
    payload[field] = value

    response = api_client.post_student(payload)
    assert response['status'] == 0, f'if status = 1 bag {field} = {value}'

