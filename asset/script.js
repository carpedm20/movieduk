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


function randomItem(a) {
  return a[Math.floor(Math.random() * a.length)];
};

$(document).ready(function(){
  $page = 1;

  $(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
      $page += 1;

      if ($("#loading-ball").length === 0) {
        $("#info-list").append('<li id="loading-ball"><div class="ball1"></div><div class="footer"><p>Copyright © 2013 Kim Tae Hoon</p><p>Designed by carpedm20</p></div></li>');
      }

      $.ajax({
        type: "GET",
        url: "/api/get_list?count=5&page="+$page,
        dataType: "json",
        success: function(data) {
          $("#loading-ball").delay(200).fadeOut(400, function () {
             $(this).remove();
             d = data[0];
             $('#info-list').append(d.source);
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
        for(var i = 0; i < 15; i++) {
          $("#topActors").append("<li class='topActor'><a target='_blank' href='./info/actor/"+data[i+2].code+"'>"+data[i+2].name+"</a></li>");
        }
        movie1 = data[0];
        $('#leftThumb').attr("src", movie1.thumb_url);
        $('#leftActorName').text(movie1.name);
        $('#left_thumb_list').html('');
        for(var m in movie1.movies) {
          m = movie1.movies[m];
          $('#left_thumb_list').append('<li class="small_thumb_list_item" data-title="'+m.title1+'" style="display: list-item;"><div class="viewport"><a href="/info/movie/'+m.code+'" target="_blank"><span class="dark-background">'+m.title1+'</span><img src="'+m.poster_url+'?type=n77_110_2" width="48" height="60"></a></div></li>');
          $('.viewport').mouseenter(function(e) {
          $(this).children('a').children('img').animate({ height: '96', marginLeft: '-9.5', marginTop: '-18', width: '77'}, 0);
          $(this).children('a').children('span').fadeIn(0);
          $(this).children('a').css('position', 'relative');
          $(this).children('a').css('z-index', 1000);
        }).mouseleave(function(e) {
          $(this).children('a').children('img').animate({ height: '60', marginLeft: '0', marginTop: '0', width: '48'}, 0);
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
          $('#right_thumb_list').append('<li class="small_thumb_list_item" data-title="'+m.title1+'" style="display: list-item;"><div class="viewport"><a href="/info/movie/'+m.code+'" target="_blank"><span class="dark-background">'+m.title1+'</span><img src="'+m.poster_url+'?type=n77_110_2" width="48" height="60"></a></div></li>');

         $('.viewport').mouseenter(function(e) {
          $(this).children('a').children('img').animate({ height: '96', marginLeft: '-9.5', marginTop: '-18', width: '77'}, 0);
          $(this).children('a').children('span').fadeIn(0);
          $(this).children('a').css('position', 'relative');
          $(this).children('a').css('z-index', 1000);
        }).mouseleave(function(e) {
          $(this).children('a').children('img').animate({ height: '60', marginLeft: '0', marginTop: '0', width: '48'}, 0);
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
    $(this).children('a').children('img').animate({ height: '96', marginLeft: '-9.5', marginTop: '-18', width: '77'}, 0);
    $(this).children('a').children('span').fadeIn(0);
    $(this).children('a').css('position', 'relative');
    $(this).children('a').css('z-index', 1000);
  }).mouseleave(function(e) {
    $(this).children('a').children('img').animate({ height: '60', marginLeft: '0', marginTop: '0', width: '48'}, 0);
    $(this).children('a').children('span').fadeOut(0);
    $(this).children('a').css('z-index', -1);
  });

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
