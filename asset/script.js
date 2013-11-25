$(function() {
  function supports_placeholder() {
    return !!document.createElement('input').placeholder;
  }
  if (!supports_placeholder()) {
    // current browser does not support the placeholder
    // attribute. Apply placeholder to input manually        
    $("input[name='searchBox']").focus(function(){
      if ($(this).val() === "제목,배우,감독 검색") {
        $(this).val("");
      }
    }).blur(function(){
      if ($(this).val() === "") {
        $(this).val("제목,배우,감독 검색");
      }
    }).val("제목,배우,감독 검색");
  }
  $("input[name='searchBox']").autocomplete({
    source: "/api/get_info/",
    select: function( event, ui ) {
      var url = "/info/" + ui.item.info + "/" + ui.item.code;    
      $(location).attr('href',url);
    },
    minLength: 2,
  });
});

$(document).ready(function(){
  $(".fake_search_btn input").click(function() {
    var $query = $("input[name='searchBox']").val();
    var url = "http://10.20.16.52:8000/search/movie/title?query=" + $query;
    $(location).attr('href',url);
  });

  $("input[name='searchBox']").keydown(function (e){
    if(e.keyCode == 13) {
      var $query = $(this).val();
      var url = "http://10.20.16.52:8000/search/movie/title?query=" + $query;
      $(location).attr('href',url);
    }
  });

  $(".show-more a").on("click", function() {
    var $link = $(this);
    var $content = $link.parent().prev("div.text-content");
    var linkText = $link.text().toUpperCase();
     
    switchClasses($content);
 
    $link.text(getShowLinkText(linkText));
     
    return false;
  });
 
  function switchClasses($content){
    if($content.hasClass("short-text")){ 
        $content.switchClass("short-text", "full-text", 400);
    } else {
        $content.switchClass("full-text", "short-text", 400);
    }
  }
 
  function getShowLinkText(currentText){
    var newText = '';
     
    if (currentText === "펼쳐보기") {
        newText = "접기";
    } else {
        newText = "펼쳐보기";
    }
     
    return newText;
  }
});
