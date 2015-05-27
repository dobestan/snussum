(function(){
  "use strict";

  $(document).ready(function(){
    var image = $("section#contact").find("img");
    var contact_section = $("section#snussum-contact");
    var button = $(contact_section).find("button");

    $(image).click(function(){
      $(contact_section).toggle();
    });

    $(button).click(function(){
      var content = $(contact_section).find("textarea#contact_content").val();
      var contact = $(contact_section).find("input#contact_contact").val();

      var data = {
        'content': content,
        'contact': contact
      };

      $.ajax({
        url: '/api/contact/',
        type: 'POST',
        data: data,
        success: function(result){
          $(contact_section).toggle();
          $.notify({message: '성공적으로 피드백/문의사항이 전달되었습니다.'},
            {type: "success"});
        },
        error: function(result){
          $.notify({message: '현재 서버와의 통신에 문제가 있습니다.'},
            {type: "danger"});
        }
      });
    });
  });
})();
