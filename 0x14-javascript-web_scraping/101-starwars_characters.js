#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const axios = require('axios').default;

function getCharacter (url) {
  axios.get(url)
    .then(function (response) {
      console.log(response.data.name);
    });
}

axios.get(url)
  .then(function (response) {
    let character;
    for (character of response.data.characters) {
      getCharacter(character);
    }
  });
