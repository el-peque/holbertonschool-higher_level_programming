#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const axios = require('axios').default;

async function getCharacter (url) {
  await axios.get(url)
    .then(function (response) {
      console.log(response.data.name);
    });
}

async function getFilm (url) {
  await axios.get(url)
    .then(async function (response) {
      let character;
      for (character of response.data.characters) {
        await getCharacter(character);
      }
    });
}

getFilm(url);
