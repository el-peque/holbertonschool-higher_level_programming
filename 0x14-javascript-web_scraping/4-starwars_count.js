#!/usr/bin/node

const url = process.argv[2];
const axios = require('axios').default;
axios.get(url)
  .then(function (response) {
    let movie;
    let count = 0;
    for (movie of response.data.results) {
      if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  });
