# API Reference

Base URL: `http://localhost:5000`

## Authentication

All protected endpoints require `Authorization: Bearer <token>` header.

## Endpoints

### Auth
- `POST /api/auth/register` — `{phone, password, name}`
- `POST /api/auth/login` — `{phone, password}` → `{access_token, refresh_token}`
- `GET  /api/auth/profile` — returns user object
- `PUT  /api/auth/profile` — update name/email
- `POST /api/auth/logout` — revoke token
- `POST /api/auth/refresh` — new access token from refresh token

### Payment
- `POST /api/payment/initiate` — `{package_id}` → `{redirect_url}`
- `GET  /api/payment/status/<tracking_id>` — poll status
- `GET  /api/payment/history` — paginated list
- `GET  /api/payment/packages` — available WiFi packages

### Devices
- `GET  /api/devices` — list registered devices
- `POST /api/devices/whitelist` — `{mac_address, device_name}`
- `GET  /api/devices/<id>` — device detail
- `DELETE /api/devices/<id>` — revoke device

### Admin (requires admin JWT)
- `GET  /api/admin/dashboard` — stats
- `GET  /api/admin/users` — paginated user list
- `PUT  /api/admin/users/<id>/suspend` — suspend user
- `GET  /api/admin/payments` — all payments
- `GET  /api/admin/devices/<id>/block` — block device
- `GET  /api/admin/logs` — audit log

### Webhooks
- `GET  /webhook/pesapal` — PesaPal IPN notification
- `GET  /webhook/pesapal/callback` — post-payment browser redirect
