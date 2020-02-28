# Алексеева Елена
# documentation https://testbase.atlassian.net/wiki/spaces/USERS/pages/994345363/AddAvatar
import os

import pytest
import requests
from faker import Faker

from test_data.api_variables_data import DO_REGISTER_REST, data_user, ADD_AVATAR

faker = Faker()


# @pytest.mark.parametrize("email, name, password", data_user())
@pytest.mark.parametrize("email, name, password", [("qq2@gmail.com", "Jill", "fsyise")])
@pytest.mark.parametrize("file", [(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Python.jpg'))])
def test_send_avatar(email, name, password, file):
    # print(f"Новый пользователь email: {email}, name: {name}, password: {password}")
    # doregister = requests.post(url=DO_REGISTER_REST.format(email, name, password))
    # print(doregister.text.encode('utf8').decode("utf8"))
    # assert doregister.text.encode('utf8'), f'Refused request. Server answer {doregister}'
    url = ADD_AVATAR.format(email)
    payload = {}
    files = [
      ('avatar', open(file, 'rb'))
    ]
    headers = {'Content-Type': 'multipart/form-data',
               'Cookie': 'PHPSESSID=fd7650477ff609ce4e238e764adcb2da'}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    assert response.json()["status"] == 'ok', f'Error message: {response.text.encode("utf8").decode("utf8")}'
