$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (response, code) => {
  $('#character').text(response.name);
});
