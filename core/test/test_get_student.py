import allure
import pytest
from pydantic import ValidationError
from core.models.get_student import StudentsResponse
from core.models.get_student_by_id import StudentByIdResponse
from requests import HTTPError


@allure.feature('Test Get Student')
@allure.story('Test get student with valid data')
def test_get_student_with_valid_data(api_client):
    response = api_client.get_student()

    try:
        StudentsResponse.model_validate(response)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")
    assert response["status"] == 1


@allure.feature('Test Get Student By ID')
@allure.story('Test get student by id create valid data')
def test_get_student_by_id_with_valid_id(api_client, create_student):
    student_id = create_student['student']['id']
    response = api_client.get_student_by_id(student_id)

    try:
        StudentByIdResponse.model_validate(response)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")
    assert response["status"] == 1

    assert create_student['student']['email'] == response['student']['email']
    assert create_student['student']['gender'] == response['student']['gender']
    assert create_student['student']['id'] == response['student']['id']
    assert create_student['student']['name'] == response['student']['name']
    assert create_student['student']['phone_no'] == response['student']['phone_no']
    assert create_student['student']['status'] == response['student']['status']


@allure.feature('Test Get Student By ID')
@allure.story('Test get student by id from student list')
def test_get_student_by_id_with_valid_id_from_student_list(api_client):
    students_list = api_client.get_student()
    student_id = students_list["students"][0]['id']
    response = api_client.get_student_by_id(student_id)

    try:
        StudentByIdResponse.model_validate(response)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")
    assert response["status"] == 1


@allure.feature('Test Get Student By ID')
@allure.story('Test get student by nonexistent id')
def test_get_student_by_nonexistent_id(api_client):
    student_id = 99999999999
    response = api_client.get_student_by_id(student_id)
    assert response["status"] == 0
    assert response["message"] == "Student not found"


@allure.story("Test Get Student By invalid id")
@pytest.mark.parametrize("student_id", ["a", -1])
def test_get_invalid_id(api_client, student_id):
    with pytest.raises(HTTPError) as exc_info:
        api_client.get_student_by_id(student_id)

    response = exc_info.value.response
    assert response.status_code == 404, (
        f"Wait 404 for id={student_id}, response {response.status_code}: {response.text}"
    )

