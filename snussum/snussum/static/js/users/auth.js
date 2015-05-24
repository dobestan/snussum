(function(){
  "use strict";

  // Login
  $(document).ready(function(){
    var input_username = $("section#login").find("input#id_username");
    var input_password = $("section#login").find("input#id_password");

    $(input_username).on('input', function(){
      var danger_msg = $(this).parent(".form-group").find(".danger");
      if ($(this).val().length === 0){
        danger_msg.show();
      } else {
        danger_msg.hide();
      }
    });

    $(input_password).on('input', function(){
      var danger_msg = $(this).parent(".form-group").find(".danger");
      if ($(this).val().length === 0){
        danger_msg.show();
      } else {
        danger_msg.hide();
      }
    });
  });


  // Signup
  $(document).ready(function(){
    var input_username = $("section#signup").find("input#id_username");
    var input_password1 = $("section#signup").find("input#id_password1");
    var input_password2 = $("section#signup").find("input#id_password2");

    $(input_username).on('input', function(){
      var danger_msg = $(this).parent(".form-group").find(".danger");
      if ($(this).val().length === 0){
        danger_msg.show();
      } else {
        danger_msg.hide();
      }
    });

    $(input_password1).on('input', function(){
      var danger_msg = $(this).parent(".form-group").find(".danger");
      if ($(this).val().length === 0){
        danger_msg.show();
      } else {
        danger_msg.hide();
      }
    });

    $(input_password2).on('input', function(){
      var danger_msg = $(this).parent(".form-group").find(".danger");
      var success_msg = $(this).parent(".form-group").find(".success");

      var input_password1_value = $(input_password1).val();
      var input_password2_value = $(this).val();

      if (input_password1_value === input_password2_value){
        $(danger_msg).hide();
        $(success_msg).show();
      } else {
        $(success_msg).hide();
        $(danger_msg).show();
      }
    });
  });
})();
