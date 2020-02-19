# Алексеева Елена
# documentation https://developer.atlassian.com/cloud/jira/platform/rest/v2/#api-rest-api-2-issueLink-linkId-get
import pytest
import requests
from requests.auth import HTTPBasicAuth
import json
from test_data.api_variables_data import GET_ISSUE_LINK, CREATE_ISSUE_LINK

"""CreateIssueLink"""


def test_create_issue():
    link = 'https://testbase.atlassian.net/rest/api/2/issue/[linked issue key]?fields=issuelinks'
    url = CREATE_ISSUE_LINK

    auth = HTTPBasicAuth("mail.for.testbase@yandex.ru", "cCehOzIeIcisnqaCzBKQ1E53")

    headers = {"Accept": "application/json",
               "Content-Type": "application/json"}

    payload = json.dumps({"outwardIssue": {"key": "MKY-1"},
                          "comment": {
                              "visibility": {
                                  "type": "group",
                                  "value": "jira-software-users"
                              },
                              "body": "Linked related issue!"
                          },
                          "inwardIssue": {
                              "key": "HSP-1"
                          },
                          "type": {
                              "name": "Duplicate"
                          }
                          })

    response = requests.request("POST", url, data=payload, headers=headers, auth=auth)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


"""GetIssueLink"""


def test_headers():
    # "Проверяем доступ к issue"
    url = GET_ISSUE_LINK.format(10200)
    auth = HTTPBasicAuth("mail.for.testbase@yandex.ru", "cCehOzIeIcisnqaCzBKQ1E53")
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, auth=auth)
    print(json.dumps(json.loads(response.text, encoding='utf-8'), sort_keys=True, indent=4, separators=(",", ": ")))
    # assert response.status_code == 200, f"Получен статус код: {response.status_code} != 200"
    # "Проверяем headers ответа"
    assert response.headers['Content-Type'] == 'application/json;charset=UTF-8', \
        f"Заголовок Content-Type = {response.headers['Content-Type']} вместо 'application/json;charset=UTF-8'"
    assert response.headers['Content-Encoding'] == 'gzip', \
        f"Заголовок Content-Encoding = {response.headers['Content-Encoding']} вместо 'gzip'"
    assert response.headers['Connection'] == 'keep-alive', \
        f"Заголовок Connection = {response.headers['Connection']} вместо 'keep-alive'"
    assert response.headers['Transfer-Encoding'] == 'chunked', \
        f"Заголовок Transfer-Encoding = {response.headers['Transfer-Encoding']} вместо 'chunked'"
    assert response.headers['Cache-Control'] == 'no-cache, no-store, no-transform', \
        f"{response.headers['Cache-Control']} != 'no-cache, no-store, no-transform'"
    assert response.headers['Server'] == 'AtlassianProxy/1.15.8.1', \
        f"{response.headers['Server']} != 'AtlassianProxy/1.15.8.1'"
    # "Проверяем headers запроса"
    assert response.request.headers['Accept-Encoding'] == 'gzip, deflate', \
        f"{response.request.headers['Accept-Encoding']} != 'gzip, deflate'"
    assert response.request.headers['Accept'] == 'application/json', \
        f"{response.request.headers['Accept']} != 'application/json'"
    assert response.request.headers['Connection'] == 'keep-alive', \
        f"{response.request.headers['Connection']} != 'keep-alive'"
    # print("referrer:", response.request.headers['referrer'])
