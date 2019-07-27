$(function() {
  var timeoutID = "";
  var time = new Date();


  var MAX_COUNT = 20;
  var counter = 0;
  var timestamp_array = [];

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
    firebase.auth().signInWithEmailAndPassword("mkv-k@i.ua", "hello1209");

    var db = firebase.firestore();
    var docRef = db.collection("data").doc("update");

    return docRef
  }

  var trace1 = {
    x: [],
    y: [],
    type: 'scatter',
  };

  var trace2 = {
    x: [],
    y: [],
    xaxis: 'x2',
    yaxis: 'y2',
    type: 'scatter',
  };

  var trace3 = {
    x: [],
    y: [],
    xaxis: 'x3',
    yaxis: 'y3',
    type: 'scatter',
  };

  var trace4 = {
    x: [],
    y: [],
    xaxis: 'x4',
    yaxis: 'y4',
    type: 'scatter',
  };

  var trace_data = [trace1, trace2, trace3, trace4];

  var layout = {
    width: 1080,
    height: 700,
    legend: {
      orientation: 'h',
      x: 0.3, // I’m editing this one
      y: 1.12,
    },
    margin: {
      pad: 10
    },
    paper_bgcolor: '#7f7f7f',
    plot_bgcolor: '#c7c7c7',
    // $("<p>").append("&sigma;<sub>н</sub>").html()
    yaxis: {domain: [0.6, 0.4], title: "Навантаження"},
    yaxis2: {domain: [0.6, 0.4], title: "Кількість циклів"},
    yaxis3: {title: "Напруження"},
    yaxis4: {title: "Рiвень шуму"},
    grid: {rows: 2, columns: 2, pattern: 'independent'},
  };

  Plotly.newPlot('charts', trace_data, layout, {displayModeBar: false, scrollZoom: true});

  function off() {
    clearTimeout(timeoutID);
    timeoutID = null;
  }

  function run() {
    timeoutID = setTimeout(start, 1000);
  }

  function start() {
    appendGraph([Math.random()+1,Math.random()+1,Math.random()+1,Math.random()+1]);
    run();
  };

  start();
});
