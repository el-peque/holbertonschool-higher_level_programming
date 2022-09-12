#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const axios = require('axios').default;

axios.get(url)
  .then(function (response) {
    let character;
    for (character of response.data.characters) {
    axios.get(character)
      .then(function (response) {
        console.log(response.data.name);
    })}
  });
