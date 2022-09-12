#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/';
const axios = require('axios').default;
let movie; let count = 0;
axios.get(url)
  .then(function (response) {
    for (movie of response.data.results) {
      if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  });
