import inspect
import logging
import requests

logger = logging.getLogger("example." + __name__)


class BugRedClient:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def verify_response(
            self, res: requests.Response, ok_status=200
    ) -> requests.Response:
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            raise ValueError(
                f"Verified response: function {func} failed: "
                f"server responded {res.status_code} "
                f"with data: {res.content}"
            )
        else:
            logger.info(
                f"Verified response: function {func} code {res.status_code}"
            )
        return res

    vr = verify_response

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self._s.get(self.host, json=data)

    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 200:
            raise Exception("Unable to authorize using given credentials")
        self._s.cookies = res.cookies

    def do_register(self, data: dict):
        return self._s.post(self.host + "/tasks/rest/doregister", json=data)
