#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const strig = process.argv[3];
fs.appendFile(filename, strig, 'utf-8', function (error) {
  if (error) throw error;
});
