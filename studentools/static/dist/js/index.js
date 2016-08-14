
/** STYLES | ANIMATIONS**/
$(document).ready(function() {
    if (isMobile) {
        $('#map').height(300);
        $('#filter-title').hide();
        $('#filter-button').css('float', 'none');
    };
});

function load_data(name) {
    remove_filters();
    remove_localizations();
    add_filters = function(obj) { append_to_filter(obj.name); }
    request(name, add_filters);
    if (name == 'tea') {
        add_areas = function(obj) { add_area(obj); }
        request(name, add_areas);
    }
    else {
        add_markers = function(obj) { add_marker(obj); } 
        request(name, add_markers);
    }
    $(document).ajaxComplete( function(){
        show_localizations();
        set_css_to_filter_lines();
    });
}

/** GENERIC AJAX **/
function request(resource, to_do) { 
    $.ajax({
        url: '/api/v1/'+ resource +'/?format=json',
        type: 'GET',
        accepts: 'application/json',
        dataType: 'json',
        success: function(data) {
            for (var i=0; i < data.meta.total_count; i++) {
                var obj = data.objects[i];
                to_do(obj);
            }
        }
    })
}

/** FILTER **/
function remove_filters() {
    $('.filter-lines').remove();
}

function append_to_filter(name){
    var line = "<li class='filter-lines'><p>"+name+"</p></li>";
    $('#filter > ul').append(line);
}

function set_css_to_filter_lines() {
    $('.filter-lines').css({
            'padding': '15px 0px',
            'margin-top': '5px',
            'height': '50px',
            'border': '1px solid black',
    });
}


/** MAP **/
var map;
var localizations = [];


function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.609027, lng: -58.380925},
        zoom: 14,
    });
    return map;
}

function set_pin(color) {
    var pinColor = color;
    var pinImage = new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColor,
        new google.maps.Size(21, 34),
        new google.maps.Point(0,0),
        new google.maps.Point(10, 34)
    );
    return pinImage;
}

function add_marker(obj) {
    var contentString = '<b>'+ obj['name'] +'</b></br>'+ obj['address'] +'</br>'+ obj['phone']+'</br><a href="' + obj['web'] + '" target="_blank">' + obj['web'].substring(7) + '</a>';
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    var lat_lng = new google.maps.LatLng(obj['latitude'], obj['longitude']);
    var marker = new google.maps.Marker({
        icon: set_pin(obj['pin_color']),
        position: lat_lng,
        title: obj['tag']
    });
    
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });

    localizations.push(marker);
}

function add_area(obj) {
    var circle = new google.maps.Circle({
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.35,
      center: {lat: obj['latitude'], lng: obj['longitude']},
      radius: 150
    });
    localizations.push(circle);
}

function setMapOnAll(map){
    for (var i=0; i<localizations.length; i++) {
        localizations[i].setMap(map);
    }
}

function show_localizations() {
    setMapOnAll(map);
}

function remove_localizations() {
    setMapOnAll(null);
    localizations = [];
}