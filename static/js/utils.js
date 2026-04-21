/**
 * utils.js — Shared JavaScript utility functions (loaded on every page)
 *
 * Functions to implement:
 *   - apiRequest(method, url, body, token) — fetch wrapper with JSON headers
 *   - getToken()                           — read JWT from localStorage
 *   - saveToken(token)                     — write JWT to localStorage
 *   - clearToken()                         — remove JWT from localStorage
 *   - getQueryParam(name)                  — parse URL query string
 *   - debounce(fn, delay)                  — debounce helper
 *   - escapeHtml(str)                      — basic XSS sanitiser
 */
