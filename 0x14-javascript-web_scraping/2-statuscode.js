#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request.get(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
