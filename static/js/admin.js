/**
 * admin.js — Admin dashboard interactivity
 *
 * Functions to implement:
 *   initAdminDashboard()  → load stats, recent payments on page load
 *   loadStats()           → GET /api/admin/stats → update stat cards
 *   loadRecentPayments()  → GET /api/admin/payments → populate table
 *   exportTableToCSV(id)  → download visible table rows as CSV file
 *   suspendUser(userId)   → PUT /api/admin/users/:id/suspend
 *   blockDevice(deviceId) → POST /api/admin/devices/:id/block
 */

'use strict';

function initAdminDashboard() {
  // TODO: loadStats(); loadRecentPayments();
  throw new Error('initAdminDashboard: not implemented');
}

function exportTableToCSV(tableId) {
  // TODO: read table rows, build CSV string, trigger download
  throw new Error('exportTableToCSV: not implemented');
}
