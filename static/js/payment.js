/**
 * payment.js — Payment form and PesaPal redirect flow
 *
 * Functions to implement:
 *   initPaymentForm()          → attach click handlers to .btn-buy buttons
 *   submitPayment(packageId)   → POST /api/payment/initiate → redirect to PesaPal URL
 *   pollPaymentStatus(trackId) → poll GET /api/payment/status/<id> every 5s
 *   handlePaymentRedirect()    → read OrderTrackingId from URL, show result
 *   showProcessing()           → show loading overlay
 *   hideProcessing()           → hide loading overlay
 */

'use strict';

function initPaymentForm() {
  // TODO: document.querySelectorAll('.btn-buy').forEach(...)
  throw new Error('initPaymentForm: not implemented');
}

function submitPayment(packageId) {
  // TODO: POST /api/payment/initiate, then window.location = redirect_url
  throw new Error('submitPayment: not implemented');
}

function pollPaymentStatus(orderTrackingId) {
  // TODO: setInterval → GET status → clear on completed/failed
  throw new Error('pollPaymentStatus: not implemented');
}

function handlePaymentRedirect() {
  // TODO: new URLSearchParams(window.location.search).get('OrderTrackingId')
  throw new Error('handlePaymentRedirect: not implemented');
}
