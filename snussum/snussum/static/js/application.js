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
});
