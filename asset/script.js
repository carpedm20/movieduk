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
  $page = 0;

  $(window).scroll(function() {
    if($(window).scrollTop() + $(window).height() == $(document).height()) {
      $page += 1;

      if ($("#loading-ball").length === 0) {
        //$("#info-list").append('<li id="loading-ball"><div class="ball"></div><div class="ball1"></div></li>')
        $("#info-list").append('<li id="loading-ball"><div class="ball1"></div><div class="footer"><p>Copyright © 2013 Kim Tae Hoon</p><p>Designed by carpedm20</p></div></li>')
      }

      $.ajax({
        type: "GET",
        url: "/api/get_list?count=5&page="+$page,
        dataType: "json",
        success: function(data) {
          $("#loading-ball").width("101%").delay(200).fadeOut(400, function () {
             $(this).remove();
          });
          d = data[0];
          $('#info-list').append(d.source);
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
    $.ajax({
      type: "GET",
      url: "/api/get_rank/",
      dataType: "json",
      success: function(data) {
        movie1 = data[0]
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
