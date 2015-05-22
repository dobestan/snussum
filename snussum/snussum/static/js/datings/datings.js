(function(){
  "use strict";
  $(document).ready(function(){
    var comments = $("section#comments");
    var dating_hash_id = $(comments).data("hash-id");

    $("section#comments button").click(function(){
      var content = $(comments).find("textarea").val();
      var data = {
        'content': content
      };
      
      function kakaotalk(content){
        var html = '<div class="row">\
          <div class="comment comment-by-me col-xs-9 col-xs-offset-3">\
            <div class="media">\
              <div class="media-body">\
                <p>\
                CONTENT\
                </p>\
              </div>\
            </div>\
          </div>\
        </div>'.replace('CONTENT', content);

        $(comments).find("div.kakaotalk").append(html);
        $(comments).find("textarea").val("");
      };
      
      $.ajax({
        url: '/api/ssum/' + dating_hash_id + '/comment/',
        type: 'POST',
        data: data,
        success: function(result){
          kakaotalk(result.content);
        },
        error: function(result){
        }
      });
    });
  });
})();
