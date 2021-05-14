import pytest


@pytest.mark.objeto
def test_objeto(client):
    rv = client.get("/objeto/Aged Brie")
    assert {"name": "Aged Brie", "sell_in": 2, "quality": 0} == rv.get_json()
