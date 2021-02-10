// Fetches from URL and displays the value of hello from that fetch in the HTML’s tag #hello.
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('#hello').text(data.hello);
});
