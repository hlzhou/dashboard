// Generated by CoffeeScript 1.6.1
(function() {

  $(function() {
    return (function() {
      $.get('/package_list', function(response) {
        console.log(JSON.stringify(response));
        return $('#package_list .names').html(response.people[0]);
      });
      return setTimeout(arguments.callee, 10000);
    })();
  });

}).call(this);
