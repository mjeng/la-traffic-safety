import {getStartEnd} from './roads';

var circle;


function demoDriveStart() {
  var geocoder = new google.maps.Geocoder();
  var poi = getStartEnd();
  var start_name = poi[0];
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
      });
    }
  })
}

function drive(lat, lng) {
  circle.setCenter(new google.maps.LatLng(lat, lng));
}


window.onload = initialize;

