import requests
from hotels import info


def test_status_code_url():
    for value in info.values():
        h_url = value[0]
        response = requests.get(h_url)
        assert response.status_code == 200
