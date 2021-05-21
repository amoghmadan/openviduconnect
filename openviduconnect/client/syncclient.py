from __future__ import annotations

from urllib.parse import urljoin

from httpx import Client, Response

from .base import BaseClient
from ..exceptions import (
    SessionBodyParameterError,
    SessionExistsError,
    SessionNotFoundError,
    ConnectionBodyParameterError,
    ConnectionIPCAMError,
    SessionDoesNotExistError,
    ConnectionNotFound,
    SessionOrConnectionDoesNotExist,
    RecordingBodyParameterError,
    RecordingResolutionOrBrowserSettingsError,
    RecordingNoConnectedParticipantsError,
    RecordingNotConfiguredForMediaNodeError,
    RecordingDisabledOnServerError,
    RecordingNotFoundError,
    RecordingStartingProgressError,
    RecordingNotCompletedError,
)


class OpenViduClient(BaseClient):
    """."""

    def __enter__(self):
        """."""

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """."""

        pass

    def create_session(self: OpenViduClient, **kwargs: str) -> dict:
        """."""

        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.post(self._apis["sessions"], headers=self._headers, json=kwargs)

        if response.status_code == 400:
            raise SessionBodyParameterError("Problem with some body parameter")
        if response.status_code == 409:
            raise SessionExistsError("Parameter customSessionId corresponds to an existing Session")

        return response.json()

    def get_session(self: OpenViduClient, session_id: str) -> dict:
        """."""

        url: str = urljoin(self._apis["sessions"], session_id)
        with Client(verify=self._verify, headers=self._timeout) as client:
            response: Response = client.get(url, headers=self._headers)

        if response.status_code == 404:
            raise SessionNotFoundError("No Session exists for the passed SESSION_ID")

        return response.json()

    def get_sessions(self: OpenViduClient) -> dict:
        """."""

        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.get(self._apis["sessions"], headers=self._headers)

        return response.json()

    def delete_session(self: OpenViduClient, session_id: str) -> dict:
        """."""

        url: str = urljoin(self._apis["sessions"], session_id)
        with Client(verify=self._verify, headers=self._timeout) as client:
            response: Response = client.delete(url, headers=self._headers)

        if response.status_code == 404:
            raise SessionNotFoundError("No Session exists for the passed SESSION_ID")

        return response.json()

    def create_connection(self: OpenViduClient, session_id: str, **kwargs: str) -> dict:
        """."""

        session_url: str = urljoin(self._apis["sessions"], session_id)
        url: str = urljoin(session_url, "connection")
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.post(url, headers=self._headers, json=kwargs)

        if response.status_code == 400:
            raise ConnectionBodyParameterError("Problem with some body parameter")
        if response.status_code == 404:
            raise SessionNotFoundError("No session exists for the passed SESSION_ID")
        if response.status_code == 500:
            raise ConnectionIPCAMError("Unexpected error when creating the Connection object")

        return response.json()

    def get_connection(self: OpenViduClient, session_id: str, connection_id: str) -> dict:
        """."""

        session_url: str = urljoin(self._apis["sessions"], session_id)
        connection_url: str = urljoin(session_url, "connection")
        url: str = urljoin(connection_url, connection_id)
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.get(url, headers=self._headers)

        if response.status_code == 400:
            raise SessionDoesNotExistError("No Session exists for the passed SESSION_ID")
        if response.status_code == 404:
            raise ConnectionNotFound("No Connection exists for the passed CONNECTION_ID")

        return response.json()

    def get_connections(self: OpenViduClient, session_id: str) -> dict:
        """."""

        session_url: str = urljoin(self._apis["session"], session_id)
        url: str = urljoin(session_url, "connection")
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.get(url, headers=self._headers)

        if response.status_code == 404:
            raise SessionNotFoundError("No Session exists for the passed SESSION_ID")

        return response.json()

    def update_connection(self: OpenViduClient, session_id: str, connection_id: str, **kwargs: str) -> dict:
        """."""

        session_url: str = urljoin(self._apis["session"], session_id)
        connection_url: str = urljoin(session_url, "connection")
        url: str = urljoin(connection_url, connection_id)
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.patch(url, headers=self._headers, json=kwargs)

        if response.status_code == 400:
            raise ConnectionBodyParameterError("Problem with some body parameter")
        if response.status_code == 404:
            raise SessionOrConnectionDoesNotExist(
                "No Session exists for the passed SESSION_ID, or no Connection exists for the passed CONNECTION_ID"
            )

        return response.json()

    def delete_connection(self: OpenViduClient, session_id: str, connection_id: str) -> dict:
        """."""

        session_url: str = urljoin(self._apis["session"], session_id)
        connection_url: str = urljoin(session_url, "connection")
        url: str = urljoin(connection_url, connection_id)
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.delete(url, headers=self._headers)

        if response.status_code == 400:
            raise SessionDoesNotExistError("No Session exists for the passed SESSION_ID")
        if response.status_code == 404:
            raise ConnectionNotFound("No Connection for the passed CONNECTION_ID")

        return response.json()

    def start_recording(self: OpenViduClient, **kwargs: str) -> dict:
        """."""

        url: str = urljoin(self._apis["recordings"], "start")
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.post(url, headers=self._headers, json=kwargs)

        if response.status_code == 400:
            raise RecordingBodyParameterError("Problem with some body parameter")
        if response.status_code == 404:
            raise SessionNotFoundError("No session exists for the passed session body parameter")
        if response.status_code == 406:
            raise RecordingNoConnectedParticipantsError("The session has no connected participants")
        if response.status_code == 409:
            raise RecordingNotConfiguredForMediaNodeError(
                "The session is not configured for using MediaMode ROUTED or it is already being recorded"
            )
        if response.status_code == 422:
            raise RecordingResolutionOrBrowserSettingsError(
                "resolution parameter exceeds acceptable values (for both width and height, min 100px and max 1999px) "
                "or trying to start a recording with both hasAudio and hasVideo to false"
            )
        if response.status_code == 501:
            raise RecordingDisabledOnServerError(
                "OpenVidu Server recording module is disabled: "
                "OPENVIDU_RECORDING configuration property is set to false"
            )

        return response.json()

    def stop_recording(self: OpenViduClient, recording_id: str) -> dict:
        """."""

        stop_url: str = urljoin(self._apis["recordings"], "stop")
        url: str = urljoin(stop_url, recording_id)
        with Client() as client:
            response: Response = client.post(url, headers=self._headers)

        if response.status_code == 404:
            raise RecordingNotFoundError("No recording exists for the passed RECORDING_ID")
        if response.status_code == 406:
            raise RecordingStartingProgressError(
                "Recording has starting status. Wait until started status before stopping the recording"
            )
        if response.status_code == 501:
            raise RecordingDisabledOnServerError(
                "OpenVidu Server recording module is disabled: "
                "OPENVIDU_RECORDING configuration property is set to false"
            )

        return response.json()

    def get_recording(self: OpenViduClient, recording_id: str) -> dict:
        """."""

        url: str = urljoin(self._apis["recordings"], recording_id)
        with Client() as client:
            response: Response = client.get(url, headers=self._headers)

        if response.status_code == 404:
            raise RecordingNotFoundError("No recording exists for the passed RECORDING_ID")
        if response.status_code == 501:
            raise RecordingDisabledOnServerError(
                "OpenVidu Server recording module is disabled: "
                "OPENVIDU_RECORDING configuration property is set to false"
            )

        return response.json()

    def get_recordings(self: OpenViduClient) -> dict:
        """."""

        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.get(self._apis["recordings"], headers=self._headers)

        if response.status_code == 501:
            raise RecordingDisabledOnServerError(
                "OpenVidu Server recording module is disabled: "
                "OPENVIDU_RECORDING configuration property is set to false"
            )

        return response.json()

    def delete_recording(self: OpenViduClient, recording_id: str) -> dict:
        """."""

        url: str = urljoin(self._apis["recordings"], recording_id)
        with Client(verify=self._verify, timeout=self._timeout) as client:
            response: Response = client.delete(url, headers=self._headers)

        if response.status_code == 404:
            raise RecordingNotFoundError("No recording exists for the passed RECORDING_ID")
        if response.status_code == 409:
            raise RecordingNotCompletedError("The recording has started status. Stop it before deletion")
        if response.status_code == 501:
            raise RecordingDisabledOnServerError(
                "OpenVidu Server recording module is disabled: "
                "OPENVIDU_RECORDING configuration property is set to false"
            )

        return response.json()
