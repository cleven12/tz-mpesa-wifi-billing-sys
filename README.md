# TZ M-Pesa WiFi Billing System

[![CI](https://github.com/cleven12/tz-mpesa-wifi-billing-sys/actions/workflows/tests.yml/badge.svg)](https://github.com/cleven12/tz-mpesa-wifi-billing-sys/actions)
[![Python](https://img.shields.io/badge/python-3.11-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Overview

A Flask-based WiFi hotspot billing system for Tanzania. Customers pay via
**PesaPal** (M-Pesa, Tigo, Airtel), after which their device MAC address is
automatically whitelisted on the router — granting timed internet access.

**Stack:** Python 3.11 · Flask 3 · PostgreSQL · PesaPal v3 · ZLT X17U (SSH) · ngrok
