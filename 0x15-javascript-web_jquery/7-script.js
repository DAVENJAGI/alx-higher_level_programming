//Javascript that fetched and replaces name with jQuery API.

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
	$('DIV#character').html(data.name);
});
