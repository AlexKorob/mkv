$(function() {
  let on = true;
  let MAX_COUNT = 20;
  let count = 0;
  let timeoutID = null;
  let graphs_names = ["chart_1", "chart_2", "chart_3", "chart_4"];
  let identificators = ["machine_1_1",
                        "machine_1_2",
                        "machine_1_3",
                        "machine_1_4"]; // for identificate Keys in document "update"
  let timestamp_array = [];


  function off() {
    clearTimeout(timeoutID);
    timeoutID = null;
  }


  function run() {
    timeoutID = setTimeout(start, 1000);
  }

  function connectToFirebase() {
    var config = {
        apiKey: "AIzaSyB5LR3UWNDjN4JUPRNjfr0snR4TpRwwsHI",
        authDomain: "mkv-kk.firebaseapp.com",
        databaseURL: "https://mkv-kk.firebaseio.com",
        projectId: "mkv-kk",
        storageBucket: "mkv-kk.appspot.com",
        messagingSenderId: "273816398845"
    };
    firebase.initializeApp(config);
    firebase.auth();

    var db = firebase.firestore();
    var docRef = db.collection("data").doc("update");

    return docRef
  }


  function appendGraph(data) {
    var time = new Date();
    console.log(timestamp_array);
    var update = {
      y: [[data[0]], [data[1]], [data[2]], [data[3]]],
      x: [[time], [time], [time], [time]]
    };
    // console.log(data[0], data[1], data[2]);

    Plotly.extendTraces('charts', update, [0, 1, 2, 3]);

    if (timestamp_array.length > MAX_COUNT){
      // var futureTime = time.setMinutes(time.getMinutes() + 0.1);
      timestamp_array.shift();
        var update_x_axis = {
          xaxis: {
            range: [timestamp_array[0], timestamp_array[timestamp_array.length - 1]]
          },
          xaxis2: {
            range: [timestamp_array[0], timestamp_array[timestamp_array.length - 1]]
          },
          xaxis3: {
            range: [timestamp_array[0], timestamp_array[timestamp_array.length - 1]]
          },
          xaxis4: {
            range: [timestamp_array[0], timestamp_array[timestamp_array.length - 1]]
          }
        };
      Plotly.relayout('charts', update_x_axis);
    }
    timestamp_array.push(time);

    // add to features
    $(".sigma").text(data[2]);
    $(".num_cycles").text(data[1]);
  };


  function buildGraphs() {
    var trace1 = {
      x: [],
      y: [],
      name: "Навантаження",
      type: 'scatter',
    };

    var trace2 = {
      x: [],
      y: [],
      name: "Кiлькiсть циклів",
      xaxis: 'x2',
      yaxis: 'y2',
      type: 'scatter',
    };

    var trace3 = {
      x: [],
      y: [],
      name: "Напруження",
      xaxis: 'x3',
      yaxis: 'y3',
      type: 'scatter',
    };

    var trace4 = {
      x: [],
      y: [],
      name: "Рiвень шуму",
      xaxis: 'x4',
      yaxis: 'y4',
      type: 'scatter',
    };

    var trace_data = [trace1, trace2, trace3, trace4];

    layout = {
      width: 825,
      height: 700,
      legend: {
        orientation: 'h',
        x: 0.2,
        y: 1.3,
      },
      margin: {
        pad: 10
      },
      // paper_bgcolor: '#7f7f7f',
      // plot_bgcolor: '#c7c7c7',
      yaxis: {domain: [0.65, 0.45], title: "P,кг"},
      yaxis2: {domain: [0.65, 0.45], title: "N"},
      yaxis3: {title: $("<p>").append("&sigma;<sub>н</sub>,МПа").html()},
      yaxis4: {title: $("<p>").append("&nu;").html()},
      grid: {rows: 2, columns: 2, pattern: 'independent'},
    };

    docRef.get().then(function(doc) {
      Plotly.newPlot("charts", trace_data, layout,
      {displayModeBar: false,
       scrollZoom: true,
       dragmode: "select",
       selectdirection: "any"});
    });
  }


  function start() {
    docRef.get().then(function(doc) {
      tmp_data_arr = []
      for (let i=0; i < identificators.length; i++){
        tmp_data_arr.push(doc.data()[identificators[i]]);
      }
      appendGraph(tmp_data_arr);
    });

    if (on == true) {
      run();
    }
  }

  // click on "main stop" button
  $(document).on("click", ".btn_stop_main", function(e) {
    on = false;
  });

  // click on "main start" button
  $(document).on("click", ".btn_start_main", function(e) {
    on = true;
    start();
  });

  var docRef = connectToFirebase();
  buildGraphs();
  start();
});
