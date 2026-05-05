# Deployment Guide

## Development (ngrok)

```bash
make install
cp .env.example .env
# Edit .env with your credentials
make db-init
make db-seed
bash scripts/deploy_ngrok.sh
```

## Production (Docker + Gunicorn)

```bash
cp .env.example .env
# Set PESAPAL_ENVIRONMENT=production, DATABASE_URL=postgresql://...
make docker-up
```

## Environment Variables Checklist

- [ ] `SECRET_KEY` — random 32+ chars
- [ ] `JWT_SECRET_KEY` — random 32+ chars
- [ ] `DATABASE_URL` — PostgreSQL connection string
- [ ] `PESAPAL_CONSUMER_KEY` / `PESAPAL_CONSUMER_SECRET`
- [ ] `PESAPAL_ENVIRONMENT=production`
- [ ] `PESAPAL_IPN_URL` — public HTTPS URL
- [ ] `ROUTER_HOST` / `ROUTER_SSH_USER` / `ROUTER_SSH_PASSWORD`
