# Алексеева Елена
# documentation https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-rest-api-2-universal-avatar-type-type-owner-entityId-post

import pytest
import requests
from faker import Faker

from test_data.api_variables_data import DO_REGISTER_REST, data_user, ADD_AVATAR

faker = Faker()


@pytest.mark.parametrize("email, name, password", data_user())
def test_send_avatar(email, name, password):
    print(f"Новый пользователь email: {email}, name: {name}, password: {password}")
    doregister = requests.post(url=DO_REGISTER_REST.format(email, name, password))
    print(doregister.text.encode('utf-8-sig'))
    assert doregister.text.encode('utf-8-sig'), f'Refused request. Server answer {doregister}'
    url = ADD_AVATAR.format(email=email)
    payload = {}
    files = [
      ('avatar', open('tests//Python.jpg', 'rb'))
    ]
    headers = {
      'Content-Type': 'multipart/form-data; boundary=--------------------------846395766302543056450567'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text.encode('utf-8-sig'))
