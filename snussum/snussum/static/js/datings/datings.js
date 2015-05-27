/*jshint multistr: true */
(function(){
  "use strict";
  $(document).ready(function(){
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
    }

    var comments = $("section#comments");
    var dating_hash_id = $(comments).data("hash-id");

    $("section#comments button").click(function(){
      var content = $(comments).find("textarea").val();

      if (content.length > 0){
        var data = {
          'content': content
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
      } else {
        $.notify(
          {
            icon: "fa fa-exclamation-triangle",
            message: "텍스트 입력 후 전송 부탁드립니다. 감사합니다."
          },
          {type: 'danger'}
        );
      }
    });
  });
})();
