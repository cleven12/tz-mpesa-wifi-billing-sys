/**
 * payment.js — Payment page logic
 *
 * Functions to implement:
 *   - loadPackageDetails(packageId)          — populate summary from URL param
 *   - initiatePayment()                      — POST /api/payment/initiate
 *   - pollPaymentStatus(checkoutRequestId)   — setInterval poll every 1s
 *   - onPaymentSuccess(data)                 — redirect to /success
 *   - onPaymentFailure(data)                 — show error, re-enable button
 *   - startCountdownTimer(seconds)           — display countdown on screen
 */
