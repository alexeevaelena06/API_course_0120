# Алексеева Елена
# documentation https://testbase.atlassian.net/wiki/spaces/USERS/pages/592674928/doRegister
# pytest.dependency  https://pytest-dependency.readthedocs.io/en/latest/usage.html
# header's documentation - https://developer.mozilla.org/
# https://httpstatuses.com/


import pytest
import requests
from faker import Faker
from zeep import client, Client, Settings

from api.client import BugRedClient
from test_data.api_variables_data import DO_REGISTER_REST, DO_REGISTER_SOAP, WSDL, data_user

faker = Faker()

"""DoRegister"""

# REST


@pytest.mark.parametrize("email, name, password", data_user())
@pytest.mark.dependency(name='1')
def test_doregister_rest(email, name, password):
    print(f"Новый пользователь email: {email}, name: {name}, password: {password}")
    doregister = requests.post(url=DO_REGISTER_REST.format(email, name, password))
    print(doregister.text.encode('utf8'))
    assert doregister.text.encode('utf8'), f'Refused request. Server answer {doregister}'
    client = BugRedClient("http://users.bugred.ru")
    client.authorize(email, password)



@pytest.mark.parametrize("email, name, password", data_user())
def test_doregister_rest_2(client, email, name, password):
    print(f"Новый пользователь email: {email}, name: {name}, password: {password}")
    data = {
        "email": email,
        "name": name,
        "password": password
    }
    res = client.vr(client.do_register(data), [200, 201])
    created = res.json()
    print(created)
    client = BugRedClient("http://users.bugred.ru")
    client.authorize(email, password)


# SOAP

@pytest.mark.parametrize("email, name, password", data_user())
@pytest.mark.dependency(name='3', depends=['1'])
def test_doregister_soap(email, name, password):
    print(f"Новый пользователь email: {email}, name: {name}, password: {password}")
    url = DO_REGISTER_SOAP
    headers = {'content-type': 'text/xml'}
    body = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wrap="http://foo.bar/wrappersoapserver">
                   <soapenv:Header/>
                   <soapenv:Body>
                      <wrap:doRegister>
                         <email>{email}</email>
                         <name>{name}</name>
                         <password>{password}</password>
                      </wrap:doRegister>
                   </soapenv:Body>
                </soapenv:Envelope>"""
    response = requests.post(url, data=body, headers=headers)
    print(response.content)
    assert response.text.encode('utf8'), f'Refused request. Server answer {response}'
    client = BugRedClient("http://users.bugred.ru")
    client.authorize(email, password)


@pytest.mark.parametrize("email, name, password", data_user())
def test_doregister_soap_2(email, name, password):
    print(f"Новый пользователь email: {email}, name: {name}, password: {password}")
    settings = Settings(strict=False, xml_huge_tree=True)
    client = Client(WSDL, settings=settings)
    new_user = client.service.doRegister(email=email, name=name, password=password)
    assert new_user, 'Новый пользователь не создан'
    client = BugRedClient("http://users.bugred.ru")
    client.authorize(email, password)


"""WSDL"""


def test_bind():
    client_obj = client.Client(WSDL)
    service = client_obj.bind()
    assert service


def test_operation_proxy_doc():
    client_obj = client.Client(WSDL)
    assert (client_obj.service["doRegister"].__doc__
            == 'doRegister(email: xsd:string, name: xsd:string, password: xsd:string) -> UserReturn: ns0:UserReturn')


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
