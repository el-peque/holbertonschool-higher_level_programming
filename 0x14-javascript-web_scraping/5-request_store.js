#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const axios = require('axios').default;
axios.get(url)
  .then(function (response) {
    fs.writeFile(path, response.data, 'utf8', err => {
      if (err) {
        return console.log(err);
      }
    });
  });
