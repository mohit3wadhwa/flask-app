$(function() {
  AOS.init();
});
// function myFunctionChart() {
//   // bar chart data
//   var barData = {
//     labels : [

//     ],

//     datasets : [{
//       fillColor: "rgba(151,187,205,0.2)",
//       strokeColor: "rgba(151,187,205,1)",
//       pointColor: "rgba(151,187,205,1)",
//       data : [
//         {% for item in values %}
//           "{{ item }}",
//         {% endfor %}
//       ]
//     }
//   ]
// }

// // get bar chart canvas
// var mychart = document.getElementById("chart").getContext("2d");

//   steps = 10
//   // max = {{max}}
//   max = 17000

//   // draw bar chart
//   new Chart(mychart).Bar(barData, {
//     scaleOverride: true,
//     scaleSteps: steps,
//     scaleStepWidth: Math.ceil(max / steps),
//     scaleStartValue: 0,
//     scaleShowVerticalLines: true,
//     scaleShowGridLines : true,
//     barShowStroke : true,
//     scaleShowLabels: true
//   }
//   );


function myFunction() {
  var x = 0;

  while (x == 0 | x > 6) {
    x = Math.floor(Math.random() * 10);
  }

  if (x==1) {
    document.getElementById("myImage").src='/static/images/dice_app/dice/dice_1.png';
  } else if (x==2) {
      document.getElementById("myImage").src='/static/images/dice_app/dice/dice_2.png';
  } else if (x==3) {
      document.getElementById("myImage").src='/static/images/dice_app/dice/dice_3.png';
  } else if (x==4) {
      document.getElementById("myImage").src='/static/images/dice_app/dice/dice_4.png';
  } else if (x==5) {
      document.getElementById("myImage").src='/static/images/dice_app/dice/dice_5.png';
  } else if (x==6) {
      document.getElementById("myImage").src='/static/images/dice_app/dice/dice_6.png';
  } else {
    console.log('x')
  }
}


function getBotResponse() {
  var rawText = $("#textInput").val();
  var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document
    .getElementById("userInput")
    .scrollIntoView({ block: "start", behavior: "smooth" });
  $.get("/get", { msg: rawText }).done(function(data) {
    var botHtml = '<p class="botText"><span>' + data + "</span></p>";
    $("#chatbox").append(botHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({ block: "start", behavior: "smooth" });
  });
}
$("#textInput").keypress(function(e) {
  if (e.which == 13) {
    getBotResponse();
  }
});