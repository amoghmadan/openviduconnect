from __future__ import annotations

from base64 import b64encode
from urllib.parse import urljoin


class BaseClient(object):
    """
    Introduction: OpenVidu client is used to connect to the platform using the REST APIs.
    Objective: The wrapper client is built for handling the APIs with method calls.
    Params: Host and the Secret Key
    """

    def __init__(self: BaseClient, host: str, secret: str, verify: bool = False, timeout: int = None) -> None:
        """
        @:param host: Host of the platform https://<host.com>
        @:param secret: Secret Key of the platform
        @:param verify: Verify URL (Default: False)
        @:param timeout: Time Out of the API call (Default: None)
        """

        self._host = host
        self._verify = verify
        self._timeout = timeout

        secret = b64encode(secret.encode()).decode()
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic OPENVIDUAPP:%s" % (secret,)
        }

        api_root = urljoin(self._host, "openvidu/api")
        self._apis = {
            "sessions": urljoin(api_root, "sessions"),
            "recordings": urljoin(api_root, "recordings")
        }

    def __repr__(self):
        """."""

        return "<%s %r>" % (self.__class__.__name__, self._host)
