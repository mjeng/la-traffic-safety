
var apiKey = 'AIzaSyD_T8LTOKpg7oO6G9V21fRx2J_F-CawP14';

var map;
var drawingManager;
var placeIdArray = [];
var polylines = [];
var snappedCoordinates = [];
var autocomplete_start;
var autocomplete_end;
var directionService;
var directionsDisplay;
var start_name;
var end_name;
var marker;

processed_data=[]

function initialize() {
  DEFAULT_ZOOM = 10;
  var mapOptions = {
    zoom: DEFAULT_ZOOM,
    center: {lat: 34.070330000000006, lng: -118.45489}
  }
  map = new google.maps.Map(document.getElementById('map'), mapOptions);

  // Adds a Places search box. Searching for a place will center the map on that
  // location.
  map.controls[google.maps.ControlPosition.RIGHT_TOP].push(
      document.getElementById('bar'));
  autocomplete_start = new google.maps.places.Autocomplete(
      document.getElementById('autoc_start'));
  autocomplete_end = new google.maps.places.Autocomplete(
      document.getElementById('autoc_end'));
  marker = new google.maps.Marker({
          map: map,
          anchorPoint: new google.maps.Point(0, -29)
  });
  directionsService = new google.maps.DirectionsService;
  directionsDisplay = new google.maps.DirectionsRenderer({
    draggable: true,
    map: map,
    polylineOptions: {
      strokeOpacity: 0.8,
      strokeColor: "#0b69ed",
      zIndex: 1
    }
  });

  directionsDisplay.addListener('directions_changed', function() {
    colorPath(directionsDisplay.getDirections());
  });

  autocomplete_start.addListener('place_changed', (e) => {
    autoSetup(autocomplete_start, marker);
  });
  autocomplete_end.addListener('place_changed', (e) => {
    autoSetup(autocomplete_end, marker);
  });
}

function autoSetup(autocomplete, marker) {
  marker.setVisible(false);
  var place = autocomplete.getPlace();
  if (place.geometry.viewport) {
    map.fitBounds(place.geometry.viewport);
  } else {
    map.setCenter(place.geometry.location);
    map.setZoom(DEFAULT_ZOOM);
  }
  marker.setPosition(place.geometry.location);
  marker.setVisible(true);
}

function drawColoredPath(weightedData) {
  for (var i = 0; i < weightedData.length - 1; i++) {
    var coord1 = new google.maps.LatLng(weightedData[i][0], weightedData[i][1]);
    var coord2 = new google.maps.LatLng(weightedData[i+1][0], weightedData[i+1][1]);
    var weight = (weightedData[i][2] + weightedData[i+1][2]) / 2;

    var color = getColorFromWeight(weight);

    var polyline = new google.maps.Polyline({
      path: [coord1, coord2],
      strokeColor: color,
      strokeWeight: 4,
      zIndex: 2
    });
    polylines.push(polyline);
    polyline.setMap(map);
  }
}
function rgbToHex(r, g, b) {
  return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}

// function getColorFromWeight(weight) {
//   weight = weight / 140;
//   var r;
//   var g = 40;
//   var b = 40;
//   r = 30 + 170 * weight;

//   return rgbToHex(r, g, b);
// }

function getColorFromWeight(weight) {
  weight = weight;
  if (weight <= 0.25) {
    return 'green';
  }
  if (weight <= 0.50) {
    return 'yellow';
  }
  if (weight <= 0.75) {
    return 'orange';
  }
  return 'red';
}

// function getColorFromWeight(weight) {
//   weight = weight / 150;

//   var r = weight <= 0.5 ? 0 : 2 * 255 * weight - 255;
//   var g = weight <= 0.5 ? 255 - (255 * 2 * weight - 255) : 0;
//   var b = 0;

//   return rgbToHex(r, g, b);
// }


function findRoute() {
  marker.setVisible(false);
  displayRoute(start_name, end_name, directionsService,
      directionsDisplay);
}

function saveStart() {
  var place = autocomplete_start.getPlace();
  document.getElementById("saved_start").innerHTML = place.formatted_address;
  start_name = place.formatted_address;
}

function saveEnd() {
  var place = autocomplete_end.getPlace();
  document.getElementById("saved_end").innerHTML = place.formatted_address;
  end_name = place.formatted_address;
}

function displayRoute(origin, destination, service, display) {
  service.route({
    origin: origin,
    destination: destination,
    travelMode: 'DRIVING',
    avoidTolls: true
  }, function(response, status) {
    if (status === 'OK') {
      display.setDirections(response);
    } else {
      alert('Could not display directions due to: ' + status);
    }
  });
}

function colorPath(result) {
  var points = [];
  var myroute = result.routes[0].legs[0];
  var all = "";
  for (var i = 0; i < myroute.steps.length; i++) {
    for (var j = 0; j < myroute.steps[i].path.length; j++) {
      var lat = myroute.steps[i].path[j].lat();
      var lng = myroute.steps[i].path[j].lng();
      var tot = lat + " " + lng ;
      points.push(tot)
    }
  }
  for (var i = 0; i < polylines.length; i++) {
    polylines[i].setMap(null);
  }
  $.post("/scoreRoute", JSON.stringify(points)).then(res => {
    weightedData = JSON.parse(res);

    //store the processed data for this potential trip globally
    processed_data = weightedData

    drawColoredPath(weightedData);
    var s = 0;
    for (var i = 0; i < weightedData.length; i++) {
      s += weightedData[i][2];
    }
    console.log(s / weightedData.length);
  });
}

function getProcessedData(){
  var json_data = JSON.stringify(processed_data);
  return json_data;
}

function startDrive() {
  // call twillio python stuff
  $.post("/assistant", getProcessedData()).then(res =>{
    console.log(res.length);
  });
  window.location.replace("/calling");
}

window.onload = initialize;
