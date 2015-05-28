(function(){
  "use strict";
  $(document).ready(function(){
    // CSRF Authentication
    // https://docs.djangoproject.com/en/1.8/ref/csrf/
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });

    // AJAX Settings - Spinner Event
    $(document).ajaxStart(function(){
      $("section#loading").removeClass("hide");
    }).ajaxStop(function(){
      $("section#loading").addClass("hide");
    });

    // Django Message Notification
    var messages = $("body#body").data("messages").split(";");
    var tags = $("body#body").data("message-tags").split(";");

    for (var i=0; i<messages.length-1; i++){
      $.notify(
        {message: messages[i]}, {type: tags[i]}
      );
    }

    // Smooth Scrolling
    $('body').scrollspy({target: '#scrollspy'});

    $(function() {
      $('a[href*=#]:not([href=#]):not([data-toggle])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top
            }, 500);
            return false;
          }
        }
      });
    });
  });
})();
