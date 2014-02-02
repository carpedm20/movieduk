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

  // search box autocomplete
  $("input[name='searchBox']").autocomplete({
    source: "/api/get_info/",
    select: function( event, ui ) {
      var url = "/info/" + ui.item.info + "/" + ui.item.code;    
      $(location).attr('href',url);
    },
    minLength: 2,
  });
});

function actorThumbError(image){
  image.onerror = "";
  image.src = "http://static.naver.net/movie/2012/06/dft_img120x150.png";
  image.width = 111;
  image.height = 139;
  return true;
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

function randomItem(a) {
  return a[Math.floor(Math.random() * a.length)];
};

function check_movie(func, code) {
  $ajax_url = "/api/check_movie?func=" + func + "&code=" + code;
  $.ajax({
    type: "GET",
    url: $ajax_url,
    dataType: "json",
    success: function(data) {
    },
  });
}

function popup_login() {
  var loginBox = $("#login-box");
  //Fade in the Popup
  $(loginBox).fadeIn(300);
    
  //Set the center alignment padding + border see css style
  var popMargTop = ($(loginBox).height() + 24) / 2; 
  var popMargLeft = ($(loginBox).width() + 24) / 2; 
  
  $(loginBox).css({ 
    'margin-top' : -popMargTop,
    'margin-left' : -popMargLeft
  });
    
  // Add the mask to body
  $('body').append('<div id="mask"></div>');
  $('#mask').fadeIn(300);
    
  return false;
}

$is_login = false;

function is_login() {
  $ajax_url = "/api/is_login";
  $.ajax({
    type: "GET",
    url: $ajax_url,
    dataType: "json",
    success: function(data) {
      $is_login = data;
    },
  });
}

$(document).ready(function(){
  is_login();

  // initial state
  $("div.filtering").hide();
  $page = 0;

  // click outside of popup_login
  $('a.close, #mask').live('click', function() { 
    $('#mask , .login-popup').fadeOut(300 , function() {
      $('#mask').remove();  
    });
    return false;
  });

  // like_count
  $(document).on("click", "a.like_count", function() {
    return false;
  });

  $(document).on("click", "a.dislike_count", function() {
    return false;
  });

  $(document).on("click", "a.actor_like_count", function() {
    return false;
  });

  $(document).on("click", "a.actor_dislike_count", function() {
    return false;
  });

  $(document).on("click", "a.director_like_count", function() {
    return false;
  });

  $(document).on("click", "a.director_dislike_count", function() {
    return false;
  });

  // movie
  $(document).on("click", "a.like", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("like", $code);
      $(this).switchClass("like","liked");

      $obj =  $(".like_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) + 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.liked", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("like", $code);
      $(this).switchClass("liked","like");

      $obj =  $(".like_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) - 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.dislike", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("dislike", $code);
      $(this).switchClass("dislike","disliked");

      $obj =  $(".dislike_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) + 1);
    } else {
      popup_login();
    }

    return false;
  });

  $(document).on("click", "a.disliked", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("dislike", $code);
      $(this).switchClass("disliked","dislike");

      $obj =  $(".dislike_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) - 1);
    } else {
      popup_login();
    }
    return false;
  });

  // actor
  $(document).on("click", "a.actor_like", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("actor_like", $code);
      $(this).switchClass("actor_like","actor_liked");

      $obj =  $(".actor_like_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) + 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.actor_liked", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("actor_like", $code);
      $(this).switchClass("actor_liked","actor_like");

      $obj =  $(".actor_like_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) - 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.actor_dislike", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("actor_dislike", $code);
      $(this).switchClass("actor_dislike","actor_disliked");

      $obj =  $(".actor_dislike_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) + 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.actor_disliked", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("actor_dislike", $code);
      $(this).switchClass("actor_disliked","actor_dislike");

      $obj =  $(".actor_dislike_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) - 1);
    } else {
      popup_login();
    }
    return false;
  });

  // director
  $(document).on("click", "a.director_like", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("director_like", $code);
      $(this).switchClass("director_like","director_liked");

      $obj =  $(".director_like_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) + 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.director_liked", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("director_like", $code);
      $(this).switchClass("director_liked","director_like");

      $obj =  $(".director_like_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) - 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.director_dislike", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("director_dislike", $code);
      $(this).switchClass("director_dislike","director_disliked");

      $obj =  $(".director_dislike_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) + 1);
    } else {
      popup_login();
    }
    return false;
  });

  $(document).on("click", "a.director_disliked", function() {
    if ($is_login) {
      $code = $(this).attr('id');
      check_movie("director_dislike", $code);
      $(this).switchClass("director_disliked","director_dislike");

      $obj =  $(".director_dislike_count[id='"+$code+"']");
      $obj.text(parseInt($obj.text()) - 1);
    } else {
      popup_login();
    }
    return false;
  });

  // youtube
  $(".video").load("change", function() {
    $('.video').attr('height',$('.video').width() * 104 / 185);
  });

  $youtubeLoop = new Array();
  $(".youtube-loop").each(function() {
    $youtubeLoop.push($(this).attr('src'));
  });

  $youtubeCount = 9;
  $(".colorbox").colorbox({iframe:true, rel:'colorbox', innerWidth:750, innerHeight:500});
  /*$("#youtube-right").click(function() {
    $youtubeCount = $youtubeCount + 1;
    $(".video").attr('src', $youtubeLoop[$youtubeCount % 3]);
  });*/

  $("#youtube-left").click(function() {
    $youtubeCount = $youtubeCount - 1;
    $(".video").attr('src', $youtubeLoop[$youtubeCount % 3]);
  });

  // default
  $("input[type='checkbox']").attr("checked",false);
  $(".default-check").attr('checked',true);

  if($.cookie('genres') != null) {
    $genres = $.cookie('genres').split(",");
    if($genres != "all") {
      $.each($genres, function(index, value) {
        $("input[name='genre']:first").attr("checked",false);
        $("input[value='" + value + "']").attr('checked',true);
      });
    }
  }

  if($.cookie('nations') != null) {
    $nations = $.cookie('nations').split(",");
    if($nations != "all") {
      $.each($nations, function(index, value) {
        $("input[name='nation']:first").attr("checked",false);
        $("input[value='" + value + "']").attr('checked',true);
      });
    }
  }

  if($.cookie('years') != null) {
    $years = $.cookie('years').split(",");
    if ($years != "all") {
      $.each($years, function(index, value) {
        $("input[name='year']:first").attr("checked",false);
        $("input[value='" + value + "']").attr('checked',true);
      });
    }
  }

  if($.cookie('genres') != null && $.cookie('genres') != "all" || $.cookie('nations') != null && $.cookie('nations') != "all" || $.cookie('years') != null && $.cookie('years') != "all")
    $("#filter-openner").text("필터링됨")

  // apply filter
  $(".submit_filtering").click(function() {
    // genre
    $genres = new Array();

    if ($("input[name='genre']:first").is(':checked')) {
      $genres.push("all");
    } else {
      $("input[name='genre']:not(:first):checked").each(function() {
        $genres.push($(this).attr('value'));
      });
    }

    // nation
    $nations = new Array();

    if ($("input[name='nation']:first").is(':checked')) {
      $nations.push("all");
    } else {
      $("input[name='nation']:not(:first):checked").each(function() {
        $nations.push($(this).attr('value'));
      });
    }

    // year
    $years = new Array();

    if ($("input[name='year']:first").is(':checked')) {
      $years.push("all");
    } else {
      $("input[name='year']:not(:first):checked").each(function() {
        $years.push($(this).attr('value'));
      });
    }

    var params = new Array();

    params["genres"] = $genres;
    params["nations"] = $nations;
    params["years"] = $years;

    // save items to cookie, may be should save in user_info
    // $.cookie("test", 1);
    // $.removeCookie("test");

    $.cookie("genres", $genres, { expires: 7, path: '/' });
    $.cookie("nations", $nations, { expires: 7, path: '/' });
    $.cookie("years", $years, { expires: 7, path: '/' });

    //post_to_url("/filter", params, "post");
    if(document.URL.indexOf("/short") != -1)
      post_to_url("/short", params, "post");
    else
      post_to_url("/", params, "post");
  });

  // hide filter when click outer space
  $(document).click(function(event) { 
    if (!$(event.target).closest('#filter-openner').length)
      if (!$(event.target).closest('.filtering').length)
        if ($('.filtering').is(":visible"))
            $('.filtering').fadeOut("slow");
  });

  // show or hide filter
  $("#filter-openner").click(function() {
    if($("div.filtering").is(':visible'))
      $("div.filtering").fadeOut("slow");
    else
      $("div.filtering").fadeIn("slow");
  });

  // filter default button
  $(".submit_reset").click(function() {
    $("input[type='checkbox']").attr("checked",false);
    $(".default-check").attr('checked',true);
  });

  // if others are checked, ALL GENRE is unchecked
  $("input[name='genre']:not(:first)").click(function() {
    if($(this).is(':checked'))
      $("input[name='genre']:first").attr("checked",false);
    if($("input[name='genre']:not(:first):checked").length == 0)
      $("input[name='genre']:first").attr("checked",true);
  });

  // if ALL GENRE is checked, uncheck others
  $("input[name='genre']:first").click(function() {
    if($(this).is(':checked'))
      $("input[name='genre']:not(:first)").attr("checked",false);
  });

  // if others are checked, ALL NATION is unchecked
  $("input[name='nation']:not(:first)").click(function() {
    if($(this).is(':checked'))
      $("input[name='nation']:first").attr("checked",false);
    if($("input[name='nation']:not(:first):checked").length == 0)
      $("input[name='nation']:first").attr("checked",true);
  });

  // if ALL NATION is checked, uncheck others
  $("input[name='nation']:first").click(function() {
    if($(this).is(':checked'))
      $("input[name='nation']:not(:first)").attr("checked",false);
  });

  // if others are checked, ALL YEAR is unchecked
  $("input[name='year']:not(:first)").click(function() {
    if($(this).is(':checked'))
      $("input[name='year']:first").attr("checked",false);
    if($("input[name='year']:not(:first):checked").length == 0)
      $("input[name='year']:first").attr("checked",true);
  });

  // if ALL NATION is checked, uncheck others
  $("input[name='year']:first").click(function() {
    if($(this).is(':checked'))
      $("input[name='year']:not(:first)").attr("checked",false);
  });

  // infinite scroll
  $(window).scroll(function() {
    if($(".ball1").length == 0)
      return;

    if($(window).scrollTop() + $(window).height() == $(document).height() || $(window).scrollTop() + $(window).height() == $(document).height() - 1) {
      $page += 1;

      if ($(".loading-ball").length === 0) {
        $("#info-list").append('<li class="loading-ball"><div class="ball1"></div><div class="footer"><p>Copyright © 2013 Kim Tae Hoon</p><p>Designed by carpedm20</p></div></li>');
      }

      if (document.URL.indexOf("/search") !== -1) {
        $ajax_url =  "/api/get_search_list/";
      }
      else if (document.URL.indexOf("/short") === -1)
        $ajax_url =  "/api/get_list/";
      else
        $ajax_url =  "/api/get_short_list/";

      var formData = {};
      if (document.URL.indexOf("/search") !== -1) {
        var option =  document.URL.substr(document.URL.lastIndexOf("/")+1)
        formData["option"] = option.substr(0,option.indexOf("?"));
        formData["query"] = getParameterByName("query");
      }
      formData["count"] = 10;
      formData["page"] = $page;
      formData["genres"] = $.cookie("genres");
      formData["nations"] = $.cookie("nations");
      formData["years"] = $.cookie("years");

      $.ajax({
        type: "POST",
        url: $ajax_url,
        data : formData,
        dataType: "json",
        success: function(data) {
          $(".loading-ball").delay(200).fadeOut(400, function () {
            $(this).remove();
            d = data[0];
            $('#info-list').append(d.source);
            if(d.end)
              $('#info-list').append('<br/><li class="loading-ball"><div class="footer"><p>Copyright © 2013 Kim Tae Hoon</p><p>Designed by carpedm20</p></div></li>');
            else
              $('#info-list').append('<li class="loading-ball"><div class="ball1"></div><div class="footer"><p>Copyright © 2013 Kim Tae Hoon</p><p>Designed by carpedm20</p></div></li>');
          });
        },
        statusCode: {
          400: function() {
            var items = [];
            $.each( data, function( val ) {
              items.push( val );
            });
            $('p').html(items.join(""));
          }
        },
      });

    }
  });

  // actor ranking
  $(".choice-button").click(function(){
    if($(this).attr("choice") == "Left")
      $v = "left";
    else if($(this).attr("choice") == "Right")
      $v = "right";
    else
      $v = "middle";

    $.ajax({
      type: "GET",
      url: "/api/get_rank?value="+$v,
      dataType: "json",
      success: function(data) {
        $(".topActor").remove();
        for(var i = 0; i < 100; i++) {
          $("#topActors").append("<li class='topActor'><a target='_blank' href='./info/actor/"+data[i+2].code+"'>"+"#"+(i+1)+" "+data[i+2].name+"</a></li>");
        }
        movie1 = data[0];
        $('#leftThumb').attr("src", movie1.thumb_url);
        $('#leftActorName').text(movie1.name);
        $('#left_thumb_list').html('');
        for(var m in movie1.movies) {
          m = movie1.movies[m];
          $('#left_thumb_list').append('<li class="small_thumb_list_item" data-title="'+m.title1+'" style="display: list-item;"><div class="viewport"><a href="/info/movie/'+m.code+'" target="_blank"><span class="dark-background">'+m.title1+'</span><img src="'+m.poster_url+'?type=n77_110_2" width="44" height="60"></a></div></li>');
          $('.viewport').mouseenter(function(e) {
          $(this).children('a').children('img').animate({ height: '96', marginLeft: '-9.5', marginTop: '-18', width: '77'}, 0);
          $(this).children('a').children('span').fadeIn(0);
          $(this).children('a').css('position', 'relative');
          $(this).children('a').css('z-index', 1000);
        }).mouseleave(function(e) {
          $(this).children('a').children('img').animate({ height: '60', marginLeft: '0', marginTop: '0', width: '44'}, 0);
          $(this).children('a').children('span').fadeOut(0);
          $(this).children('a').css('z-index', -1);
        });
        }
        movie2 = data[1]
        $('#rightThumb').attr("src", movie2.thumb_url);
        $('#rightActorName').text(movie2.name);
        $('#right_thumb_list').html('');
        for(var m in movie2.movies) {
          m = movie2.movies[m];
          $('#right_thumb_list').append('<li class="small_thumb_list_item" data-title="'+m.title1+'" style="display: list-item;"><div class="viewport"><a href="/info/movie/'+m.code+'" target="_blank"><span class="dark-background">'+m.title1+'</span><img src="'+m.poster_url+'?type=n77_110_2" width="44" height="60"></a></div></li>');

         $('.viewport').mouseenter(function(e) {
          $(this).children('a').children('img').animate({ height: '96', marginLeft: '-9.5', marginTop: '-18', width: '77'}, 0);
          $(this).children('a').children('span').fadeIn(0);
          $(this).children('a').css('position', 'relative');
          $(this).children('a').css('z-index', 1000);
        }).mouseleave(function(e) {
          $(this).children('a').children('img').animate({ height: '60', marginLeft: '0', marginTop: '0', width: '44'}, 0);
          $(this).children('a').children('span').fadeOut(0);
          $(this).children('a').css('z-index', -1);
        });
        }
    var $rank_choice = new Array('하...','갖고싶어','갖고싶다','가질래','라면 먹고 갈래?','내가 낫다','누구세요?','명배우','멋져!','머싯다','갖고싶니?','역시 왼쪽이..','완전 내스타일','하... 노답','느낌있는데?','오 느낌있어','누구지?','듣보잡?','...?','아름답다','미인!','미남!','내 룸메가 낫다','노답','뭐야 이건','흠','그렇군...','역시 이쪽이...','얜 뭐지?','아따 이쁘다','헿','고민되는데','이쪽인가','저쪽인가','모르겠다...','하핳','완전 내스타일','내꺼','헤헿','역시','내 이상형','내 여친','여친보다 이뻐','음...','안녕하세요?',"I'm your father",'으악','내 눈!','정화된다...','눈정화','역시 이 배우지','고민고민하지마','이쪽?','저쪽?','으잉?','모르겠다','깬또깬또','왼쪽일까?','오른쪽일까?','둘다 노답','하... 못고르겠어','내꺼찜','여신!','미래의...','개쩜','개간지','소간지');
    var $i_dont_know = new Array('둘다 별로','둘다 으...','뭐지?','내가 낫다','내가 훨씬 낫다','노답들','노노노','스킵','다음 주세요','넥스트','투마로우','웟더','눈배림','내눈','내눈을 위하여','둘다 진짜...','둘다 여신','둘다 내스타일','둘다 내꺼','으악','정화가 필요해','다음','스킵스킵','노답노답','하...');

    $("#choice-left input").attr("value",randomItem($rank_choice));
    $("#choice-middle input").attr("value",randomItem($i_dont_know));
    $("#choice-right input").attr("value",randomItem($rank_choice));

      },
      statusCode: {
        400: function() {
          var items = [];
          $.each( data, function( val ) {
            items.push( val ); 
          });
          $('p').html(items.join(""));
        }
      }
    });
  });

  $('.viewport').mouseenter(function(e) {
    $(this).children('a').children('img').animate({ height: '110', marginLeft: '-9.5', marginTop: '-18', width: '77'}, 0);
    $(this).children('a').children('span').fadeIn(0);
    $(this).children('a').css('position', 'relative');
    $(this).children('a').css('z-index', 1000);
  }).mouseleave(function(e) {
    $(this).children('a').children('img').animate({ height: '68', marginLeft: '0', marginTop: '0', width: '50'}, 0);
    $(this).children('a').children('span').fadeOut(0);
    $(this).children('a').css('z-index', -1);
  });

  $(".fake_search_btn input").click(function() {
    var $query = $("input[name='searchBox']").val();
    var params = new Array();
    params["query"] = $query;
    $.cookie("query", $query);

    //post_to_url("/", params, "post");
    var url = "http://moza.us.to:8000/search/movie/title?query=" + $query;
    $(location).attr('href',url);
  });

  $("input[name='searchBox']").keydown(function (e){
    if(e.keyCode == 13) {
      var $query = $(this).val();
      var params = new Array();
      params["query"] = $query;
      $.cookie("query", $query);

      //post_to_url("/", params, "post");
      var url = "http://moza.us.to:8000/search/movie/title?query=" + $query;
      $(location).attr('href',url);
    }
  });

  // show more
  // $(document) is added for a new added dom elements
  $(document).on("click", ".show-more a", function() {
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

 var $walls = new Array('1_0_2008_07_09_13_20_50_32812.jpg',
'1.jpg',
'20(349).jpg',
'2652_1.jpg',
'300_wallpaper_hd-wide.jpg',
'338848.jpg',
'71509_S27_180908.jpg',
'abraham_lincoln_vampire_hunter-wallpaper-1920x1080.jpg',
'a.jpg',
'arrow___green_arrow-wallpaper-1920x1080.jpg',
'batman_8-wallpaper-1920x1080.jpg',
'batman_the_dark_knight_2-wallpaper-1920x1080.jpg',
'batman_trilogy-wallpaper-1920x1080.jpg',
'Before Sunset 2 - Ed.jpg',
'breaking_bad_science-wallpaper-1920x1080.jpg',
'burning_poker_joker-wallpaper-1920x1080.jpg',
'butterfly-effect-1920x1080.jpg',
'c0066036_51bc298c20fd7.jpg',
'c0111144_4d639016e973c.jpg',
'captain_america_movie_2011-wallpaper-1920x1080.jpg',
'darth-vader-star-wars-x-movie-wallpaper.jpg',
'film-titanic_clar.jpg',
'game_of_thrones-wallpaper-1920x1080.jpg',
'godfather_marlon_brando-wallpaper-1920x1080.jpg',
'good-will-hunting-original-1.jpg',
'great_power_great_responsibility-wallpaper-1920x1080.jpg',
'hitchhiker-the-hitchhikers-guide-to-galaxy-film-bureaublad-achtergronden-236650.jpg',
'hp7-wallpaper-1920x1080.jpg',
'hulk_smash-wallpaper-1920x1080.jpg',
'img15.jpg',
'inception_totem-wallpaper-1920x1080.jpg',
'ironman_1920xip_list-wallpaper-1920x1080.jpg',
'iron_man_3_2013_film-wallpaper-1920x1080.jpg',
'iron_man_3_iron_man_vs_mandarin-wallpaper-1920x1080 (1).jpg',
'iron_man_3_iron_man_vs_mandarin-wallpaper-1920x1080.jpg',
'joker_4-wallpaper-1920x1080.jpg',
'joker_smile-wallpaper-1920x1080.jpg',
'king_kong_vs_godzilla-wallpaper-1920x1080.jpg',
'leon_1994_movie_wallpaper-HD.jpg',
'Leonard-Sheldon-the-big-bang-theory-8631788-1920-1080.jpg',
'leon_the_professional_1994_wallpaper-wide.jpg',
'man_of_steel_2013_superman-wallpaper-1920x1080.jpg',
'man_of_steel_2015-wallpaper-1920x1080 (1).jpg',
'man_of_steel_2015-wallpaper-1920x1080 (2).jpg',
'man_of_steel_2015-wallpaper-1920x1080.jpg',
'man_of_steel_5-wallpaper-1920x1080.jpg',
'modern-family-season-3-sezonul-3-wallpaper-2.jpg',
'movies_oldboy_desktop_hd_wallpaper-normal.jpg',
'mu4tyb-1c05fe349dbb8eb346f9.jpg',
'pirates_of_the_caribbean_5_2013-wallpaper-1920x1080.jpg',
'pixar-monsters-5000x2887-wallpaper-2389493.jpg',
'sam_worthington_as_jake_sully-wallpaper-1920x1080.jpg',
'sherlockseason1.jpg',
'silver_linings_playbook-wallpaper-1920x1080.jpg',
'Skyfall, Daniel Craig.jpg',
'spider_man_4-wallpaper-1920x1080.jpg',
'spider_man_in_the_rain-wallpaper-1920x1080.jpg',
'spider_man-wallpaper-1920x1080.jpg',
'the_amazing_spider_man_2012_film-wallpaper-1920x1080.jpg',
'the_amazing_spiderman_2012-wallpaper-1920x1080.jpg',
'the_amazing_spider_man-wallpaper-1920x1080.jpg',
'the_dark_knight_rises_2013-wallpaper-1920x1080.jpg',
'the_dark_knight_rises_2-wallpaper-1920x1080.jpg',
'the_dark_knight_rises-wallpaper-1920x1080.jpg',
'the_dark_knight-wallpaper-1920x1080.jpg',
'the_godfather-wallpaper-1920x1080.jpg',
'The-Hobbit-2-Legolas.jpg',
'the_joker_painting-wallpaper-1920x1080.jpg',
'the_joker_the_dark_knight-wallpaper-1920x1080.jpg',
'The-Matrix-Reloaded-DI.jpg',
'thor_the_dark_world_2013_movie-wallpaper-1920x1080.jpg',
'thor_the_dark_world_loki-wallpaper-1920x1080.jpg',
'transformers_11-wallpaper-1920x1080.jpg',
'v_for_vendetta-wallpaper-1920x1080.jpg',
'watchmen_movie-wallpaper-1920x1080.jpg',
'-Pixar-Up-movie-Fresh-New-Hd-Wallpaper--.png');
  $('.login_background').css('background-image', 'url(/media/wallpaper/' + randomItem($walls) + ')');
});

function post_to_url(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.style.display = 'none';
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}
