/**
 * websocket.js — SocketIO real-time payment status updates
 *
 * Events:
 *   payment_completed  → {order_tracking_id, confirmation_code, package_name}
 *   payment_failed     → {order_tracking_id, reason}
 *   session_expiring   → {device_id, minutes_remaining}
 *
 * Functions to implement:
 *   initSocketIO()             → io.connect('/'), register handlers
 *   onPaymentStatusUpdate(e)   → update DOM when payment completes
 *   onSessionExpiring(e)       → show countdown banner
 */

'use strict';

function initSocketIO() {
  // TODO: const socket = io('/'); socket.on('payment_completed', onPaymentStatusUpdate);
  throw new Error('initSocketIO: not implemented');
}

function onPaymentStatusUpdate(event) {
  // TODO: update payment status UI, show success/fail banner
  throw new Error('onPaymentStatusUpdate: not implemented');
}

function onSessionExpiring(event) {
  // TODO: show banner "Your session expires in X minutes"
  throw new Error('onSessionExpiring: not implemented');
}
