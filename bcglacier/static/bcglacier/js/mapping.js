// $("#map").height($(window).height()).width($(window).width());
// map.invalidateSize();


var map = L.map( 'map', {
  // center: [37.094612, -95.713061],
  minZoom: 2,
  zoom: 5
});

// L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
// 	maxZoom: 17,
// 	attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
// }).addTo( map );

// add Stamen Watercolor to map.
//L.tileLayer.provider('Stamen.Watercolor').addTo(map);

// L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
// 	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
// 	subdomains: 'abcd',
// 	minZoom: 1,
// 	maxZoom: 16,
// 	ext: 'jpg'
// }).addTo(map);

// var Stamen_Terrain = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.{ext}', {
// 	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
// 	subdomains: 'abcd',
// 	minZoom: 0,
// 	maxZoom: 18,
// 	ext: 'png'
// }).addTo(map);

// var Esri_WorldTopoMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
// 	attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ, TomTom, Intermap, iPC, USGS, FAO, NPS, NRCAN, GeoBase, Kadaster NL, Ordnance Survey, Esri Japan, METI, Esri China (Hong Kong), and the GIS User Community'
// }).addTo(map);

var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// var Esri_NatGeoWorldMap = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', {
// 	attribution: 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC',
// 	maxZoom: 16
// }).addTo(map);

// custom camping icon
var myIcon = L.icon({
    iconUrl: "/static/bcglacier/camping-tent.png",
//    iconRetinaUrl: myURL + 'images/pin48.png',
    iconSize: [36, 36],
    iconAnchor: [9, 21],
    popupAnchor: [14, -14],
    tooltipAnchor: [18,0]
});

$( window ).on( "load", function() {
  // alert("dom is ready");
  // alert($("#navbarDropdown").text());
  // alert(document.getElementsByName("navbarDropdown").text);

// var map = L.map( 'map', {
//   center: [48.771154, -113.910081],
//   minZoom: 2,
//   zoom: 10
// });

//alert("setting nav bar");
if ($("#navbarDropdown").text().trim() == 'Glacier National Park') {
  // alert("found glacier");
  map.setView(new L.LatLng(48.771154, -113.910081), 10);
  // map.setZoom(10);
}
else if ($("#navbarDropdown").text().trim() == 'Yellowstone National Park') {
  // alert("found yellowstone");
  map.setView(new L.LatLng(44.580752, -110.363388), 9);
  // map.setZoom(9);
}
else {
  alert($("#navbarDropdown").text().trim());
  map.setView(new L.LatLng(37.094612, -95.713061), 5);
  // map.setZoom(5);
}



//OpenTopoMap
// L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
// 	attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
// 	subdomains: 'abcd',
// 	minZoom: 1,
// 	maxZoom: 16,
// 	ext: 'jpg'
// });

// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
// 	maxZoom: 19,
// 	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
// });



// }


setMarkers();

});

// set map setMapCenter
function setMapCenter(lat, long)
{
  map.panTo(new L.LatLng(lat, long));
}

// Update UI's markers
function setMarkers()
{
    let parameters = {};
    $.getJSON("setMarkers", parameters, function(markers, textStatus, jqXHR) {
		for ( var i=0; i < markers.length; ++i )
        {
		  // alert(JSON.stringify(markers[i].fields.latitude));
		  //alert(markers[i].fields.latitude);
          var M = L.marker( [markers[i].fields.latitude, markers[i].fields.longitude], {icon: myIcon});
		  // M.bindPopup( '<a href="' + markers[i].url + '" target="_blank">' + markers[i].name + '</a>' )
		  // Next one here brings up campsite detail in a seperate tab
          // M.bindPopup( '<a href="' + markers[i].pk + '/" target="_blank">' + markers[i].fields.name + '</a>' );
          M.bindPopup( '<a href="' + markers[i].pk + '/">' + markers[i].fields.name + '</a>' );
          M.bindTooltip( markers[i].fields.code,
           {
             permanent: true,
             direction: 'right'
           });
           M.addTo( map );
        }
    });
};
