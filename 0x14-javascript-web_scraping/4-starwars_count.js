#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/';
const axios = require('axios').default;
let movie; let count = 0;
axios.get(url)
  .then(function (response) {
    const movieList = response.data.results;
    for (movie of movieList) {
      const chars = movie.characters;
      if (chars.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count += 1;
      }
    }
    console.log(count);
  });
