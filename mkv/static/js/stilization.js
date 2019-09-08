$(function () {
  $(".btn_start").addClass("btn_start_activate");
  $(".btn_start_main").addClass("btn_start_main_activate");

  $(document).on("click", ".btn_stop", function () {
    $(this).addClass("btn_stop_activate");
    $(this).parent().find(".btn_start").removeClass("btn_start_activate");
  });

  $(document).on("click", ".btn_start", function () {
    $(this).addClass("btn_start_activate");
    $(this).parent().find(".btn_stop").removeClass("btn_stop_activate");
  });

  $(document).on("click", ".btn_stop_main", function () {
    $(this).addClass("btn_stop_main_activate");
    $(this).parent().find(".btn_start_main").removeClass("btn_start_main_activate");
  });

  $(document).on("click", ".btn_start_main", function () {
    $(this).addClass("btn_start_main_activate");
    $(this).parent().find(".btn_stop_main").removeClass("btn_stop_main_activate");
  });

  $(document).on("click", ".btn_stop_monitoring", function () {
    $(this).addClass("btn_stop_main_activate");
    $(this).parent().find(".btn_start_monitoring").removeClass("btn_start_main_activate");
  });

  $(document).on("click", ".btn_start_monitoring", function () {
    $(this).addClass("btn_start_main_activate");
    $(this).parent().find(".btn_stop_monitoring").removeClass("btn_stop_main_activate");
  });

  // show date
  let date =  new Date();
  let year = date.getFullYear();
  let month = date.getMonth();
  let day = date.getDate();
  let month_array = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
                     "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"];
  month = month_array[month];
  let minutes = date.getMinutes();
  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  $('.date').text(day + "-е " + month + " "  + year + " года " +
                  date.getHours() + ":" + minutes);
});
