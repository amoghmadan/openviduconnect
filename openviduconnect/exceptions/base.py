from __future__ import annotations


class Error(Exception):
    """Base Error Class"""

    pass


class OpenViduError(Error):
    """OpenViduHTTPError is a base  and should not be instantiated"""

    status = None
