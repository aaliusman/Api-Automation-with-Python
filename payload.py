import mysql.connector
from utilities.configuration import *


def add_book_payload(isbn, aisle):
    body = {
        "name": "Learn Android",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Sidra Usman",
    }
    return body


def build_payload_from_db(query):
    add_body = {}
    tp = getQuery(query)
    add_body['name'] = tp[0]
    add_body['isbn'] = tp[1]
    add_body['aisle'] = tp[2]
    add_body['author'] = tp[3]
    return add_body


def add_place_payload():
    body = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91) 983 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }
    return body


def update_place_payload(place_id):
    body = {
        "place_id": place_id,
        "name": "Usman Academy",
        "address": "Philadelphia",
        "key": "qaclick123"
    }
    return body
