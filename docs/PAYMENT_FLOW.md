# Payment Flow

## Happy Path

```
Customer                   Flask API               PesaPal               Router
   │                           │                      │                     │
   │  POST /payment/initiate   │                      │                     │
   │──────────────────────────▶│                      │                     │
   │                           │  SubmitOrderRequest  │                     │
   │                           │─────────────────────▶│                     │
   │                           │  {redirect_url}       │                     │
   │                           │◀─────────────────────│                     │
   │  302 → redirect_url       │                      │                     │
   │◀──────────────────────────│                      │                     │
   │                           │                      │                     │
   │  Pays on PesaPal page     │                      │                     │
   │──────────────────────────────────────────────────▶│                    │
   │                           │  GET /webhook/pesapal │                     │
   │                           │◀─────────────────────│                     │
   │                           │  GetTransactionStatus│                     │
   │                           │─────────────────────▶│                     │
   │                           │  {COMPLETED}          │                     │
   │                           │◀─────────────────────│                     │
   │                           │  SSH add_mac_whitelist│                     │
   │                           │────────────────────────────────────────────▶│
   │  SMS: "WiFi active"       │                      │                     │
```

## Timeout Flow

If PesaPal does not call the IPN within `PAYMENT_TIMEOUT_MINUTES`, a background
job marks the payment as `timeout` and no access is granted.
