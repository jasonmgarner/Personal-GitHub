// from data.js
var tableData = data;
var tbody = d3.select("tbody")

console.log(data);


data.forEach(function(sightings) {
    console.log(sightings)
    var row = tbody.append("tr");
    
    Object.entries(sightings).forEach(function([key, value]) {
        console.log(key, value);
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

  console.log(filteredData);

});


  // Set filteredAddresses to addressData initially
var filteredDataSet = data;

// renderTable renders dataset to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredDataSet.length; i++) {

    // Get the current object and its fields
    var data = filteredDataSet[i];
    var fields = Object.keys(data);

    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {

      // For every field in the table object, create a new cell at set its inner text to be the current value at the current field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = data[field];
    
      renderTable();
    
    }
  }
}

