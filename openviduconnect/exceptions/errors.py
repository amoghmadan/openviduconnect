from __future__ import annotations

from .base import OpenViduError


class SessionBodyParameterError(OpenViduError):
    """Create Session Bad Body"""

    status = 400


class SessionExistsError(OpenViduError):
    """Create Custom Session Id Exists"""

    status = 409


class SessionNotFoundError(OpenViduError):
    """Session Does Not Exist"""

    status = 404


class ConnectionBodyParameterError(OpenViduError):
    """Create Connection Bad Body"""

    status = 400


class ConnectionIPCAMError(OpenViduError):
    """Type: IPCAM, can only cause this error"""

    status = 500


class SessionDoesNotExistError(OpenViduError):
    """Session Does Not Exist"""

    status = 400


class ConnectionNotFound(OpenViduError):
    """Connection Not Found"""

    status = 404


class SessionOrConnectionDoesNotExist(OpenViduError):
    """Session or Connection Does Not Exist"""

    status = 404


class RecordingBodyParameterError(OpenViduError):
    """Recording Body Parameter Error"""

    status = 400


class RecordingResolutionOrBrowserSettingsError(OpenViduError):
    """Resolution not supported or Browser has audio or video off"""

    status = 422


class RecordingNoConnectedParticipantsError(OpenViduError):
    """No participants to record"""

    status = 406


class RecordingNotConfiguredForMediaNodeError(OpenViduError):
    """Recording can not be done on the media node"""

    status = 409


class RecordingDisabledOnServerError(OpenViduError):
    """Recording disabled on server"""

    status = 501


class RecordingNotFoundError(OpenViduError):
    """Recording not found"""

    status = 404


class RecordingStartingProgressError(OpenViduError):
    """Recording has not yet started"""

    status = 406


class RecordingNotCompletedError(OpenViduError):
    """Stop recording before accessing it"""

    status = 409
