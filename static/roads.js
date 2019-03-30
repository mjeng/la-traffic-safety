
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
  });

  directionsDisplay.addListener('directions_changed', function() {
    findPoints(directionsDisplay.getDirections());
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
    console.log("we here");
    map.setCenter(place.geometry.location);
    map.setZoom(DEFAULT_ZOOM);
  }
  marker.setPosition(place.geometry.location);
  marker.setVisible(true);
}

function drawColoredPath(weightedData) {
  for (var i = 0; i < weightedData.length - 1; i++) {
    var coord1 = weightedData[i].slice(0, 2);
    var coord1latlng = new google.maps.LatLng(coord1[0], coord1[1]);
    var coord2 = weightedData[i+1].slice(0, 2);
    var coord2latlng = new google.maps.LatLng(coord2[0], coord2[1]);
    // var weight = (weightedData[i][2] + weightedData[i+1][2]) / 2;
    var weight = 3;
    
    // var color = getColorForWeight(weight);
    color = 'purple'
    var polyline = new google.maps.Polyline({
      path: [coord1latlng, coord2latlng],
      strokeColor: color,
      strokeWeight: 2
    });
    polyline.setMap(map);
  }
}


// function getColorForSpeed(speed_kph) {
//   if (speed_kph <= 40) {
//     return 'purple';
//   }
//   if (speed_kph <= 50) {
//     return 'blue';
//   }
//   if (speed_kph <= 60) {
//     return 'green';
//   }
//   if (speed_kph <= 80) {
//     return 'yellow';
//   }
//   if (speed_kph <= 100) {
//     return 'orange';
//   }
//   return 'red';
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

function findPoints(result) {
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
  //console.log(JSON.stringify(points));
  $.post("/scoreRoute", JSON.stringify(points));
}

function startDrive() {
  // call twillio python stuff
  $.get("/assistant");
}

window.onload = initialize;



var data = [[34.070330000000006, -118.45489], [34.070330000000006, -118.45502], [34.070330000000006, -118.45502], [34.070310000000006, -118.45556], [34.0703, -118.45563000000001], [34.0703, -118.45568000000002], [34.0703, -118.45574], [34.07029, -118.45580000000001], [34.070280000000004, -118.45584000000001], [34.07027, -118.45590000000001], [34.070260000000005, -118.45597000000001], [34.070240000000005, -118.45602000000001], [34.07023, -118.45608000000001], [34.07021, -118.45612000000001], [34.070190000000004, -118.45617000000001], [34.07018, -118.45620000000001], [34.070170000000005, -118.45622000000002], [34.07014, -118.45627], [34.07012, -118.45631000000002], [34.07007, -118.45639000000001], [34.070040000000006, -118.45643000000001], [34.07, -118.4565], [34.069970000000005, -118.45653000000001], [34.06984, -118.45673000000001], [34.069630000000004, -118.45704], [34.06944, -118.45732000000001], [34.06936, -118.45743000000002], [34.069320000000005, -118.45749], [34.06929, -118.45754000000001], [34.06926, -118.45759000000001], [34.069230000000005, -118.45765000000002], [34.069190000000006, -118.45772000000001], [34.069160000000004, -118.45778000000001], [34.069120000000005, -118.45790000000001], [34.06909, -118.45800000000001], [34.06906, -118.45813000000001], [34.06904, -118.45823000000001], [34.06904, -118.45830000000001], [34.069030000000005, -118.45835000000001], [34.069030000000005, -118.45838], [34.069030000000005, -118.45842], [34.069030000000005, -118.45845000000001], [34.069030000000005, -118.45849000000001], [34.069030000000005, -118.45859000000002], [34.069030000000005, -118.45862000000001], [34.06908, -118.45961000000001], [34.06908, -118.45970000000001], [34.06908, -118.45972], [34.06908, -118.45975000000001], [34.06908, -118.45980000000002], [34.06907, -118.45984000000001], [34.06907, -118.45986], [34.06906, -118.45991000000001], [34.069050000000004, -118.45995], [34.06904, -118.45998000000002], [34.069030000000005, -118.46001000000001], [34.06902, -118.46005000000001], [34.069010000000006, -118.46008], [34.06899, -118.46011000000001], [34.068940000000005, -118.46021], [34.06893, -118.46023000000001], [34.06891, -118.46026], [34.06889, -118.46029000000001], [34.06888, -118.46031], [34.06886, -118.46033000000001], [34.068830000000005, -118.46037000000001], [34.06879, -118.46041000000001], [34.06875, -118.46045000000001], [34.06871, -118.46049000000001], [34.068670000000004, -118.46052000000002], [34.06864, -118.46053], [34.06861, -118.46055000000001], [34.068540000000006, -118.46059000000001], [34.0685, -118.46060000000001], [34.068470000000005, -118.46062], [34.06842, -118.46063000000001], [34.068360000000006, -118.46064000000001], [34.06833, -118.46064000000001], [34.068290000000005, -118.46065000000002], [34.068250000000006, -118.46065000000002], [34.06817, -118.46065000000002], [34.06812, -118.46065000000002], [34.06804, -118.46066], [34.06799, -118.46066], [34.06795, -118.46067000000001], [34.067910000000005, -118.46068000000001], [34.06788, -118.46069000000001], [34.06786, -118.46069000000001], [34.06781, -118.46071], [34.067780000000006, -118.46073000000001], [34.06776, -118.46074000000002], [34.06772, -118.46076000000001], [34.067690000000006, -118.46078000000001], [34.067660000000004, -118.4608], [34.067640000000004, -118.46081000000001], [34.067600000000006, -118.46085000000001], [34.06754, -118.46090000000001], [34.06752, -118.46093], [34.06749, -118.46096000000001], [34.067460000000004, -118.46100000000001], [34.06743, -118.46106], [34.0674, -118.46109000000001], [34.0673, -118.46125], [34.0673, -118.46125], [34.066990000000004, -118.46094000000001], [34.066880000000005, -118.46083000000002], [34.06682, -118.46077000000001], [34.066790000000005, -118.46074000000002], [34.06665, -118.46061], [34.0666, -118.46057], [34.066300000000005, -118.46031], [34.0662, -118.46022], [34.06575, -118.45989000000002], [34.065580000000004, -118.45975000000001], [34.06544, -118.45963], [34.065400000000004, -118.45960000000001], [34.06504, -118.45929000000001], [34.064370000000004, -118.45871000000001], [34.0642, -118.45857000000001], [34.06387, -118.45829], [34.063410000000005, -118.45790000000001], [34.062920000000005, -118.45748], [34.06264, -118.45723000000001], [34.06237, -118.45700000000001], [34.06163, -118.45637], [34.06141, -118.45617000000001], [34.061330000000005, -118.45611000000001], [34.061020000000006, -118.45584000000001], [34.0606, -118.45547], [34.06049, -118.45537000000002], [34.06027, -118.45518000000001], [34.06015, -118.45509000000001], [34.05971, -118.45472000000001], [34.059520000000006, -118.45457], [34.05857, -118.45375000000001], [34.05695, -118.45236000000001], [34.056540000000005, -118.45198], [34.05613, -118.45163000000001], [34.05613, -118.45163000000001], [34.05595, -118.45196000000001], [34.0559, -118.45204000000001], [34.05586, -118.45210000000002], [34.05574, -118.45231000000001], [34.055710000000005, -118.45236000000001], [34.055530000000005, -118.45269], [34.05543, -118.45287], [34.05543, -118.45287], [34.055420000000005, -118.45299000000001], [34.05541, -118.45303000000001], [34.055400000000006, -118.45308000000001], [34.055400000000006, -118.45312000000001], [34.05541, -118.45316000000001], [34.055420000000005, -118.45320000000001], [34.05543, -118.45325000000001], [34.05545, -118.45330000000001], [34.05547, -118.45332], [34.0555, -118.45335000000001], [34.05554, -118.45339000000001], [34.05565, -118.45348000000001], [34.05595, -118.45371000000002], [34.056110000000004, -118.45383000000001], [34.056160000000006, -118.45387000000001], [34.05621, -118.4539], [34.05622, -118.45391000000001], [34.05624, -118.45392000000001], [34.056270000000005, -118.45392000000001], [34.056290000000004, -118.45393000000001], [34.05631, -118.45393000000001], [34.056340000000006, -118.45393000000001], [34.056360000000005, -118.45393000000001], [34.056380000000004, -118.45393000000001], [34.05639, -118.45393000000001], [34.056430000000006, -118.45391000000001], [34.056470000000004, -118.45389000000002], [34.0565, -118.45387000000001], [34.056520000000006, -118.45385], [34.056540000000005, -118.45382000000001], [34.056560000000005, -118.45380000000002], [34.05657, -118.45378000000001], [34.05659, -118.45375000000001], [34.0566, -118.45373000000001], [34.056610000000006, -118.45371000000002], [34.056610000000006, -118.45368], [34.05662, -118.45365000000001], [34.05662, -118.45363], [34.056630000000006, -118.45361000000001], [34.056630000000006, -118.45359], [34.056630000000006, -118.45357000000001], [34.056630000000006, -118.45353000000001], [34.05662, -118.45349000000002], [34.05662, -118.45345], [34.056610000000006, -118.45343000000001], [34.0566, -118.45341], [34.056580000000004, -118.45337], [34.05655, -118.45333000000001], [34.05653, -118.45330000000001], [34.0565, -118.45327], [34.056450000000005, -118.45323], [34.055890000000005, -118.45264000000002], [34.055620000000005, -118.45240000000001], [34.055350000000004, -118.45216], [34.05496, -118.45184], [34.05463, -118.45156000000001], [34.05453, -118.45145000000001], [34.05451, -118.45143000000002], [34.054500000000004, -118.4514], [34.05447, -118.45129000000001], [34.054280000000006, -118.45112], [34.05391, -118.45082000000001], [34.053720000000006, -118.45067000000002], [34.053380000000004, -118.45043000000001], [34.05281, -118.45011000000001], [34.05256, -118.44998000000001], [34.05221, -118.44981000000001], [34.051700000000004, -118.44959000000001], [34.051, -118.44937000000002], [34.05057, -118.44923000000001], [34.05026, -118.44912000000001], [34.04992, -118.44898], [34.049760000000006, -118.44891000000001], [34.049510000000005, -118.44879000000002], [34.04936, -118.44871], [34.0491, -118.44855000000001], [34.04892, -118.44844], [34.0486, -118.44822], [34.04824, -118.44796000000001], [34.04798, -118.44775000000001], [34.04769, -118.4475], [34.04741, -118.44726000000001], [34.04693, -118.44684000000001], [34.046440000000004, -118.44643], [34.046170000000004, -118.4462], [34.04307, -118.44353000000001], [34.04261, -118.44314000000001], [34.04231, -118.44288000000002], [34.04079, -118.44159], [34.0397, -118.44061], [34.03929, -118.44027000000001], [34.03927, -118.44023000000001], [34.039120000000004, -118.44011], [34.03902, -118.44002], [34.038920000000005, -118.43995000000001], [34.0388, -118.43986000000001], [34.03873, -118.43981000000001], [34.03859, -118.43970000000002], [34.03853, -118.43966], [34.038360000000004, -118.43955000000001], [34.03811, -118.43939], [34.037940000000006, -118.4393], [34.03754, -118.43908], [34.03728, -118.43894000000002], [34.03719, -118.4389], [34.037060000000004, -118.43885000000002], [34.03699, -118.43882], [34.03679, -118.43871000000001], [34.03679, -118.43871000000001], [34.03672, -118.43875000000001], [34.036680000000004, -118.43877], [34.03665, -118.43877], [34.036620000000006, -118.43877], [34.036590000000004, -118.43876000000002], [34.03645, -118.43871000000001], [34.03642, -118.43870000000001], [34.03624, -118.43864], [34.03615, -118.43861000000001], [34.03605, -118.43857000000001], [34.03602, -118.43856000000001], [34.03598, -118.43854], [34.03557, -118.43836], [34.035340000000005, -118.43826000000001], [34.03524, -118.43820000000001], [34.03515, -118.43815000000001], [34.035140000000006, -118.43815000000001], [34.03504, -118.43809000000002], [34.034890000000004, -118.43799000000001], [34.034800000000004, -118.43793000000001], [34.034710000000004, -118.43786000000001], [34.03454, -118.43775000000001], [34.03436, -118.43762000000001], [34.03436, -118.43762000000001], [34.03428, -118.43752], [34.034220000000005, -118.43748000000001], [34.03408, -118.43736000000001], [34.034000000000006, -118.43728000000002], [34.0339, -118.43719000000002], [34.03369, -118.43698], [34.03304, -118.43634000000002], [34.03276, -118.43606000000001], [34.032540000000004, -118.43585000000002], [34.032410000000006, -118.43571000000001], [34.032360000000004, -118.43565000000001], [34.03231, -118.43557000000001], [34.03226, -118.43552000000001], [34.032160000000005, -118.43539000000001], [34.03211, -118.43532], [34.03202, -118.43519], [34.031940000000006, -118.43506000000001], [34.03191, -118.43501], [34.031870000000005, -118.43495000000001], [34.03182, -118.43486000000001], [34.03179, -118.43480000000001], [34.03173, -118.43469], [34.03166, -118.43456], [34.031600000000005, -118.43442], [34.03154, -118.43429], [34.03148, -118.43416], [34.03143, -118.43402], [34.03139, -118.43391000000001], [34.03136, -118.4338], [34.03132, -118.43367], [34.031290000000006, -118.43358], [34.03125, -118.43343000000002], [34.03121, -118.43326], [34.031180000000006, -118.43311000000001], [34.03116, -118.43299], [34.031130000000005, -118.43279000000001], [34.031110000000005, -118.43264], [34.03108, -118.43239000000001], [34.03107, -118.4321], [34.031060000000004, -118.43197], [34.031060000000004, -118.43183], [34.03107, -118.43169], [34.03107, -118.43157000000001], [34.03108, -118.43144000000001], [34.0311, -118.43127000000001], [34.031130000000005, -118.43099000000001], [34.031240000000004, -118.43033000000001], [34.03126, -118.43021000000002], [34.0313, -118.4299], [34.03137, -118.42946], [34.031400000000005, -118.42926000000001], [34.03144, -118.42898000000001], [34.031470000000006, -118.42879], [34.031470000000006, -118.42874], [34.03148, -118.42866000000001], [34.03148, -118.42853000000001], [34.031530000000004, -118.42797000000002], [34.03155, -118.42766], [34.031560000000006, -118.42750000000001], [34.031580000000005, -118.42742000000001], [34.031600000000005, -118.42738000000001], [34.031650000000006, -118.42734000000002], [34.03166, -118.42639000000001], [34.031650000000006, -118.42602000000001], [34.031650000000006, -118.42549000000001], [34.031670000000005, -118.42451000000001], [34.031670000000005, -118.42404], [34.031670000000005, -118.42356000000001], [34.03168, -118.42219000000001], [34.031690000000005, -118.42179000000002], [34.031690000000005, -118.42139000000002], [34.0317, -118.41884], [34.031710000000004, -118.41823000000001], [34.031710000000004, -118.41794000000002], [34.031710000000004, -118.41755], [34.03172, -118.41669], [34.03172, -118.41634], [34.03172, -118.41572000000001], [34.0317, -118.41554000000001], [34.0317, -118.41536], [34.0317, -118.41527], [34.031690000000005, -118.41515000000001], [34.03166, -118.41486], [34.03163, -118.41461000000001], [34.03161, -118.41444000000001], [34.031510000000004, -118.41389000000001], [34.03143, -118.41352], [34.03139, -118.41338], [34.031330000000004, -118.41321], [34.03123, -118.41290000000001], [34.03101, -118.41226], [34.03087, -118.41187000000001], [34.03076, -118.41154000000002], [34.03061, -118.41111000000001], [34.030590000000004, -118.41107000000001], [34.030460000000005, -118.41069000000002], [34.03041, -118.41051000000002], [34.03034, -118.41029], [34.03031, -118.41016], [34.03023, -118.40984], [34.030170000000005, -118.40952000000001], [34.030120000000004, -118.40924000000001], [34.03009, -118.40909], [34.03007, -118.40886], [34.030030000000004, -118.40851], [34.02998, -118.40801], [34.02987, -118.40666000000002], [34.02984, -118.40633000000001], [34.029790000000006, -118.40584000000001], [34.02976, -118.40547000000001], [34.02973, -118.4051], [34.029630000000004, -118.40402], [34.02957, -118.40334000000001], [34.02957, -118.40324000000001], [34.02953, -118.40276000000001], [34.029500000000006, -118.40244000000001], [34.029320000000006, -118.40044], [34.029230000000005, -118.39946], [34.029210000000006, -118.39924], [34.02917, -118.39866], [34.02913, -118.39823000000001], [34.02904, -118.39728000000001], [34.02902, -118.39692000000001], [34.02902, -118.39659], [34.02902, -118.39648000000001], [34.02902, -118.39633], [34.02902, -118.39618000000002], [34.029030000000006, -118.39607000000001], [34.02904, -118.39597], [34.029050000000005, -118.39580000000001], [34.029090000000004, -118.39538], [34.029120000000006, -118.39518000000001], [34.029160000000005, -118.39493000000002], [34.0292, -118.39467], [34.029270000000004, -118.39432000000001], [34.02931, -118.39415000000001], [34.02938, -118.39389000000001], [34.029410000000006, -118.39379000000001], [34.029500000000006, -118.39353000000001], [34.02953, -118.39344000000001], [34.029630000000004, -118.39317000000001], [34.029770000000006, -118.39283], [34.0298, -118.39275], [34.029920000000004, -118.39247], [34.03005, -118.39220000000002], [34.030190000000005, -118.39195000000001], [34.030280000000005, -118.39179000000001], [34.03052, -118.39137000000001], [34.03076, -118.39096], [34.03105, -118.39047000000001], [34.03132, -118.39001], [34.03154, -118.38963000000001], [34.03188, -118.38905000000001], [34.032450000000004, -118.38807000000001], [34.033480000000004, -118.38632000000001], [34.03374, -118.38589], [34.03383, -118.38574000000001], [34.03387, -118.38567], [34.03394, -118.38555000000001], [34.03398, -118.38549], [34.034000000000006, -118.38545], [34.03441, -118.38478], [34.03455, -118.38455], [34.034960000000005, -118.38384], [34.035030000000006, -118.38372000000001], [34.03555, -118.38284000000002], [34.03591, -118.38221000000001], [34.03618, -118.38170000000001], [34.03632, -118.38138000000001], [34.03651, -118.38087000000002], [34.036620000000006, -118.38052], [34.03669, -118.38024000000001], [34.036730000000006, -118.38006000000001], [34.036770000000004, -118.37989], [34.03681, -118.37966000000002], [34.036820000000006, -118.37954], [34.03685, -118.37930000000001], [34.03687, -118.37914], [34.036880000000004, -118.37899000000002], [34.03689, -118.37882], [34.03689, -118.37866000000001], [34.03689, -118.37835000000001], [34.03689, -118.37818000000001], [34.036880000000004, -118.37800000000001], [34.03687, -118.37787000000002], [34.036840000000005, -118.37755000000001], [34.0368, -118.37723000000001], [34.036730000000006, -118.37688000000001], [34.03665, -118.37649], [34.036570000000005, -118.37615000000001], [34.036530000000006, -118.37593000000001], [34.036480000000005, -118.37572000000002], [34.036480000000005, -118.37569], [34.03647, -118.37564], [34.036440000000006, -118.37551], [34.036440000000006, -118.37550000000002], [34.036390000000004, -118.37530000000001], [34.035900000000005, -118.37297000000001], [34.035810000000005, -118.37255], [34.03578, -118.37242], [34.03575, -118.37229], [34.03575, -118.37226000000001], [34.03571, -118.37208000000001], [34.035590000000006, -118.37152], [34.035410000000006, -118.37075000000002], [34.03521, -118.36975000000001], [34.03506, -118.36901], [34.035000000000004, -118.36875], [34.03497, -118.36863000000001], [34.03492, -118.36843], [34.034800000000004, -118.36786000000001], [34.03448, -118.36630000000001], [34.034420000000004, -118.36600000000001], [34.034330000000004, -118.36562], [34.03428, -118.36539], [34.034130000000005, -118.36469000000001], [34.03405, -118.36430000000001], [34.034000000000006, -118.36398000000001], [34.033950000000004, -118.36368000000002], [34.033930000000005, -118.36356], [34.033860000000004, -118.36302], [34.03383, -118.36272000000001], [34.03378, -118.36224000000001], [34.033770000000004, -118.36198], [34.033750000000005, -118.36181], [34.033730000000006, -118.36137000000001], [34.03372, -118.36103000000001], [34.03372, -118.36062000000001], [34.03372, -118.36027000000001], [34.033730000000006, -118.35981000000001], [34.033750000000005, -118.35945000000001], [34.03385, -118.35761000000001], [34.033930000000005, -118.35600000000001], [34.03394, -118.35589000000002], [34.03394, -118.35569000000001], [34.03394, -118.35568], [34.033970000000004, -118.35501000000001], [34.033970000000004, -118.35491], [34.03398, -118.35481000000001], [34.034000000000006, -118.35426000000001], [34.03403, -118.35349000000001], [34.034180000000006, -118.35050000000001], [34.03419, -118.35023000000001], [34.03419, -118.35022000000001], [34.03419, -118.35012], [34.034200000000006, -118.35002000000001], [34.034200000000006, -118.35001000000001], [34.03421, -118.34974000000001], [34.034380000000006, -118.34622000000002], [34.03441, -118.34554000000001], [34.03443, -118.34521000000001], [34.034440000000004, -118.34498], [34.03445, -118.34478000000001], [34.03445, -118.34462], [34.03445, -118.34446000000001], [34.03445, -118.34428000000001], [34.0345, -118.34341], [34.03452, -118.34284000000001], [34.03455, -118.34214000000001], [34.03459, -118.34151000000001], [34.03461, -118.34097000000001], [34.03463, -118.34063], [34.03464, -118.34032], [34.034670000000006, -118.33973], [34.034690000000005, -118.33939000000001], [34.034710000000004, -118.33903000000001], [34.03473, -118.33862], [34.03475, -118.33828000000001], [34.034760000000006, -118.33808], [34.034780000000005, -118.33770000000001], [34.03479, -118.33759], [34.03482, -118.33711000000001], [34.03482, -118.33701], [34.03484, -118.33671000000001], [34.03486, -118.33629], [34.034890000000004, -118.33574000000002], [34.03495, -118.33448000000001], [34.034980000000004, -118.33383], [34.03501, -118.33312000000001], [34.03504, -118.33247000000001], [34.03506, -118.33200000000001], [34.035090000000004, -118.3315], [34.03511, -118.33097000000001], [34.03515, -118.33012000000001], [34.03515, -118.32979], [34.0352, -118.32872], [34.035230000000006, -118.32820000000001], [34.035250000000005, -118.32773000000002], [34.03529, -118.32712000000001], [34.035340000000005, -118.32663000000001], [34.03538, -118.32632000000001], [34.03544, -118.32585], [34.03548, -118.32553000000001], [34.03555, -118.32506000000001], [34.035590000000006, -118.32476000000001], [34.03566, -118.32429], [34.03571, -118.32398], [34.03577, -118.32356000000001], [34.03577, -118.32352000000002], [34.03586, -118.32291000000001], [34.03587, -118.32283000000001], [34.035970000000006, -118.32212000000001], [34.03607, -118.32143], [34.03614, -118.32097], [34.036210000000004, -118.32056000000001], [34.03632, -118.31984000000001], [34.03634, -118.31975000000001], [34.0364, -118.31928], [34.03651, -118.31849000000001], [34.0366, -118.31781000000001], [34.03676, -118.31660000000001], [34.036840000000005, -118.31582000000002], [34.036860000000004, -118.31566000000001], [34.036880000000004, -118.31538], [34.036930000000005, -118.31458], [34.03694, -118.31445000000001], [34.036970000000004, -118.31395], [34.037000000000006, -118.31352000000001], [34.03701, -118.31319], [34.037040000000005, -118.31262000000001], [34.03705, -118.31222000000001], [34.03705, -118.31208000000001], [34.037060000000004, -118.31175], [34.037060000000004, -118.31154000000001], [34.03707, -118.31108], [34.03707, -118.31070000000001], [34.03708, -118.31034000000001], [34.03708, -118.30989000000001], [34.03708, -118.30958000000001], [34.03708, -118.30951], [34.037060000000004, -118.30851000000001], [34.037060000000004, -118.30829000000001], [34.037060000000004, -118.30784000000001], [34.037060000000004, -118.30770000000001], [34.03705, -118.30702000000001], [34.03705, -118.30674], [34.03703, -118.30508], [34.037020000000005, -118.30457000000001], [34.037020000000005, -118.30426000000001], [34.03703, -118.30397], [34.03703, -118.30397], [34.036970000000004, -118.30386000000001], [34.03696, -118.30380000000001], [34.03694, -118.30373000000002], [34.03694, -118.30364000000002], [34.036930000000005, -118.30354000000001], [34.0369, -118.30309000000001], [34.03689, -118.30291000000001], [34.03687, -118.30263000000001], [34.03685, -118.30233000000001], [34.036840000000005, -118.30209], [34.03683, -118.30189000000001], [34.036820000000006, -118.30180000000001], [34.036820000000006, -118.30170000000001], [34.03681, -118.30164], [34.0368, -118.30161000000001], [34.03678, -118.30154], [34.03679, -118.30112000000001], [34.0368, -118.30071000000001], [34.0368, -118.30031000000001], [34.03679, -118.29990000000001], [34.036770000000004, -118.29776000000001], [34.03676, -118.29750000000001], [34.03676, -118.29724000000002], [34.03674, -118.29709000000001], [34.03672, -118.29699000000001], [34.03672, -118.29694], [34.03669, -118.29633000000001], [34.03669, -118.29607000000001], [34.036680000000004, -118.29513000000001], [34.03665, -118.29498000000001], [34.03665, -118.29496], [34.036640000000006, -118.29495000000001], [34.03663, -118.29477000000001], [34.03661, -118.29454000000001], [34.03658, -118.29406000000002], [34.036570000000005, -118.29385], [34.036570000000005, -118.29369000000001], [34.036550000000005, -118.29351000000001], [34.036530000000006, -118.29319000000001], [34.036530000000006, -118.29309], [34.03651, -118.29289000000001], [34.03647, -118.29215], [34.036460000000005, -118.29176000000001], [34.036460000000005, -118.2917], [34.03647, -118.29158000000001], [34.03647, -118.29158000000001], [34.03622, -118.29157000000001], [34.036190000000005, -118.29157000000001], [34.036010000000005, -118.29157000000001], [34.035900000000005, -118.29157000000001], [34.03584, -118.29157000000001], [34.03568, -118.29156], [34.035650000000004, -118.29156], [34.035500000000006, -118.29156], [34.0352, -118.29157000000001], [34.035070000000005, -118.29157000000001], [34.03454, -118.29156], [34.03439, -118.29156], [34.03403, -118.29157000000001], [34.03367, -118.29156], [34.03358, -118.29156], [34.033500000000004, -118.29156], [34.03332, -118.29156], [34.0332, -118.29156], [34.03314, -118.29156], [34.03276, -118.29156], [34.0323, -118.29156], [34.03222, -118.29156], [34.032090000000004, -118.29156], [34.031960000000005, -118.29156], [34.03159, -118.29155000000002], [34.03107, -118.29155000000002], [34.03096, -118.29155000000002], [34.03092, -118.29155000000002], [34.03074, -118.29155000000002], [34.0306, -118.29156], [34.0305, -118.29156], [34.03045, -118.29156], [34.030210000000004, -118.29156], [34.03007, -118.29156], [34.029590000000006, -118.29156], [34.02868, -118.29156], [34.028400000000005, -118.29156], [34.027770000000004, -118.29156], [34.02743, -118.29156], [34.026880000000006, -118.29156], [34.02639, -118.29155000000002], [34.02602, -118.29155000000002], [34.02588, -118.29155000000002], [34.02564, -118.29156], [34.02564, -118.29156], [34.02553, -118.29161], [34.02545, -118.29161], [34.02545, -118.29149000000001], [34.02545, -118.29100000000001], [34.02545, -118.28995], [34.02545, -118.28893000000001], [34.02545, -118.28846000000001], [34.02545, -118.28834], [34.02545, -118.28828000000001], [34.02544, -118.28823000000001], [34.025420000000004, -118.28811], [34.02541, -118.28802], [34.02539, -118.28795000000001], [34.02534, -118.28777000000001], [34.02528, -118.28760000000001], [34.02516, -118.28734000000001], [34.02506, -118.28711000000001], [34.02506, -118.28711000000001], [34.02494, -118.28718]];