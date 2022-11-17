#!/usr/bin/node
const request = require('request');
const ep = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + ep, function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
