function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.609027, lng: -58.380925},
        zoom: 14,
    });

    var pinColor = "FE7569";
    var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34)
    );

    var contentString = '<b>Facultad de Ingenieria</b> </br> Paseo Colon 850</br> 4343-0893 </br> <a href="http://www.fi.uba.ar" target="_blank">www.fi.uba.ar</a>'
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    var marker = new google.maps.Marker({
        icon: pinImage,
        position: {lat: -34.617541, lng: -58.368290},
        map: map,
        title: 'Facultad de Ingenieria'
    });
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });

    var contentString = '<b>Facultad de asdasd</b> </br> Paseo Colon 850</br> 4343-0893 </br> <a href="http://www.fi.uba.ar" target="_blank">www.fi.uba.ar</a>'
    var infowindow2 = new google.maps.InfoWindow({
        content: contentString
    });
    var marker2 = new google.maps.Marker({
        icon: pinImage,

        position: {lat: -34.599886, lng: -58.373048},
        map: map,
        title: 'Facultad de Ingenieria'
    });
    marker2.addListener('click', function() {
        infowindow2.open(map, marker2);
    });
};