#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const axios = require('axios').default;
axios.get(url)
  .then(function (response) {
    console.log(response.data.title);
  });
