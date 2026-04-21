"""Device registration and router MAC whitelist management."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class DeviceService:
    """Syncs Device records with the router MAC whitelist."""

    def __init__(self) -> None:
        pass  # TODO: instantiate RouterService

    def register_device(
        self, user_id: int, mac_address: str, device_name: Optional[str] = None
    ) -> dict:
        """Create or update a Device record and whitelist on the router.

        Args:
            user_id: Owner user FK.
            mac_address: Canonical MAC (XX:XX:XX:XX:XX:XX).
            device_name: Optional human-readable label.

        Returns:
            Device dict.
        """
        raise NotImplementedError("TODO")

    def revoke_device(self, device_id: int, admin_id: Optional[int] = None) -> bool:
        """Remove device from DB and router whitelist.

        Args:
            device_id: PK of the Device row.
            admin_id: If provided, write an AdminLog entry.

        Returns:
            bool: True on success.
        """
        raise NotImplementedError("TODO")

    def get_devices_for_user(self, user_id: int) -> list:
        """Return all Device dicts for a user."""
        raise NotImplementedError("TODO")

    def sync_router_state(self) -> dict:
        """Compare DB whitelist with live router ARP table; return discrepancies.

        Returns:
            dict with keys: db_only (list), router_only (list).
        """
        raise NotImplementedError("TODO")

    def expire_sessions(self) -> int:
        """Revoke access for devices whose payment sessions have expired.

        Returns:
            int: Number of devices revoked.
        """
        raise NotImplementedError("TODO")
