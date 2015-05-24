/*jshint multistr: true */
(function(){
  "use strict";

  // Verify SNU
  // 1. MySNU Email Verification
  $(document).ready(function(){
    $("input#mysnu-email-button").click(function(){
      var username = $("input#mysnu-email-username").val();
      var data = {'username': username};

      $.ajax({
        url: '/api/users/mysnu/email/',
        type: 'POST',
        data: data,
        success: function(result){
          $.notify(
            {icon: "fa fa-envelope" ,message: "입력하신 이메일로 인증 메일이 발송되었습니다."},
            {type: 'success'}
          );
        },
        error: function(result){
          $.notify(
            {
              icon: "fa fa-exclamation-triangle",
              message: "현재 서버와의 통신에 문제가 있습니다.\
              지속적으로 동일한 문제가 발생하는 경우 다른 인증 방법을 통해서\
              인증해주시면 감사하겠습니다."
            },
            {type: 'danger'}
          );
        }
      });
    });
  });

  // 2. MySNU Login Verification
  $(document).ready(function(){
    $("input#mysnu-login-button").click(function(){
      $.notify(
        {icon: "fa fa-lock" ,message: "마이스누 로그인 인증이 시작되었습니다. \
        입력하신 아이디, 비밀번호는 공인 인증서(SSL)을 통해서 암호화됩니다."},
        {type: 'success'}
      );

      var username = $("input#mysnu-username").val();
      var password = $("input#mysnu-password").val();

      var data = {
        'username': username,
        'password': password
      };

      $.ajax({
        url: '/api/users/mysnu/login/',
        type: 'POST',
        data: data,
        success: function(result){
          $.notify(
            {message: "마이스누 로그인 인증에 성공하였습니다."},
            {type: 'success'}
          );
        },
        error: function(result){
          $.notify(
            {
              icon: "fa fa-exclamation-triangle",
              message: "마이스누 로그인 인증에 실패하였습니다.\
              지속적으로 동일한 문제가 발생하는 경우 다른 인증 방법을 통해서\
              인증해주시면 감사하겠습니다."
            },
            {type: 'danger'}
          );
        }
      });
    });
  });

  // 3. Snulife Login Verification
  $(document).ready(function(){
    $("input#snulife-login-button").click(function(){
      $.notify(
        {icon: "fa fa-lock" ,message: "스누라이프 로그인 인증이 시작되었습니다. \
        입력하신 아이디, 비밀번호는 공인 인증서(SSL)을 통해서 암호화됩니다."},
        {type: 'success'}
      );

      var username = $("input#snulife-username").val();
      var password = $("input#snulife-password").val();

      var data = {
        'username': username,
        'password': password
      };

      $.ajax({
        url: '/api/users/snulife/login/',
        type: 'POST',
        data: data,
        success: function(result){
          $.notify(
            {message: "스누라이프 로그인 인증에 성공하였습니다."},
            {type: 'success'}
          );
        },
        error: function(result){
          $.notify(
            {
              icon: "fa fa-exclamation-triangle",
              message: "스누라이프 로그인 인증에 실패하였습니다.\
              지속적으로 동일한 문제가 발생하는 경우 다른 인증 방법을 통해서\
              인증해주시면 감사하겠습니다."
            },
            {type: 'danger'}
          );
        }
      });
    });
  });

  // Verify Profile
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
      var form = $(this).parent(".form-group");

      var success_msg = $(form).find("p.success");
      var danger_msg = $(form).find("p.danger");

      var button = $("#verify-profile").find("button[type='submit']");

      if (length > 50) {
        $(form).removeClass("border-danger").addClass("border-success");
        $(danger_msg).hide();
        $(success_msg).show();

        $(button).prop("disabled", false);

      } else {
        $(form).removeClass("border-success").addClass("border-danger");
        $(success_msg).hide();
        $(danger_msg).show();

        $(button).prop("disabled", true);
      }
    });
  });
})();
