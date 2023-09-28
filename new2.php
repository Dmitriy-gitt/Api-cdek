<?php
require 'vendor/autoload.php';

use folium\Folium;
use folium\plugins\Geocoder;

$map = new Folium\Map(['55.047874', '60.112206'], 8);
$d = [];

function search($lat, $long, $name_city, $s_1) {
    $marker = new Folium\Marker([$lat, $long]);
    $marker->setPopup($name_city);
    $marker->setTooltip($s_1);
    $marker->addTo($map);
    $map->save('mapcdek.html');
}

$geocoder = new Geocoder();
$geocoder->addTo($map);
$map->save('mapcdek.html');
?>