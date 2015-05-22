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
})();
