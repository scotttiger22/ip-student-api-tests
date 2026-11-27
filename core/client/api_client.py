import requests
import allure
import logging

logger = logging.getLogger("rv.tests")


class APIClient:
    def __init__(self):
        self.base_url = "http://194.87.126.16/student"
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def log(self, step, message):
        logger.info(message)
        allure.attach(message, step, allure.attachment_type.TEXT)

    def get_student(self):
        with allure.step('Get Student'):
            url = self.base_url
            self.log("GET /student", f"get{url}")
            response = self.session.get(url)
            self.log("GET /student", f"response {response.status_code}\nbody: {response.text}")
            response.raise_for_status()
        with allure.step('Checking status code'):
            assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
        return response.json()

    def post_student(self, student_data):
        with allure.step('Creating Student'):
            url = self.base_url
            self.log("POST /student", f"post {url}\nbody: {student_data}")
            response = self.session.post(url, json=student_data)
            self.log("POST /student", f"response {response.status_code}\nbody: {response.text}")
            response.raise_for_status()
        with allure.step('Checking status code'):
            assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
        return response.json()

    def delete_student(self, student_id):
        with allure.step('Get Student by id'):
            url = f'{self.base_url}/{student_id}'
            self.log("DELETE /student/{id}", f"delete {url}")
            response = self.session.delete(url)
            self.log("DELETE /student/{id}", f"response {response.status_code}\nbody: {response.text}")
            response.raise_for_status()
        with allure.step('Checking status code'):
            assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
        return response.json()

    def get_student_by_id(self, student_id):
        with allure.step('Get Student by id'):
            url = f'{self.base_url}/{student_id}'
            self.log("GET /student/{id}", f"get {url}")
            response = self.session.get(url)
            self.log("GET /student/{id}", f"response {response.status_code}\nbody: {response.text}")
            response.raise_for_status()
        with allure.step('Checking status code'):
            assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
        return response.json()

    def put_student(self, student_id, student_data):
        with allure.step('Creating Student'):
            url = f'{self.base_url}/{student_id}'
            self.log("PUT /student/{id}", f"put {url}\nbody: {student_data}")
            response = self.session.put(url, json=student_data)
            self.log("PUT /student/{id}", f"response {response.status_code}\nbody: {response.text}")
            response.raise_for_status()
        with allure.step('Checking status code'):
            assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
        return response.json()

