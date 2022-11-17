#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const charx = films[i].characters;
      for (const x in charx) {
        if (charx[x].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error Code: ' + response.statusCode);
  }
});
