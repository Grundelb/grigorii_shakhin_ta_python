import requests

def test_get_method_punkapi():
    get_beer = requests.get('https://api.punkapi.com/v2/beers/8')

    assert get_beer.status_code == 200
    assert get_beer.json()[0]['name'] == 'Fake Lager'
    assert get_beer.json()[0]['abv'] == 4.7

def test_delete_method_punkapi():
    delete_beer = requests.delete('https://api.punkapi.com/v2/beers/8')
    assert delete_beer.status_code == 404
    assert delete_beer.json()['message'] == "No endpoint found that matches '/v2/beers/8'"