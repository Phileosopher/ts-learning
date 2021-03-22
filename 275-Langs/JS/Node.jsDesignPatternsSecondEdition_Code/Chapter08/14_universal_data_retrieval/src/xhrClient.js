"use strict";

const Axios = require('axios');

const baseURL = typeof window !== 'undefined' ? '/api' : 'https://localhost:3001';
const xhrClient = Axios.create({baseURL});

module.exports = xhrClient;
