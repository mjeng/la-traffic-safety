
var apiKey = 'AIzaSyD_T8LTOKpg7oO6G9V21fRx2J_F-CawP14';

var map;
var autocomplete_start;
var autocomplete_end;
var directionService;
var directionsDisplay;
var start_name;
var end_name;
var marker;
var geocoder;
var circle;


function initialize() {
  DEFAULT_ZOOM = 10;
  var mapOptions = {
    zoom: DEFAULT_ZOOM,
    center: {lat: 34.070330000000006, lng: -118.45489}
  }
  map = new google.maps.Map(document.getElementById('map'), mapOptions);
  geocoder = new google.maps.Geocoder();

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
    draggable: false,
    map: map,
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

function demoDriveStart() {
  geocoder.geocode({'address': start_name}, function(results, status) {
  if (status == 'OK') {
    console.log("inside okay status");
    console.log(results[0].geometry.location.lat(), results[0].geometry.location.lng());
    circle = new google.maps.Circle({
      map: map,
      center: results[0].geometry.location,
      radius: 150,
      strokeColor: '#FFFFFF',
      strokeOpacity: 1
      })
    }
  })
}

function drive(lat, lng) {
  circle.setCenter(new google.maps.LatLng(lat, lng));
}


window.onload = initialize;
