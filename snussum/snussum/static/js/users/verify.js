(function(){
  "use strict";
  $(document).ready(function(){
    var boy = $("section#verify-profile-gender").find("img#boy");
    var girl = $("section#verify-profile-gender").find("img#girl");

    var boy_makeup = $("section#verify-profile-gender").find("img#boy_makeup");
    var girl_makeup = $("section#verify-profile-gender").find("img#girl_makeup");

    var input_is_boy = $("section#verify-profile-gender").find("input#id_is_boy");

    $(boy).click(function(){
      $(girl_makeup).hide();
      $(girl).show();

      $(boy).hide();
      $(boy_makeup).show();
      $(boy_makeup).addClass("active");

      $(input_is_boy).prop("value", "boy");
    });

    $(girl).click(function(){
      $(boy_makeup).hide();
      $(boy).show();

      $(girl).hide();
      $(girl_makeup).show();
      $(girl_makeup).addClass("active");

      $(input_is_boy).prop("value", "girl");
    });

    $("section#verify-profile-introduce").find("#id_profile_introduce").on('summernote.change', function() {
      var length = $(this).code().replace(/<(?:.|\n)*?>/gm, '').length;
      console.log(length);
      var form = $(this).parent(".form-group");

      var success_msg = $(form).find("p.success");
      var danger_msg = $(form).find("p.danger");

      if (length > 50) {
        $(form).removeClass("border-danger").addClass("border-success");
        $(danger_msg).hide();
        $(success_msg).show();

      } else {
        $(form).removeClass("border-success").addClass("border-danger");
        $(success_msg).hide();
        $(danger_msg).show();
      }
    });
  });
})();
