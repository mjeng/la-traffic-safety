import {Socket} from './demo-ws';

var apiKey = 'AIzaSyD_T8LTOKpg7oO6G9V21fRx2J_F-CawP14';

function initialize() {
  DEFAULT_ZOOM = 10;
  var mapOptions = {
    zoom: DEFAULT_ZOOM,
    center: {lat: 34.070330000000006, lng: -118.45489}
  }
  initSocket();
}

function initSocket() {
  console.log("Initializing websocket...");
  Socket.initialize(drive);
}

function demoDriveStart() {
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({'address': start_name}, function(results, status) {
  if (status == 'OK') {
    circle = new google.maps.Circle({
      map: map,
      center: results[0].geometry.location,
      radius: 150,
      strokeColor: '#FFFFFF',
      strokeOpacity: 1
      });
    }
  });
}

function drive(lat, lng) {
  circle.setCenter(new google.maps.LatLng(lat, lng));
}

window.onload = initialize;