/**
 * utils.js — Shared utility functions
 *
 * Functions to implement:
 *   formatCurrency(amount, currency)  → "TZS 1,500"
 *   formatPhone(phone)                → "+255 7XX XXX XXX"
 *   showAlert(message, type)          → insert alert div into DOM
 *   hideAlert()                       → remove alert div
 *   formatDate(isoString)             → "05 May 2026, 14:30"
 *   copyToClipboard(text)             → write to clipboard API
 */

'use strict';

/**
 * Format a number as a currency string.
 * @param {number} amount
 * @param {string} [currency='TZS']
 * @returns {string}
 */
function formatCurrency(amount, currency = 'TZS') {
  // TODO: implement
  throw new Error('formatCurrency: not implemented');
}

/**
 * Format a phone number for display.
 * @param {string} phone E.164 format
 * @returns {string}
 */
function formatPhone(phone) {
  // TODO: implement
  throw new Error('formatPhone: not implemented');
}

/**
 * Show an alert banner in #alert-container.
 * @param {string} message
 * @param {'success'|'error'|'warning'|'info'} type
 */
function showAlert(message, type = 'info') {
  // TODO: implement
  throw new Error('showAlert: not implemented');
}

function hideAlert() {
  // TODO: implement
}
