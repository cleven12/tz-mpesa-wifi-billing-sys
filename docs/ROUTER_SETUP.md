# Router Setup (ZLT X17U)

## Enable SSH

1. Login to router admin: `http://192.168.1.1`
2. Go to **System → SSH** and enable SSH daemon.
3. Set a strong password for the `admin` account.

## Network Topology

```
Internet ──▶ ZLT X17U ──▶ (WiFi SSID: HotSpot-TZ)
                  │
              Flask server (192.168.1.x)
```

## MAC Whitelist Commands

The `RouterService._exec()` will run commands similar to:

```
# Add MAC
iwpriv wl0 set macmode=2
iwpriv wl0 set maclist=AA:BB:CC:DD:EE:FF

# Remove MAC
iwpriv wl0 set maclist=
```

Exact commands depend on firmware version — check `services/router_service.py`.

## Bandwidth Limiting

The router supports per-client bandwidth limits via `tc` (traffic control).
See `RouterService.set_bandwidth_limit()`.
