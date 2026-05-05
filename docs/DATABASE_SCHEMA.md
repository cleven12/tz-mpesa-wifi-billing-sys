# Database Schema

## users
| Column | Type | Notes |
|---|---|---|
| id | INTEGER PK | |
| phone | VARCHAR(20) UNIQUE | E.164 format |
| name | VARCHAR(100) | |
| email | VARCHAR(100) | nullable |
| password_hash | VARCHAR(255) | bcrypt |
| account_balance | NUMERIC(10,2) | TZS |
| status | ENUM | active/suspended/deleted |
| created_at | DATETIME | UTC |
| last_login | DATETIME | nullable |

## payments
| Column | Type | Notes |
|---|---|---|
| id | INTEGER PK | |
| user_id | FK → users | |
| phone | VARCHAR(20) | payer phone |
| amount | NUMERIC(10,2) | TZS |
| status | ENUM | pending/completed/failed/timeout |
| order_tracking_id | VARCHAR(255) UNIQUE | PesaPal |
| merchant_reference | VARCHAR(255) | our ID |
| confirmation_code | VARCHAR(50) | receipt |

## devices
| Column | Type | Notes |
|---|---|---|
| id | INTEGER PK | |
| user_id | FK → users | |
| mac_address | VARCHAR(17) UNIQUE | AA:BB:CC:DD:EE:FF |
| status | ENUM | active/whitelisted/blocked |
| session_expires_at | DATETIME | nullable |

## transactions
One-to-one with payments. Stores raw PesaPal callback payload as JSON.

## admin_logs
Audit trail. Every admin action recorded with before/after state.
