# Алексеева Елена
import random
import string
from faker import Faker

faker = Faker()

WSDL = 'http://users.bugred.ru/tasks/soap/WrapperSoapServer.php?wsdl'
DO_REGISTER_REST = 'http://users.bugred.ru/tasks/rest/doregister?email={}&name={}&password={}'
DO_REGISTER_SOAP = 'http://users.bugred.ru/tasks/soap/WrapperSoapServer.php'
REST_POST = 'http://users.bugred.ru/tasks/rest/list'
DO_LOGIN = 'http://users.bugred.ru/tasks/rest/dologin?email={}&password={}'
CURL = 'curl -X POST --header "Content-Type: application/json" "http://users.bugred.ru/tasks/rest/doregister?email=first_mail_1@mail.ru&name=five&password=test"'
CURL_2 = 'curl -i -X POST -H "Content-Type: application/json" -d "{\"email\": \"mailchik@gmail.com\", \"name\": \"Marmelad\", \"password\": \"1\"}" http://users.bugred.ru/tasks/rest/doregister'
CURL_3 = 'curl -d "{\"email\": \"mailchik1@gmail.com\", \"name\": \"Marmelad1\", \"password\": \"1\"}" http://users.bugred.ru/tasks/rest/doregister'
GET_ISSUE_LINK = 'https://testbase.atlassian.net/rest/api/2/issueLink/{}'
CREATE_ISSUE_LINK = 'https://testbase.atlassian.net/rest/api/2/issueLink'
ADD_AVATAR = 'http://users.bugred.ru/tasks/rest/addavatar/?email={}'

"""DoRegister"""


def data_user():
    """Формирование нового сета данных для пользователя"""
    new_name = f"{faker.first_name()}"
    new_email = f"{new_name}@" + random.choice(['gmail.com', 'mail.ru', 'yandex.ru', 'yahoo.com', 'rambler.ru'])
    password = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    test_data = [(new_email, new_name, password)]
    return test_data
