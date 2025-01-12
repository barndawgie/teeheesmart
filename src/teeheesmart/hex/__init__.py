"""Encapsulates Hex Protocol communication and devices"""

from ..media_switch import MediaSwitch as MediaSwitchProtocol
from .io import TcpDevice, TcpEndpoint
from .media_switch import MediaSwitch


def get_tcp_media_switch(
    host: str, port: int | None = None, timeout_sec: float | None = None
) -> MediaSwitchProtocol:
    if timeout_sec is None:
        # Let `TcpEndpoint` manage timeout
        endpoint = TcpEndpoint(host, port)
    else:
        endpoint = TcpEndpoint(host, port, timeout_sec)
    tcp_device = TcpDevice(endpoint)
    return MediaSwitch(tcp_device)
