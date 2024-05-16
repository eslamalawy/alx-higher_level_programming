#!/usr/bin/node
// Creates file and writes content from args

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
