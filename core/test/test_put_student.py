import allure
import pytest
from pydantic import ValidationError
from core.models.put_student import StudentUpdatedResponse


@allure.feature('Test Put Student')
@allure.story('Test put student valid data')
def test_put_student(api_client):
    students = api_client.get_student()
    student_id = students['students'][0]['id']
    data = {
        "email": "ivanov@mail.ru",
        "gender": "male",
        "name": "Ivan Ivanov",
        "status": 1
    }
    response = api_client.put_student(student_id, data)

    try:
        StudentUpdatedResponse.model_validate(response)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")

    assert response["message"] == "Student updated successfully"
    assert response["status"] == 1
    assert response["student"]["email"] == data["email"]
    assert response["student"]["gender"] == data["gender"]
    assert response["student"]["name"] == data["name"]
    assert response["student"]["status"] == data["status"]


@allure.feature('Test Put Student')
@allure.story('Test put student without parameter email')
def test_put_student_with_valid_data(api_client):
    students_list = api_client.get_student()
    student_id = students_list["students"][0]['id']

    data = {
        "gender": "male",
        "name": "Ivan Petrov",
        "status": 1
    }

    response = api_client.put_student(student_id=student_id, student_data=data)

    assert response["message"] == "Wrong JSON, student not updated"
    assert response["status"] == 0

