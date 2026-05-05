/**
 * main.js — Entry point; initialises page-level behaviour
 *
 * Functions to implement:
 *   init()                  → called on DOMContentLoaded
 *   fetchPackages()         → GET /api/payment/packages, render cards
 *   updateBalanceDisplay()  → GET /api/auth/profile, update balance in nav
 *   handleLogout()          → POST /api/auth/logout, clear token, redirect
 */

'use strict';

document.addEventListener('DOMContentLoaded', function () {
  // TODO: call init()
});

function init() {
  // TODO: detect page, call relevant setup
  throw new Error('init: not implemented');
}

function fetchPackages() {
  // TODO: fetch('/api/payment/packages').then(renderPackages)
  throw new Error('fetchPackages: not implemented');
}

function updateBalanceDisplay() {
  // TODO: get JWT from localStorage, fetch profile, update DOM
  throw new Error('updateBalanceDisplay: not implemented');
}

function handleLogout() {
  // TODO: POST /api/auth/logout, clear localStorage, redirect to /
  throw new Error('handleLogout: not implemented');
}
