(function(){
  "use strict";

  // Profile - Account
  $(document).ready(function(){
    var account = $("section#profile").find("#account");

    var button_edited = $(account).find("button.edited");
    var button_editing = $(account).find("button.editing");

    $(button_edited).click(function(){
      $(this).parent("td").find(".edited").hide();
      $(this).parent("td").find(".editing").show();
    });
  });
  

  // Profile - Information
  $(document).ready(function(){
    var information = $("section#profile").find("#information");
    var button_edited = $(information).find("button.edited");
    var button_editing = $(information).find("button.editing");

    var edited_items = $(information).find(".edited");
    var editing_items = $(information).find(".editing");

    $(button_edited).click(function(){
      $(edited_items).hide();
      $(editing_items).show();
    });
  });


  // Profile - Condition
  $(document).ready(function(){
    var condition = $("section#profile").find("#condition");
    var button_edited = $(condition).find("button.edited");
    var button_editing = $(condition).find("button.editing");

    var edited_items = $(condition).find(".edited");
    var editing_items = $(condition).find(".editing");

    $(button_edited).click(function(){
      $(edited_items).hide();
      $(editing_items).show();
    });
  });
})();
