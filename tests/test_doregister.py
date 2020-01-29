# Алексеева Елена
# documentation https://testbase.atlassian.net/wiki/spaces/USERS/pages/592674928/doRegister
# pytest.dependency  https://pytest-dependency.readthedocs.io/en/latest/usage.html

import pytest
import requests
from zeep import client
from faker import Faker
from test_data.api_variables_data import *

faker = Faker()


"""DoRegister"""

# REST


@pytest.mark.dependency()
def test_doregister_rest():
    new_name = f"{faker.first_name()}"
    new_email = f"{new_name}@mail.ru"
    print(new_email)
    doregister = requests.post(url=DO_REGISTER_REST.format(new_email, new_name, "test"))
    print(doregister.text.encode('utf8'))
    assert doregister.text.encode('utf8'), f'Refused request. Server answer {doregister}'


def test_doregister_rest_2(client):
    new_name = f"{faker.first_name()}"
    new_email = f"{new_name}@mail.ru"
    print(new_email)

    data = {
        "email": new_email,
        "name": new_name,
        "password": "1"
    }
    res = client.vr(client.do_register(data), [200, 201])
    created = res.json()
    print(created)


# SOAP


@pytest.mark.dependency(depends=["test_doregister_rest"])
def test_doregister_soap():
    url = DO_REGISTER_SOAP
    headers = {'content-type': 'text/xml'}
    new_name = f"{faker.first_name()}"
    new_email = f"{new_name}@mail.ru"
    body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wrap="http://foo.bar/wrappersoapserver">
                   <soapenv:Header/>
                   <soapenv:Body>
                      <wrap:doRegister>
                         <email>{new_email}</email>
                         <name>{new_name}</name>
                         <password>test</password>
                      </wrap:doRegister>
                   </soapenv:Body>
                </soapenv:Envelope>"""
    print(new_email)
    response = requests.post(url, data=body, headers=headers)
    print(response.content)
    assert response.text.encode('utf8'), f'Refused request. Server answer {response}'


"""WSDL"""


def test_bind():
    client_obj = client.Client(WSDL)
    service = client_obj.bind()
    assert service


def test_operation_proxy_doc():
    client_obj = client.Client(WSDL)
    assert (
        client_obj.service["doRegister"].__doc__
        == 'doRegister(email: xsd:string, name: xsd:string, password: xsd:string) -> UserReturn: ns0:UserReturn'
    )


def test_client_no_wsdl():
    with pytest.raises(ValueError):
        client.Client(None)


def test_client_cache_service():
    client_obj = client.Client(WSDL)
    assert client_obj.service["doRegister"], f"service {client_obj.service['doRegister']} not found"
    assert client_obj.service["getUser"], f"service {client_obj.service['getUser']} not found"
    assert client_obj.service["getUserFull"], f"service {client_obj.service['getUserFull']} not found"
    assert client_obj.service["getCompany"], f"service {client_obj.service['getCompany']} not found"
    assert client_obj.service["UpdateUserOneField"], f"service {client_obj.service['UpdateUserOneField']} not found"
