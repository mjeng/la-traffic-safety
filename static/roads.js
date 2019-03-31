
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
var marker;
var counter;
var locations;


function initialize() {
  DEFAULT_ZOOM = 10;
  var mapOptions = {
    zoom: DEFAULT_ZOOM,
    center: {lat: 34.070330000000006, lng: -118.45489},
    mapTypeControl: false,
    fullscreenControl: false
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
  document.getElementById("advance").style.display = "none";
  counter = 0;
  $("#drive")[0].disabled = true;
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
  var start = autocomplete_start.getPlace();
  var end = autocomplete_end.getPlace();
  start_name = start.formatted_address;
  end_name = end.formatted_address;
  marker.setVisible(false);
  displayRoute(start_name, end_name, directionsService,
      directionsDisplay);
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
      $("#drive")[0].disabled = false;
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
    drawColoredPath(weightedData);
    var s = 0;
    for (var i = 0; i < weightedData.length; i++) {
      s += weightedData[i][2];
    }
    console.log(s / weightedData.length);
  });
  locations = weightedData;
}

function startDrive() {
  // call twillio python stuff
  $.post("/assistant");
  // window.location.replace("/calling");
  displayCalling();

}

function displayCalling() {
  setTimeout(() => {
    $("#map")[0].style.display = "none";
    $(".calling")[0].style.display = "";
    $('.loop').html("Calling");
    loop(0);
  }, 200);
}

function loop(i) {
  setTimeout((i) => {
      if (i % 4 == 0) {
          $('.loop').html("Calling .");
      } else {
          $('.loop').html($('.loop').html() + " .");
      }
      loop(i + 1);
  }, 600, i);
}

function goToDemo() {
  $("#map")[0].style.display = "";
  $(".calling")[0].style.display = "none";
}

function demoDriveStart() {
  var geocoder = new google.maps.Geocoder();
  document.getElementById("advance").style.display = "";
  geocoder.geocode({'address': start_name}, function(results, status) {
  if (status == 'OK') {
    console.log("inside okay status");
    console.log(results[0].geometry.location.lat(), results[0].geometry.location.lng());
    circle = new google.maps.Circle({
      map: map,
      center: results[0].geometry.location,
      radius: 150,
      strokeColor: '#000000',
      strokeOpacity: 1,
      fillColor: '#444444',
      fillOpacity: 0.75
      });
    }
    $.post("/assistant");
  })
}

function drive() {
  if (counter < locations.length) {
    var lat = locations[counter][0];
    var lng = locations[counter][1];
    var weight = locations[counter][2];

    // var lat = parseFloat(locations[counter]);
    // var ind_space = locations[counter].indexOf(' ');
    // var lng = parseFloat(locations[counter].substring(ind_space + 1));
    counter = counter + 5;
    console.log(lat + " " + lng);
    circle.setCenter(new google.maps.LatLng(lat, lng));
    $.post("/demo/update", weight);
  } 
}



window.onload = initialize;
