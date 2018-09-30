// from data.js
var tableData = data;
var tbody = d3.select("tbody")

// console.log(data);


data.forEach(function(sightings) {
    // console.log(sightings)
    var row = tbody.append("tr");
    
    Object.entries(sightings).forEach(function([key, value]) {
        // console.log(key, value);
        var cell = tbody.append("td");
        cell.text(value);
    });
});

var filter= d3.select("#filter-btn");

filter.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);
  

  var filteredData = tableData.filter(event => event.datetime === inputValue);

  console.table(filteredData);

  tbody.html("CAN YOU BE TRUSTED!!!!IF YOU'RE A TRUE BELIEVER YOU CAN FIND WHAT YOU ARE SEEKKING IN THE CONSOLE. BEWARE OF WHAT YOU FIND. ONCE YOU SEE....YOU CANNOT UNSEE.");

  

});





