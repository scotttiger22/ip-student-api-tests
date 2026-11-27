import allure
import pytest
from requests import HTTPError


@allure.feature('Test Delete Student')
@allure.story('Test delete student with valid id')
def test_delete_student_with_valid_id(api_client, create_student):
    student_id = create_student['student']['id']
    get_student_by_id = api_client.get_student_by_id(student_id)
    assert get_student_by_id['student']['id'] == student_id
    response = api_client.delete_student(student_id)
    assert response['message'] == 'Student deleted successfully'
    assert response['status'] == 1


@allure.feature('Test Delete Student')
@allure.story('Test delete student by nonexistent id')
def test_delete_student_by_nonexistent_id(api_client):
    student_id = 99999999999
    response_get = api_client.get_student_by_id(student_id)
    assert response_get["status"] == 0
    assert response_get["message"] == "Student not found"
    response_delete = api_client.delete_student(student_id)
    assert response_delete['status'] == 0, f'if status = 1 bag for {student_id}'


@allure.story('Test Delete Student By invalid id')
@pytest.mark.parametrize("student_id", ["a", -1])
def test_get_not_invalid_id(api_client, student_id):
    with pytest.raises(HTTPError) as exc_info:
        api_client.get_student_by_id(student_id)

    response = exc_info.value.response
    assert response.status_code == 404, (
        f"Ожидали 404 для id={student_id}, получили {response.status_code}: {response.text}"
    )

