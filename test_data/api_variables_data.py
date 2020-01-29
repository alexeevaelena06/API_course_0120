WSDL = 'http://users.bugred.ru/tasks/soap/WrapperSoapServer.php?wsdl'
DO_REGISTER_REST = 'http://users.bugred.ru/tasks/rest/doregister?email={}&name={}&password={}'
DO_REGISTER_SOAP = 'http://users.bugred.ru/tasks/soap/WrapperSoapServer.php'
REST_POST = 'http://users.bugred.ru/tasks/rest/list'
DO_LOGIN = 'http://users.bugred.ru/tasks/rest/dologin?email={}&password={}'
CURL = 'curl -X POST --header "Content-Type: application/json" "http://users.bugred.ru/tasks/rest/doregister?email=first_mail_1@mail.ru&name=five&password=test"'
CURL_2 = 'curl -i -X POST -H "Content-Type: application/json" -d "{\"email\": \"mailchik@gmail.com\", \"name\": \"Marmelad\", \"password\": \"1\"}" http://users.bugred.ru/tasks/rest/doregister'
CURL_3 = 'curl -d "{\"email\": \"mailchik1@gmail.com\", \"name\": \"Marmelad1\", \"password\": \"1\"}" http://users.bugred.ru/tasks/rest/doregister'

