from flask import request, jsonify
import pytest


@pytest.mark.wellcome
def testWellcome(client):
    rv = client.get("/")
    assert b'{"Wellcome": "to Ollivanders"}' in rv.data
    assert {"Wellcome": "to Ollivanders"} == rv.get_json()
