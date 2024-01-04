request = require("request");

function printCharacters(characters, index) {
  if (index < characters.length) {
    request(
      { url: characters[index], json: true },
      function (error, response, body) {
        if (!error && response.statusCode == 200) {
          console.log(body.name);
          printCharacters(characters, index + 1);
        }
      }
    );
  }
}

function main() {
  const movieId = process.argv[2];
  request(
    { url: `https://swapi.dev/api/films/${movieId}/`, json: true },
    function (error, response, body) {
      if (!error && response.statusCode == 200) {
        printCharacters(body.characters, 0);
      }
    }
  );
}
