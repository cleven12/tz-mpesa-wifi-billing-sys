# TZ M-Pesa WiFi Billing System

[![CI](https://github.com/cleven12/tz-mpesa-wifi-billing-sys/actions/workflows/tests.yml/badge.svg)](https://github.com/cleven12/tz-mpesa-wifi-billing-sys/actions)
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Overview

A Flask-based WiFi hotspot billing system for Tanzania. Customers pay via
**PesaPal** (M-Pesa, Tigo, Airtel), after which their device MAC address is
automatically whitelisted on the router — granting timed internet access.

**Stack:** Python 3.11 · Flask 3 · PostgreSQL · PesaPal v3 · ZLT X17U (SSH) · ngrok

## Features

- PesaPal v3 payment integration (M-Pesa, Tigo Pesa, Airtel Money)
- Automatic MAC-address whitelisting via SSH after successful payment
- JWT-secured REST API with role-based access (admin / customer)
- Real-time payment status updates via SocketIO
- Africa's Talking SMS notifications
- Admin dashboard (users, payments, devices, audit log)
- ngrok tunnel for local webhook development

## Architecture

```
Browser / Mobile App
        │
        ▼
  Flask REST API  ──▶  PesaPal v3  ──▶  Customer's Phone (M-Pesa)
        │                   │
        │       IPN callback (POST /webhook/pesapal)
        │                   │
        ▼                   ▼
   PostgreSQL         PaymentService
                           │
                    DeviceService ──▶  ZLT X17U Router (SSH)
                                            │
                                     MAC Whitelist added
```

## Prerequisites

| Dependency | Version |
|---|---|
| Python | 3.11+ |
| PostgreSQL | 14+ (SQLite for dev) |
| ngrok | 3.x |
| ZLT X17U router | firmware ≥ 1.3 |
| PesaPal account | sandbox or live |

## Quick Start

```bash
git clone https://github.com/cleven12/tz-mpesa-wifi-billing-sys.git
cd tz-mpesa-wifi-billing-sys
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # fill in your credentials
python3 -c "from database.init_db import init_db; init_db()"
python3 app.py
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/register` | — | Register new user |
| POST | `/api/auth/login` | — | Login, get JWT |
| GET | `/api/auth/profile` | JWT | Get profile |
| POST | `/api/payment/initiate` | JWT | Start PesaPal payment |
| GET | `/api/payment/status/<id>` | JWT | Poll payment status |
| GET | `/api/payment/packages` | — | List WiFi packages |
| GET | `/api/devices` | JWT | List user devices |
| POST | `/api/devices/whitelist` | JWT | Whitelist MAC |
| GET | `/webhook/pesapal` | — | PesaPal IPN callback |
