$(document).ready(function() {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  let csrftoken = getCookie('csrftoken');

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });

  let timer = 2950;
  function oneHundredMillisecondsPass() {
    let timer_el = document.getElementById("timer");
    timer_el.innerText = timer;
    timer -= 50;
  }

  $(document).on("click", ".main-command", function() {
    let url = new URL(window.location.href);
    let machineId = url.searchParams.get("machine_id");

    $(".main-command").prop("disabled", true);

    $.ajax({
      method: "POST",
      url: window.location.origin + "/remote-control/send-command/",
      contentType: "application/json; charset=UTF-8",
      data: JSON.stringify({command: this.value, machine_id: machineId}),
      error: function(jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
      },
      success: function(data, status) {
        let notification = $(".notification-after-ajax");
        let notificationWrapper = $(".wrapper-notification-after-ajax");
        notification.text("");

        if (data["status"] == "OK") {
          notification.css("color", "#3a3");
        }
        else if (data["status"] == "ERROR") {
          notification.css("color", "#a33");
        }

        notification.text(data["info"]);
        notificationWrapper.fadeIn(600);

        let interval = setInterval(oneHundredMillisecondsPass, 50);

        setTimeout(() => {
          notificationWrapper.fadeOut(600);
          console.log(timer);
          clearInterval(interval);
          $(".main-command").prop("disabled", false);
          timer = 2950;
        }, 3000);
      }
    });

  });
});
