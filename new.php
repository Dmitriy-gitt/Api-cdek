<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;

$client = new Client();

$response = $client->post('https://api.edu.cdek.ru/v2/oauth/token?parameters', [
    'form_params' => [
        'grant_type' => 'client_credentials',
        'client_id' => 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI',
        'client_secret' => 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
    ]
]);

$data = json_decode($response->getBody(), true);
$token = $data['access_token'];

$name_city = ['Миасс', 'Златоуст', 'Челябинск', 'Москва'];
foreach ($name_city as $i) {
    $response = $client->get('https://api.edu.cdek.ru/v2/location/cities?city=' . $i, [
        'headers' => [
            'Authorization' => 'Bearer ' . $token
        ]
    ]);
    $get_city = json_decode($response->getBody(), true);
    $code = $get_city[0]['code'];

    $response = $client->get('https://api.edu.cdek.ru/v2/deliverypoints?city_code=' . $code, [
        'headers' => [
            'Authorization' => 'Bearer ' . $token
        ]
    ]);
    $get_adres = json_decode($response->getBody(), true);

    foreach ($get_adres as $i) {
        $s_1 = $i['location']['address_full'];
        $long = $i['location']['longitude'];
        $lat = $i['location']['latitude'];
        map_search($lat, $long, $name_city, $s_1);
    }
}

function map_search($lat, $long, $name_city, $s_1) {
    // Your map search function implementation here
}