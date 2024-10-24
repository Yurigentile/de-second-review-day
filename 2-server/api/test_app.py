from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_healthcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is Running"}

def test_info_doughnuts():
    response = client.get("/api/doughnuts/info")
    assert response.status_code == 200
    assert response.json() == {
    "doughnut_data": [
        {"doughnut_type":"Choccy Delight","price":1.38,"calories":800,"contains_nuts":True},
        {"doughnut_type":"Strawberry Haze","price":2.42,"calories":900,"contains_nuts":True},
        {"doughnut_type":"Sprinkly Bonanza","price":1.97,"calories":1000,"contains_nuts":True},
        {"doughnut_type":"Nutty Heaven","price":1.27,"calories":700,"contains_nuts":False},
        {"doughnut_type":"Caramel Caress","price":1.45,"calories":750,"contains_nuts":False},
        {"doughnut_type":"Delectable Delights","price":2.75,"calories":300,"contains_nuts":False},
        {"doughnut_type":"Banana Bonanza","price":1.87,"calories":585,"contains_nuts":False},
        {"doughnut_type":"Marshmallow Marsh","price":1.65,"calories":788,"contains_nuts":True},
        {"doughnut_type":"Rocky Road","price":2.22,"calories":999,"contains_nuts":True},
        {"doughnut_type":"Biscoff Gourmet","price":1.46,"calories":692,"contains_nuts":False}
    ]
}

def test_single_query():
    response = client.get("/api/doughnuts/info?max_calories=700&allow_nuts=true")
    assert response.status_code == 200
    assert response.json() == {
    "doughnut_data": [
        {"doughnut_type":"Delectable Delights","price":2.75,"calories":300,"contains_nuts":False},
        {"doughnut_type":"Banana Bonanza","price":1.87,"calories":585,"contains_nuts":False},
        {"doughnut_type":"Biscoff Gourmet","price":1.46,"calories":692,"contains_nuts":False}
    ]
}
