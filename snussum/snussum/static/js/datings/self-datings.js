(function(){
  "use strict";
  $(document).ready(function(){
    var self_dating_applies_list = $("ul.self-dating-applies");

    $(self_dating_applies_list).find(".btn-accept").click(function(){
      $(this).closest("div.edited").hide();
      $(this).closest("li.self-dating-apply").find(".editing-accept").show();
    });

    $(self_dating_applies_list).find(".btn-refuse").click(function(){
      $(this).closest("div.edited").hide();
      $(this).closest("li.self-dating-apply").find(".editing-refuse").show();
    });
  });

  $(document).ready(function(){
    $("section#self-dating-new").find("#id_content").on("summernote.change", function(){
      var length = $(this).code().replace(/<(?:.|\n)*?>/gm, '').length;
      var form = $(this).parent(".form-group");
      var success_msg = $(form).find("p.success");
      var danger_msg = $(form).find("p.danger");
      var button = $(form).parent("form").find("button[type='submit']");

      if (length > 200) {
        $(danger_msg).hide();
        $(success_msg).show();
        $(button).prop("disabled", false);
      } else {
        $(success_msg).hide();
        $(danger_msg).show();
        $(button).prop("disabled", true);
      }
    });
  });
})();
