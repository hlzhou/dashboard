// Generated by CoffeeScript 1.6.1

/* About
*/


/* License and Warranty
*/


(function() {

  $(function() {
    return (function() {
      $.get('/news', function(news) {
        return $('#news .title').html(news.title);
      });
      return setTimeout(arguments.callee, 10000);
    })();
  });

}).call(this);
